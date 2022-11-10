import argparse
import sys
import time
import warnings
from webbrowser import get

import requests,json,base64
warnings.filterwarnings("ignore")

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
parser.add_argument('-profileType', help='repository profile type', required=True);
parser.add_argument('-sharepath', help='sharepath', required=True);
parser.add_argument('-spcred', help='sharepath credential', required=True);
parser.add_argument('-protocol',help='protocol type',choices=['CIFS','NFS','HTTP','HTTPS','UNAVAILABLE'],required = True);
parser.add_argument('-certificateCheck',help ='certificate check required?',required = False);

args = vars(parser.parse_args())
ome_ip = args['ip'];
ome_user_name = args['ome_user'];
ome_cred = args['ome_pswd'];
omevv_user_name = args['omevv_user'];
omevv_cred = args['omevv_pswd'];
retry = 3;
payload ={};

def create_payload():
    if args["profilename"]:
        payload["profileName"] = args["profilename"];
    if args["description"] :
       payload["description"] = args["description"];
    if args["profileType"]:
        payload["profileType"] = args["profileType"];
    if args["sharepath"]:
        payload["sharePath"] = args["sharepath"];
    if args["protocol"]:
        payload["protocolType"] = args["protocol"];

    if args['protocol'] == "CIFS" and args['spcred'] == "":
        raise Exception('credential missing for sharedpath for CISF protocol')
    if args['spcred']:
        creds = args['spcred'].split("|");
        userName = creds[0];
        pswd = creds[1];
        spcred = {"username": userName.strip(),"password": pswd.strip()};
        payload['shareCredential'] = spcred

    if args["certificateCheck"]:
        payload["checkCertificate"] = args["certificateCheck"];








def get_uuid():
    uuid = "";
    url = "https://%s/omevv/GatewayService/v1/Consoles"%(ome_ip);
    encoded_cred = encode_cred(ome_user_name,ome_cred);
    cred_str = 'Basic '+encoded_cred;
    headers = {'Authorization': cred_str};
    response = requests.get(url,headers=headers,verify=False);
    status_code = response.status_code
    if status_code != 200:
       print("Error:Failed to retrieve the UUID ",response.content);
    else:
        data = response.json();
        uuid = data[0]['uuid']
    return uuid;

def encode_cred(username,pwd):
    cred_str = username+":"+pwd;
    cred_str_bytes = cred_str.encode("ascii");
    base64_bytes = base64.b64encode(cred_str_bytes);
    base64_string = base64_bytes.decode("ascii");
    return base64_string;

def create_repo_profl():
    global retry
    url = 'https://%s/omevv/GatewayService/v1/RepositoryProfiles'%(ome_ip);
    encoded_cred = encode_cred(omevv_user_name,omevv_cred);
    try:
        headers = {'content-type': 'application/json'}
        cred_str = 'Basic ' + encoded_cred;
        headers['Authorization'] = cred_str;
        headers['x_omivv-api-vcenter-identifier'] = get_uuid()
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False);
        data = response.json();
        status_code = response.status_code
        if status_code == 200:
          return "Repo is created successfully with id "+ str(data);
        else:
            raise Exception("Error occured while creaying the repo profile ",data);
    except Exception as e:
        print("Exception occured while creating repo ",e," retrying ..");
        if retry >0:
            retry = retry - 1;
            time.sleep(5);
            create_repo_profl();
            create_repo_profl();

        else:
            print("Failed after 3 retries,exiting");
            sys.exit();





if __name__ == "__main__":
    create_payload()
    print(create_repo_profl());
