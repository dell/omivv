from typing import Any, Dict, List, Optional, Union
import argparse
import warnings
from omevv_apis_client import AuthenticatedClient
import sys
import requests, json
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
import base64
import constants
import time
from omevv_apis_client.types import Response
from omevv_apis_client.api.console_management import remove_extensions
from omevv_apis_client.models.console_extension_request import ConsoleExtensionRequest
from omevv_apis_client.models.console_provider_type import ConsoleProviderType

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3

class UnregisterVcenters:
    def __init__(self):
        pass

    def create_payload(self, base_url, omeIp, omeUsercredential, vCenterUUID, payload, extensions):
        credential = omeUsercredential.username + ":" + omeUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {}
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.extensions = extensions
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

        self.consoleProviderTypeList = []
        for extension in self.extensions:
            if extension == "WEBCLIENT_PHA":
                self.consoleProviderTypeList.append(ConsoleProviderType('WEBCLIENT_PHA'))
            elif extension == "VLCM":
                self.consoleProviderTypeList.append(ConsoleProviderType('VLCM'))
            else:
                print("Invalid input for extensions. Please provide valid inputs.")
                sys.exit()
                
        self.json_body = ConsoleExtensionRequest(extensions=self.consoleProviderTypeList)
 
    def unregister_vcenters(self):        
        global retry
        try:
            response: Response[Union[Any, ErrorObject]] = \
                remove_extensions.sync_detailed(uuid=self.uuid, client=self.client, json_body=self.json_body)
            
            if response.status_code == 200:
                print("vCenter unregistered successfully for the given extensions")
            else:
                print(json.loads(response.content)["message"])        

        except Exception as e:
            print("Exception occured while unregistering vCenter(s) ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.unregister_vcenters();
            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OME Appliance IP")
    PARSER.add_argument("--omeusername", "--arg1", required=True, default=None, type = str, help="ome username")
    PARSER.add_argument("--omepassword", "--arg2", required=True, default=None, type = str, help="ome password")
    PARSER.add_argument("--vcUUID", "--arg3", required=True, default=None, type = str, help="vCenter uuid which needs to be unregistered")
    PARSER.add_argument("--extensions", "--arg4", nargs = '+', required=True, default=None, type = str, help="space separated extensions which needs to be unregistered. Possible values of extensions - WEBCLIENT_PHA, VLCM")
    
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.omeusername is not None and ARGS.omepassword is not None and ARGS.vcUUID is not None and ARGS.extensions is not None:
        if type(ARGS.extensions) == list:
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.omeusername, password=ARGS.omepassword)
            payload = {}
            unregistervcentershelper = UnregisterVcenters()
            unregistervcentershelper.create_payload(base_url=base_url, omeIp=ARGS.ip, omeUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, extensions=ARGS.extensions)
            unregistervcentershelper.unregister_vcenters()
        else:
            print("Invalid input. Extensions parameter should be a list") 
    else:
        print("Required parameters missing. Please review module help.")