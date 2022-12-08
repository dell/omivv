import argparse
import sys
import time
import warnings
from webbrowser import get

import requests
import json,base64
import re
warnings.filterwarnings("ignore")

class RepoProfileUtility:
    def __init__(self,ome_ip,ome_user,ome_pswd,omevv_user,omevv_pswd):
        self.headers = {'content-type': 'application/json'}
       # print("omevv_user ",omevv_user,"omevv_pswd ",omevv_pswd);
        omevv_encoded_cred = self.encode_cred(omevv_user, omevv_pswd)
        self.omevv_auth_cred = 'Basic ' + omevv_encoded_cred
        #print("omevv_user ", self.omevv_auth_cred);
        ome_encoded_cred = self.encode_cred(ome_user, ome_pswd)
        self.ome_auth_cred = 'Basic ' + ome_encoded_cred
        self.omevv_user_name = omevv_user
        self.omevv_pswd = omevv_pswd
        self.ome_console_url = 'https://%s/omevv/GatewayService/v1/Consoles'%(ome_ip)
        self.repo_prfl_url = 'https://%s/omevv/GatewayService/v1/RepositoryProfiles'%(ome_ip)
        self.retry = 3
        self.payload = {}

    def validate_path(self,protocol,sharedpath):
        isMatch = False
        path_regex_dict = {}
        path_regex_dict['HTTP'] = "^(http)://[-a-zA-Z0-9+&@#/%?=~_|,!:.;]*[-a-zA-Z0-9+@#/%=&_|](.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        path_regex_dict['HTTPS'] = "^(https)://[-a-zA-Z0-9+&@#/%?=~_|,!:.;]*[-a-zA-Z0-9+@#/%=&_|](.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        path_regex_dict['CIFS'] = "^(\\\\)+[a-zA-Z0-9+&@#\\/%?=~_|,!:.;](.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        path_regex_dict['NFS'] = ".*[:]{1}[\\/]{1}[^\\/].(.*)?.{1,255}[.]((i)xml.gz|xml|gz|cab)$"
        reg = re.compile(path_regex_dict[protocol])
        res = re.match(reg,sharedpath)
        if res is not None:
            isMatch = True
        return isMatch



    def encode_cred(self,username, pwd):
        cred_str = username + ":" + pwd;
        cred_str_bytes = cred_str.encode("ascii");
        base64_bytes = base64.b64encode(cred_str_bytes);
        base64_string = base64_bytes.decode("ascii");
        return base64_string;

    def create_payload(self,profname,desc,profileType,sharepath,protocolType,shareCred,checkCert):
        self.payload["profileName"] = profname
        self.payload["description"] = desc

        self.payload["profileType"] = profileType
        self.payload["sharePath"] = sharepath
        self.payload["protocolType"] = protocolType
        if args['spcred'] is not None and args['spcred'] != "":
            spcred = {}
            creds = args['spcred'].split("|");
            userName = creds[0];
            pswd = creds[1];
            # spcred = {"username": userName.strip(), "password": pswd.strip()};
            spcred["username"] = userName.strip()
            spcred["password"] = pswd.strip()
            self.payload['shareCredential'] = spcred
        self.payload["checkCertificate"] = checkCert


    def get_uuid(self):
        uuid = "";
        self.headers['Authorization'] = self.ome_auth_cred
        response = requests.get(self.ome_console_url, headers=self.headers, verify=False);
        status_code = response.status_code
        if status_code != 200:
            print("Error:Failed to retrieve the UUID ", response.content);
        else:
            data = response.json();
            uuid = data[0]['uuid']
        return uuid;

    def create_repo_profl(self):
        try:
            uuid = self.get_uuid()
          #  print(" uuid ",uuid)
            self.headers['x_omivv-api-vcenter-identifier'] = uuid
            self.headers['Authorization'] = self.omevv_auth_cred
          #  print(self.headers)
            response = requests.post(self.repo_prfl_url, data=json.dumps(self.payload), headers=self.headers, verify=False);
            data = response.json();
            status_code = response.status_code
           # print(status_code)
            if status_code == 200:
                return str(data);
            else:
                raise Exception("Error occured while creating the repo profile ", data);
        except Exception as e:
            print("Exception occured while creating repo ", e, " retrying ..");
            if self.retry > 0:
                self.retry = self.retry - 1;
                time.sleep(5);
                self.headers = {'content-type': 'application/json'}
                self.create_repo_profl();

            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script using OME api to create Repository profile"
    );
    parser.add_argument('-ip', help='OMEVV IP address', required=True);
    parser.add_argument('-ome_user', help='OME username', required=True);
    parser.add_argument('-ome_pswd', help='OME password', required=True);
    parser.add_argument('-omevv_user', help='OMEVV username', required=True);
    parser.add_argument('-omevv_pswd', help='OMEVV password', required=True);
    parser.add_argument('-profilename', help='repository profile name', required=True);
    parser.add_argument('-description', help='repository profile description', required=False);
    parser.add_argument('-profileType', help='repository profile type',choices=['Driver','Firmware'], required=True);
    parser.add_argument('-sharepath', help='sharepath', required=True);
    parser.add_argument('-spcred', help='sharepath credential', required=False);
    parser.add_argument('-protocol', help='protocol type', choices=['CIFS', 'NFS', 'HTTP', 'HTTPS', 'UNAVAILABLE'],
                        required=True);
    parser.add_argument('-certificateCheck', help='certificate check required?', required=False);

    args = vars(parser.parse_args())
    ome_ip = args['ip'];
    ome_user_name = args['ome_user'];
    ome_cred = args['ome_pswd'];
    omevv_user_name = args['omevv_user'];
    omevv_cred = args['omevv_pswd'];

    if args['protocol'] == "CIFS" and args['spcred'] == "":
        raise Exception('credential missing for sharedpath for CISF protocol')
    if args['profilename'] == "" and args['profilename'] is None:
        raise Exception('Profilename is a required parameter.Please pass a value for the same')



    repoProflutilobj = RepoProfileUtility(ome_ip,ome_user_name,ome_cred,omevv_user_name,omevv_cred)
    if (repoProflutilobj.validate_path(args["protocol"], args["sharepath"]) is not True):
        raise Exception('Please pass valid sharedpath location for the provided protocl type')
    repoProflutilobj.create_payload(args["profilename"],args["description"],args["profileType"],args["sharepath"],args["protocol"],args['spcred'],args["certificateCheck"])
    print(repoProflutilobj.create_repo_profl())
