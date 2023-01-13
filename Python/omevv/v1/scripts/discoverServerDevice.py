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
from omevv_apis_client.api.console_compliance_and_discovery import discover_hosts
from omevv_apis_client.models.create_hosts_discover_request import CreateHostsDiscoverRequest
from omevv_apis_client.models.host_discovery_group import HostDiscoveryGroup

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3

class HostDiscoveryWrapper:
    def __init__(self):
        pass

    def create_payload(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, jobname, jobdescription, console_entity_id, device_username, device_password):
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
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

        self.hostDiscoveryGroupList = []
        if self.console_entity_id and self.device_username and self.device_password:
            self.hostDiscoveryGroupList.append(HostDiscoveryGroup(console_entity_i_ds=self.console_entity_id, user_name=self.device_username, pass_word=self.device_password, use_global_credentials=False))

        self.json_body = CreateHostsDiscoverRequest(job_name=self.jobname, job_description=self.jobdescription, host_discovery_groups=self.hostDiscoveryGroupList)
            
    def run_discovery_job(self):        
        global retry
        try:
            response: Response[Union[ErrorObject, int]] = \
                discover_hosts.sync_detailed(uuid=self.uuid, client=self.client, json_body=self.json_body)
            
        except Exception as e:
            print("Exception occured while creating discovery job ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.run_discovery_job();
            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

        try:
            discovery_job_id = int(response.parsed)

        except Exception as exception:
            return response.parsed

        return "Discovery job is created successfully with job id "+ str(discovery_job_id)   

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
    PARSER.add_argument("--console_entity_id", nargs = '+', required=True, default=None, help="console entity id of the server device")
    PARSER.add_argument("--device_username", required=True, default=None, help="username of device")
    PARSER.add_argument("--device_password", required=True, default=None, help="password of device")

    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.jobname is not None and ARGS.console_entity_id is not None and ARGS.device_username is not None and ARGS.device_password is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        payload = {}
        hostdiscoveryhelper = HostDiscoveryWrapper()
        hostdiscoveryhelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, jobname=ARGS.jobname, jobdescription=ARGS.jobdescription, console_entity_id=ARGS.console_entity_id, device_username=ARGS.device_username, device_password=ARGS.device_password)
        print(hostdiscoveryhelper.run_discovery_job())
    else:
        print("Required parameters missing. Please review module help.")