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
from omevv_apis_client.api.console_management import register_console
from omevv_apis_client.models.console_create_request import ConsoleCreateRequest
from omevv_apis_client.models.console import Console
from omevv_apis_client.models.console_provider_type import ConsoleProviderType

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
retry = 3

class RegisterVcenter:
    def __init__(self):
        pass

    def create_payload(self, base_url, omeIp, omeUsercredential, vcusername, vcpassword, console_address, description, extensions):
        credential = omeUsercredential.username + ":" + omeUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {}
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.omeIp = omeIp
        self.vcusername = vcusername
        self.vcpassword = vcpassword
        self.console_address = console_address
        self.description = description
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

        self.vccredential = Credential(username=self.vcusername, password=self.vcpassword)
                
        self.json_body = ConsoleCreateRequest(extensions=self.consoleProviderTypeList, credential=self.vccredential, console_address=self.console_address, description=self.description)
 
    def register_vcenter(self):        
        global retry
        try:
            response: Response[Union[Console, ErrorObject]] = \
                register_console.sync_detailed(client=self.client, json_body=self.json_body)
            
            if response.status_code == 201:
                print("vCenter registered successfully for the given extensions")
            
            print(json.loads(response.content))        

        except Exception as e:
            print("Exception occured while registering vCenter ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.register_vcenter();
            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OME Appliance IP")
    PARSER.add_argument("--omeusername", "--arg1", required=True, default=None, type = str, help="ome username")
    PARSER.add_argument("--omepassword", "--arg2", required=True, default=None, type = str, help="ome password")
    PARSER.add_argument("--vcusername", "--arg3", required=True, default=None, type = str, help="vCenter username")
    PARSER.add_argument("--vcpassword", "--arg4", required=True, default=None, type = str, help="vCenter password")
    PARSER.add_argument("--console_address", "--arg5", required=True, default=None, type = str, help="name or ipaddress or fqdn of vCenter console")
    PARSER.add_argument("--description", "--arg6", required=False, default=None, type = str, help="description of vCenter console")
    PARSER.add_argument("--extensions", "--arg7", nargs = '+', required=True, default=None, type = str, help="space separated extensions which needs to be registered. Possible values of extensions - WEBCLIENT_PHA, VLCM")
    
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.omeusername is not None and ARGS.omepassword is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.console_address is not None and ARGS.extensions is not None:
        if type(ARGS.extensions) == list:
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.omeusername, password=ARGS.omepassword)
            registervcenterhelper = RegisterVcenter()
            registervcenterhelper.create_payload(base_url=base_url, omeIp=ARGS.ip, omeUsercredential=credential, vcusername=ARGS.vcusername, vcpassword=ARGS.vcpassword, console_address=ARGS.console_address, description=ARGS.description, extensions=ARGS.extensions)
            registervcenterhelper.register_vcenter()
        else:
            print("Invalid input. Extensions parameter should be a list") 
    else:
        print("Required parameters missing. Please review module help.")