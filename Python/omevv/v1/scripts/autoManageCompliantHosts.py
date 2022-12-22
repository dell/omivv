from typing import Any, Dict, List, Optional, Union, Tuple
import argparse
import sys
import constants
import time
from omevvServerManagement import HostsManagementWrapper
from omevv_apis_client.models import Credential
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3


def getDiscoveredHosts(ip, vcusername, vcpassword, vcuuid) -> Tuple[bool,dict]:
    global retry
    headers = {constants.vcGuidHeader: vcuuid}
    headers["Content-Type"] = "application/json"
    url = f"https://{ip}/omevv/GatewayService/v1/Consoles/{vcuuid}/Compliance"
    try:
        response = requests.get(url, headers=headers, verify=False, auth=(vcusername,vcpassword))
        response.raise_for_status()
        return (True, response.json())
    except requests.ReadTimeout as e:
        print("Exception occured while querying available host compliance ",e," retrying ..")
        if retry > 0:
            retry -= 1
            time.sleep(5)
            getDiscoveredHosts(ip, vcusername, vcpassword, vcuuid)
        else:
            return (False, {"Error": e})
    except requests.HTTPError as e:
        return (False, {"Error": e})


def getCompliantHostIds(discovered_hosts) -> Tuple[bool,list]:
    compliant_hosts = []
    for i in discovered_hosts:
        if i["state"] == "COMPLIANT":
            compliant_hosts.append(i["hostid"])
    if compliant_hosts:
        return (True, compliant_hosts)
    else:
        return (False, compliant_hosts)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OME Appliance IP")
    PARSER.add_argument("--vcusername", "-u", required=True,
                        help="username of vcenter")
    PARSER.add_argument("--vcpassword", "-p", required=True,
                        help="password of vcenter")
    PARSER.add_argument("--vcUUID", "-d", required=True, default=None,
                        help="UUID of the relevant vCenter")
    ARGS = PARSER.parse_args()

    success,response = getDiscoveredHosts(ARGS.ip, ARGS.vcusername, ARGS.vcpassword, ARGS.vcUUID)
    if success and response:
        success,host_ids = getCompliantHostIds(response)
        if success:
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
            jobname = f"API ManageJob-{time.ctime()}"
            hostmgmthelper = HostsManagementWrapper(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, \
                                            vCenterUUID=ARGS.vcUUID, payload={}, jobname=jobname, \
                                            jobdescription=None, host_ids=host_ids)
            hostmgmthelper.create_payload()
            print(hostmgmthelper.manage())
        else:
            print("SUCESS: No Discovered Hosts matching COMPLIANT state.")
    elif success and len(response) == 0:
        print("SUCCESS: No Unmanaged Hosts")
    else:
        print("FAILED: Error %s" % response)
