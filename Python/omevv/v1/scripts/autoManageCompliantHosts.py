from typing import Any, Dict, List, Optional, Union, Tuple
import argparse
import sys
import constants
import time
from omevvServerManagement import HostsManagementWrapper
from getManagementHostComplianceData import HostManagementComplianceWrapper
from omevv_apis_client.models import Credential
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3
valid_hosts = []

class AutoManageCompliantHostsWrapper:
    def __init__(self):
        pass

    def getValidHostIds(discovered_hosts) -> Tuple[bool,list]:
        for i in discovered_hosts:
            valid_hosts.append(i["hostid"])

        return valid_hosts    

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

        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        hostmgmtcompliancehelper = HostManagementComplianceWrapper()
        
        for compliance_filter in ["COMPLIANT","NONCOMPLIANT"]:        
            hostmgmtcompliancehelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, \
                                                    vCenterUUID=ARGS.vcUUID, compliance_filter=compliance_filter)  
            success,response = hostmgmtcompliancehelper.get_managed_hosts_compliance()
            if success:
                valid_hosts = getValidHostIds(response)

        jobname = f"API ManageJob-{time.ctime()}"
        if len(valid_hosts) > 0:
            hostmgmthelper = HostsManagementWrapper()
            hostmgmthelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, \
                                                vCenterUUID=ARGS.vcUUID, payload={}, jobname=jobname, \
                                                jobdescription=None, host_ids=valid_hosts)
            print(hostmgmthelper.run_manage_job())

        else:
            print("No Discovered Hosts available to be Managed. Please see Management Compliance State for Reason.")