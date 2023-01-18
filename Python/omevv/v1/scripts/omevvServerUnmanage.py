from typing import Any, Dict, List, Optional, Union
import argparse
import warnings
from omevv_apis_client import AuthenticatedClient
import sys
import requests, json
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
import constants
import base64
import time
from omevv_apis_client.types import Response
from omevv_apis_client.api.console_compliance_and_discovery import un_manage_hosts_by_console
from omevv_apis_client.models.un_manage_hosts_request import UnManageHostsRequest

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3

class UnmanageHostsWrapper:
    def __init__(self):
        pass

    def create_payload(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, jobname, jobdescription, host_ids):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {constants.vcGuidHeader: vCenterUUID}
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.jobname = jobname
        self.jobdescription = jobdescription
        self.host_ids = host_ids
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

        self.json_body = UnManageHostsRequest(host_i_ds=self.host_ids, job_name=self.jobname, job_description=self.jobdescription)
 
    def run_unmanage_job(self):        
        global retry
        try:
            response: Response[Union[ErrorObject, int]] = \
                un_manage_hosts_by_console.sync_detailed(uuid=self.uuid, client=self.client, json_body=self.json_body)
            
        except Exception as e:
            print("Exception occured while unmanaging servers ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.run_unmanage_job();
            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

        try:
            unmanage_job_id = int(response.parsed)

        except Exception as exception:
            return response.parsed

        return "Unmanage job is created successfully with job id "+ str(unmanage_job_id)   

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
    PARSER.add_argument("--host_ids", "--arg", nargs = '+', required=True, default=None, type = int, help="space separated list of host ids of the hosts to be unmanaged by OMEVV")

    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.jobname is not None and ARGS.host_ids is not None:
        if type(ARGS.host_ids) == list:
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
            payload = {}
            unmanagehosthelper = UnmanageHostsWrapper()
            unmanagehosthelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, jobname=ARGS.jobname, jobdescription=ARGS.jobdescription, host_ids=ARGS.host_ids)
            print(unmanagehosthelper.run_unmanage_job())
        else:
            print("Invalid input for host_ids") 
    else:
        print("Required parameters missing. Please review module help.")