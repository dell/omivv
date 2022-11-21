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
warnings.filterwarnings("ignore")
retry = 3

class HostDiscoveryWrapper:
    def __init__(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, jobname, jobdescription, console_entity_id, device_username, device_password, use_global_creds):
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
        self.console_entity_id = console_entity_id
        self.device_username = device_username
        self.device_password = device_password
        self.use_global_creds = use_global_creds
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

    def create_payload(self):
        if self.jobname:
            self.payload["jobName"] = self.jobname;
        if self.jobdescription:
            self.payload["jobDescription"] = self.jobdescription;

        hostDiscoveryGroupPayload = []
        hostDiscoveryGroupPayload.append(
            {
                "consoleEntityIDs": [self.console_entity_id],
                "userName": self.device_username,
                "passWord": self.device_password,
                "useGlobalCredentials": self.use_global_creds            
            }
        )

        if self.console_entity_id and self.device_username and self.device_password:
            self.payload["hostDiscoveryGroups"] = hostDiscoveryGroupPayload;

    def run_discovery(self):
        global retry
        headers = self.headers
        url = 'https://%s/omevv/GatewayService/v1/Consoles/%s/Hosts/Discover'%(self.omeIp, self.uuid)
        try:
            response = requests.post(url, data=json.dumps(self.payload), headers=headers, verify=False);
            data = response.json();
            status_code = response.status_code
            if status_code == 202:
              return "Discovery job is created successfully with id "+ str(data)
            elif status_code == 400 or status_code == 500 or status_code == 404:
                return "Error occured while creating discovery job : "+ str(data)
            else:
                raise Exception("Error occured while creating discovery job ",data);
        except Exception as e:
            print("Exception occured while creating discovery job ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                run_discovery();

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
    PARSER.add_argument("--console_entity_id", required=True, default=None, help="console entity id of the server device")
    PARSER.add_argument("--device_username", required=True, default=None, help="username of device")
    PARSER.add_argument("--device_password", required=True, default=None, help="password of device")
    PARSER.add_argument("--use_global_creds", required=True, default=None, help="indicate whether to use global credentials")

    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.jobname is not None and ARGS.console_entity_id is not None and ARGS.device_username is not None and ARGS.device_password is not None and ARGS.use_global_creds is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        payload = {}
        output=HostDiscoveryWrapper(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, jobname=ARGS.jobname, jobdescription=ARGS.jobdescription, console_entity_id=ARGS.console_entity_id, device_username=ARGS.device_username, device_password=ARGS.device_password, use_global_creds=ARGS.use_global_creds).create_payload()
        print(HostDiscoveryWrapper(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, jobname=ARGS.jobname, jobdescription=ARGS.jobdescription, console_entity_id=ARGS.console_entity_id, device_username=ARGS.device_username, device_password=ARGS.device_password, use_global_creds=ARGS.use_global_creds).run_discovery())
    else:
        print("Required parameters missing. Please review module help.")