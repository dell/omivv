#
#  Python script using OMIVV API to get host detail by service tag.
#
# _author_ = Prakash Ranjan <Prakash_Ranjan@Dell.com>
# _version_ = 0.1
#
# Copyright (c) 2021 Dell EMC Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
SYNOPSIS:
   Script to upload a licence in OMIVV.

DESCRIPTION:
   This script exercises the Spectre REST API to get a Vcenter datacenters,
   clusters and host. For authentication X-Auth is used over Basic
   Authentication
   Note that the credentials entered are not stored to disk.

EXAMPLE:
   python UploadLicense.py  --ip <xx>  --user <username> --password <pwd> --vcenterip <vcenterIP>
        --vcusername <vcUsername> --vcdomain <vcDomain> --vcpassword <vcpwd> 
"""
import sys
import argparse
from argparse import RawTextHelpFormatter
import json
import requests
import urllib3
import traceback

def upload_License(ip_address, user_name, password, bearer_token, vcenter_ip,  vc_username, vc_domain, vc_password,
                   share_type, share_location, share_username, share_domain, share_password):
    """Authenticate with OMIVV and enumerate reports."""
    try:
        local_bearer_token=None
        if(bearer_token == None):
            local_bearer_token = get_bearer_token(ip_address, user_name, password)
        else:
            local_bearer_token = bearer_token
            
        post_license(ip_address, local_bearer_token, share_type, share_location, share_username, share_domain, share_password)
            

        """ Log out from OMIVV """
        if(bearer_token == None):
            logout(ip_address, local_bearer_token)
    except:
        traceback.print_exc()
        print("get_vcenter_tree: Unexpected error:", sys.exc_info()[0])


def get_bearer_token(ip_address, user_name, password):
    try:
        baseurl = "https://" + ip_address + "/Spectre/api/rest/v1/Services/AuthenticationService/login"
        postBodyData = {"apiUserCredential": {"username": user_name, "domain": "", "password": password}}
        response = requests.post(baseurl, json=postBodyData, verify=False)
        if (response.status_code  == 200):
            json_response = response.json()
            bearerToken = json_response['accessToken']
            return bearerToken
        else:
            print("Login to OMIVV failed")
    except:
        print("get_bearer_token: Unexpected error:", sys.exc_info()[0])

def logout(omivvIP,session_token):
    try:
        head = {'Authorization': 'Bearer ' + session_token}
        url = "https://" + omivvIP + "/Spectre/api/rest/v1/Services/AuthenticationService/logoff"
        response = requests.post(url, verify=False, headers=head)
        if (response.status_code != 200):
            print("Log out failed.")
    except:
        print("logout: Unexpected error:", sys.exc_info()[0])


def get_registered_vcenter_list(omivvIP,bearerToken):
    """Get all registered vcenter with this OMIVV"""
    url ="https://" + omivvIP + "/Spectre/api/rest/v1/Services/ConsoleService/Consoles"
    head = {'Authorization': 'Bearer ' + bearerToken}
    response = requests.get(url, verify=False, headers=head)
    if(response.status_code == 200):
        json_response = json.dumps(response.json(), indent=4, sort_keys=True)
        return json_response
    else:
        print("Get registered vCenter list failed")

def post_license(omivv_ip, bearer_token, share_type, share_location, share_username, share_domain, share_password):
    base_url = "https://" + omivv_ip + "/Spectre/api/rest/v1/Services/LicenseService/Licenses"
    postBodyData = {"sharetype": share_type,
                    "path": share_location,
                    "credential": {"username": share_username, "domain": share_domain,
                                              "password": share_password}}
    head = {'Authorization': 'Bearer ' + bearer_token}
    jsonReponse = requests.post(base_url, json=postBodyData, verify=False, headers=head)
    if (jsonReponse.status_code != 200):
        json_response = json.dumps(jsonReponse.json(), indent=4, sort_keys=True)
        print(json_response)
        print("License upload failed.")
    else:
        json_response = json.dumps(jsonReponse.json(), indent=4, sort_keys=True)
        print(json_response)

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OMIVV Appliance IP")
    PARSER.add_argument("--user", "-u", required=False,
                        help="Username for OMIVV Appliance", default="admin")
    PARSER.add_argument("--password", "-p", required=False, default=None,
                        help="Password for OMIVV Appliance")
    PARSER.add_argument("--bearertoken", "-bt", required=False, default=None,
                        help="bearertoken for OMIVV Appliance")
    PARSER.add_argument("--vcenterip", "-vcip", required=True,
                        help="IP for vcenter")
    PARSER.add_argument("--vcusername", "-vcuser", required=True,
                        help="username of vcenter")
    PARSER.add_argument("--vcdomain", "-vcdomain", required=True,
                        help="domain of the vcenter")
    PARSER.add_argument("--vcpassword", "-vcpass", required=True,
                        help="password of vcenter")
    PARSER.add_argument("--shareType", "-stype", required=True, default=None,
                        help="license share type")
    PARSER.add_argument("--sharepath", "-spath", required=True, default=None,
                        help="path for the license file")
    PARSER.add_argument("--shareusername", "-susername", required=True, default=None,
                        help="share place username")
    PARSER.add_argument("--sharedomain", "-sdomain", required=True, default=None,
                        help="share place domain")
    PARSER.add_argument("--sharepassword", "-password", required=True, default=None,
                        help="password of shared location")
    
    ARGS = PARSER.parse_args()
    if(ARGS.password == None and ARGS.bearertoken == None):
        print("Pass either the password or the bearer token")
    upload_License(ARGS.ip, ARGS.user, ARGS.password, ARGS.bearertoken, ARGS.vcenterip,  ARGS.vcusername, ARGS.vcdomain, ARGS.vcpassword,
                     ARGS.shareType, ARGS.sharepath, ARGS.shareusername, ARGS.sharedomain, ARGS.sharepassword)
