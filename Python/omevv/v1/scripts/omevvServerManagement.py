from typing import Any, Dict, List, Optional, Union
import argparse
import sys
import json
import constants
import base64
import time
from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.models import Credential

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3

class HostsManagementWrapper:
    def __init__(self):
        self.headers["Content-Type"] = 'application/json'

    def create_payload(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, jobname, jobdescription, host_ids):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {constants.vcGuidHeader: vCenterUUID}
        self.headers["Authorization"] = basicAuth
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.jobname = jobname
        self.jobdescription = jobdescription
        self.host_ids = host_ids
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

        if self.host_ids:
            self.payload["hostIDs"] = self.host_ids
        if self.jobname:
            self.payload["jobName"] = self.jobname
        if self.jobdescription:
            self.payload["jobDescription"] = self.jobdescription

    def manage(self):
        global retry
        headers = self.headers
        url = 'https://%s/omevv/GatewayService/v1/Consoles/%s/Hosts/Manage'%(self.omeIp, self.uuid)
        try:
            response = requests.post(url, data=json.dumps(self.payload), headers=headers, verify=False);
            data = response.json();
            status_code = response.status_code
            if status_code == 202:
              return "Manage job is created successfully with id "+ str(data)
            elif status_code == 400 or status_code == 500 or status_code == 404:
                return "Error occured while creating manage job : "+ str(data)
            else:
                raise Exception("Error occured while creating manage job ",data);
        except Exception as e:
            print("Exception occured while creating manage job ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.manage();

            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

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
    PARSER.add_argument("--jobname", "-g", required=True, default=None, help="job name")
    PARSER.add_argument("--jobdescription", required=False, default=None, help="job description")
    PARSER.add_argument("--host_ids", "--arg", nargs = '+', required=True, default=None, type = int, help="space separated host ids of the hosts to be managed by OMEVV")

    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.jobname is not None and ARGS.host_ids is not None:
        if type(ARGS.host_ids) == list:
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
            hostmgmthelper = HostsManagementWrapper()
            hostmgmthelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload={}, jobname=ARGS.jobname, jobdescription=ARGS.jobdescription, host_ids=ARGS.host_ids)
            print(hostmgmthelper.manage())
        else:
            print("Invalid input for host_ids") 
    else:
        print("Required parameters missing. Please review module help.")