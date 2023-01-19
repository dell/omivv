import argparse
import sys
import time
import warnings
import base64
import constants
from webbrowser import get
import re
from omevv.v1.omevv_apis_client.models import Credential, ShareCredential
from omevv.v1.omevv_apis_client.models import ManagedHost
from omevv.v1.omevv_apis_client.models import ErrorObject,protocol_type,profile_type,share_credential
from omevv.v1.omevv_apis_client.api.repository_management import create_repository_profile
from omevv.v1.omevv_apis_client import AuthenticatedClient
from omevv.v1.omevv_apis_client.types import Response,UNSET
from typing import Any, Dict, List, Optional, Union
from omevv.v1.omevv_apis_client.models.create_repository_profile_request import CreateRepositoryProfileRequest



class CreateRepo:

    def __init__(self,ome_ip,omevv_user,omevv_pswd,uuid,):
        self.headers ={}
        self.payload = {}
        credential = Credential(username=omevv_user, password=omevv_pswd)
        appendedcredential = credential.username + ":" + credential.password
        basicAuth = "Basic %s" % base64.b64encode(appendedcredential.encode('utf-8')).decode()
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.headers['x_omivv-api-vcenter-identifier'] = uuid
        self.omeIp = ome_ip;
        self.uuid = uuid
        self.retry = 3
        self.base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ome_ip)
        self.client = AuthenticatedClient(base_url=self.base_url, token=None, verify_ssl=False). \
             with_headers(headers=self.headers)

    def validate_path(self, protocol, sharedpath):
        isMatch = False
        path_regex_dict = {}
        path_regex_dict[
            'HTTP'] = "^(http)://[-a-zA-Z0-9+&@#/%?=~_|,!:.;]*[-a-zA-Z0-9+@#/%=&_|](.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        path_regex_dict[
            'HTTPS'] = "^(https)://[-a-zA-Z0-9+&@#/%?=~_|,!:.;]*[-a-zA-Z0-9+@#/%=&_|](.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        path_regex_dict['CIFS'] = "^(\\\\)+[a-zA-Z0-9+&@#\\/%?=~_|,!:.;](.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        path_regex_dict['NFS'] = ".*[:]{1}[\\/]{1}[^\\/].(.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        reg = re.compile(path_regex_dict[protocol])
        res = re.match(reg, sharedpath)
        if res is not None:
            isMatch = True
        return isMatch

    def create_payload(self,profname,desc,profileType,sharepath,protocolType,shareCred,checkCert,domain):
        self.shr_cred_obj = UNSET
        if shareCred is not None and shareCred != "":
            spcred = {}
            creds = args['spcred'].split("|");
            userName = creds[0];
            pswd = creds[1];
            # spcred = {"username": userName.strip(), "password": pswd.strip()};
            self.shr_cred_obj = ShareCredential(userName.strip(),pswd.strip(),domain)
        self.create_repo_pro_obj = CreateRepositoryProfileRequest(profname,protocol_type.ProtocolType[protocolType],sharepath,desc,profile_type.ProfileType[profileType],checkCert,self.shr_cred_obj)


    def create_repo_profile(self,):
        try:

            response: Response[Union[ErrorObject, int]] = create_repository_profile.sync_detailed(client=self.client,json_body=self.create_repo_pro_obj)


        except Exception as e:
            print("Exception occured while creating profile \"%s\"" % e,"retrying")
            if self.retry > 0:
                self.retry = self.retry - 1
                time.sleep(5)
                self.create_repo_profile()
            else:
                print("Failed after 3 retries,exiting");
                sys.exit();
        try:
            repo_id = int(response.parsed)

        except Exception as e:
            return response.parsed
        return "Repository created successfully with id "+str(repo_id)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script using OME api to create Repository profile"
    );
    parser.add_argument('-ip', help='OMEVV IP address', required=True);
    parser.add_argument('-omevv_user', help='OMEVV username', required=True);
    parser.add_argument('-omevv_pswd', help='OMEVV password', required=True);
    parser.add_argument('-profilename', help='repository profile name', required=True);
    parser.add_argument('-description', help='repository profile description', required=False);
    parser.add_argument('-profileType', help='repository profile type', choices=['DRIVER', 'FIRMWARE'], required=True);
    parser.add_argument('-sharepath', help='sharepath', required=True);
    parser.add_argument('-spcred', help='sharepath credential', required=False);
    parser.add_argument('-protocol', help='protocol type', choices=['CIFS', 'NFS', 'HTTP', 'HTTPS', 'UNAVAILABLE'],
                        required=True);
    parser.add_argument('-certificateCheck', help='certificate check required?', required=False);
    parser.add_argument('-uuid', help='UUID for authentication', required=True);
    parser.add_argument('-domain', help='domain of share path', required=False);

    args = vars(parser.parse_args())
    ome_ip = args['ip'];
    omevv_user_name = args['omevv_user'];
    omevv_cred = args['omevv_pswd'];
    uuid = args['uuid'];

    if args['protocol'] == "CIFS" and args['spcred'] == "":
        print('credential missing for sharedpath for CISF protocol')
    if args['profilename'] == "" and args['profilename'] is None:
        print('Profilename is a required parameter.Please pass a value for the same')
    obj = CreateRepo(ome_ip,omevv_user_name,omevv_cred,uuid)
    if (obj.validate_path(args["protocol"], args["sharepath"]) is not True):
        print('Please pass valid sharedpath location for the provided protocl type')

    obj.create_payload(args["profilename"],args["description"],args["profileType"],args["sharepath"],args["protocol"],args['spcred'],args["certificateCheck"],args["domain"])
    print(obj.create_repo_profile())
