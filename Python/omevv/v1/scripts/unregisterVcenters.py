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

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class UnregisterVcenters:
    def __init__(self):
        self.headers["Content-Type"] = 'application/json'

    def create_payload(self, base_url, omeIp, omeUsercredential, vCenterUUID, payload, extensions):
        credential = omeUsercredential.username + ":" + omeUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {}
        self.headers["Authorization"] = basicAuth
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.extensions = extensions
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

        if self.extensions:
            self.payload["extensions"] = self.extensions

    def unregisterVc(self):
        headers = self.headers
        url = 'https://%s/omevv/GatewayService/v1/Consoles/%s/removeExtensions'%(self.omeIp, self.uuid)
        try:
            response = requests.post(url, data=json.dumps(self.payload), headers=headers, verify=False);
            status_code = response.status_code
            if status_code == 200:
              return "vCenter with uuid "+self.uuid+" unregistered successfully"
            elif status_code == 400 or status_code == 500 or status_code == 404:
                data = response.json()
                return "Error occured while unregistering : "+ str(data)
            else:
                data = response.json()
                raise Exception("Error occured while trying to attempt unregistration ",data);
        except Exception as e:
            print(e);

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OME Appliance IP")
    PARSER.add_argument("--omeusername", "--arg1", nargs = '+', required=True, default=None, type = str, help="space separated ome username")
    PARSER.add_argument("--omepassword", "--arg2", nargs = '+', required=True, default=None, type = str, help="space separated ome password")
    PARSER.add_argument("--vcUUID", "--arg3", nargs = '+', required=True, default=None, type = str, help="space separated vCenter uuids which needs to be unregistered")
    PARSER.add_argument("--extensions", "--arg4", nargs = '+', required=True, default=None, type = str, help="space separated extensions which needs to be unregistered")
    
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.omeusername is not None and ARGS.omepassword is not None and ARGS.vcUUID is not None and ARGS.extensions is not None:
        if type(ARGS.omeusername) == list and type(ARGS.omepassword) == list and type(ARGS.vcUUID) == list and type(ARGS.extensions) == list:
            for i in range(0, len(ARGS.vcUUID)):
                base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
                credential = Credential(username=ARGS.omeusername[i], password=ARGS.omepassword[i])
                payload = {}
                unregistervcentershelper = UnregisterVcenters()
                unregistervcentershelper.create_payload(base_url=base_url, omeIp=ARGS.ip, omeUsercredential=credential, vCenterUUID=ARGS.vcUUID[i], payload=payload, extensions=ARGS.extensions)
                print(unregistervcentershelper.unregisterVc())
        else:
            print("Invalid input. Each input parameter should be a list") 
    else:
        print("Required parameters missing. Please review module help.")