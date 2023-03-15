from typing import Any, Dict, List, Optional, Union, Tuple
import argparse
from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.api.console_compliance_and_discovery import get_host_compliance
from omevv_apis_client.models import ManagedHost
from omevv_apis_client.models import HostCompliance
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
import constants
import base64
import xlwt
import time
import sys
import csv
import json
import utilities as utility_object
from omevv_apis_client.types import Response

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3

class HostManagementComplianceWrapper:
    def __init__(self):
        pass

    def create_payload(self, base_url, omeIp, vcUsercredential, vCenterUUID, compliance_filter):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {constants.vcGuidHeader: vCenterUUID}
        self.headers["Authorization"] = basicAuth
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.compliance_filter = compliance_filter
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

    def get_managed_hosts_compliance(self) -> Tuple[bool,object]:
        global retry
        try:
            response: Response[Union[ErrorObject, List[HostCompliance]]] = \
                get_host_compliance.sync_detailed(uuid=self.uuid, client=self.client)

            status_code = response.status_code
            if status_code == 200:
                data = json.loads(response.content)
            
                filtered_data = []
                for entry in data:
                    if entry['state'] == self.compliance_filter:
                        filtered_data.append(entry)

                return (True, filtered_data)
            elif status_code == 400 or status_code == 500 or status_code == 404 or status_code == 401 or status_code == 403:
                return (False, response.parsed)
            else:
                raise Exception("Error occured while getting host management compliance data");
        except Exception as e:
            print("Exception occured while getting host management compliance data ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.get_managed_hosts_compliance();

            else:
                print("Failed after 3 retries,exiting");
                return False,e

        return False,''

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
    PARSER.add_argument("--compliance_filter", "-g", required=True, default=None, help="compliance_filter")
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.compliance_filter is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        hostManagementComplianceWrapper = HostManagementComplianceWrapper()
        hostManagementComplianceWrapper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, compliance_filter=ARGS.compliance_filter)
        file_name = "host_management_compliance_data.csv";
        success, response = hostManagementComplianceWrapper.get_managed_hosts_compliance()
        if success and response is not None and len(response) > 0: 
            utility_object.Utilities().write_to_csv(response, file_name)
            print("Host management compliance data has been retrieved successfully in downloaded csv file")
        elif success and len(response) == 0:
            print("Not able to retrieve compliance data for the input compliance filter",ARGS.compliance_filter)
        else:
            print("Error occured while getting host management compliance data",response)
                
    else:
        print("Required parameters missing. Please review module help.")