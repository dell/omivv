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
   Script to cancel or delete the job in OMIVV

DESCRIPTION:
   This script exercises the Spectre REST API to cancel or delete a job in OMIVV. 
   For authentication X-Auth is used over Basic Authentication
   Note that the credentials entered are not stored to disk.

EXAMPLE:
   python CancelOrDeleteAJobByName.py  --ip <xx>  --user <username> --password <pwd> --vcenterip <vcenterIP>
        --vcusername <vcUsername> --vcdomain <vcDomain> --vcpassword <vcpwd> 
"""
import sys
import argparse
from argparse import RawTextHelpFormatter
import json
import requests
import urllib3
import traceback


def get_vcenter_tree(ip_address, user_name, password, bearer_token, vcenter_ip,  vc_username, vc_domain, vc_password, action, job_name):
    """Authenticate with OMIVV and enumerate reports."""
    try:
        local_bearer_token=None
        if(bearer_token == None):
            local_bearer_token = get_bearer_token(ip_address, user_name, password)
        else:
            local_bearer_token = bearer_token
        """ Get all registered vcenter """
        registered_vcenter_list =  get_registered_vcenter_list(ip_address, local_bearer_token)
        if(registered_vcenter_list is None):
            print("No vcenter is regsitered with this OMIVV")
            return
        else:
            vcenter_id = None;
            registered_vc_array = json.loads(registered_vcenter_list)
            for vc in registered_vc_array:
                if vcenter_ip.upper() == vc['ip'].upper():
                    vcenter_id = vc['id']

            #Set operational Context.
            set_operational_context(ip_address, vcenter_id, local_bearer_token, vc_username, vc_domain, vc_password)
            # Get all update Jobs

            all_update_job = get_all_update_jobs(ip_address, local_bearer_token)
            if all_update_job is not None:
                if(job_name is None):
                    print("Pass the job name")
                else:
                    all_jobs = json.loads(all_update_job)
                    for job in all_jobs:
                        job_detail = get_job_details(ip_address, local_bearer_token, job['id'])
                        job_details = json.loads(job_detail)
                        if(job_name == job_details['data']['jobname']):
                            print("The job id of the job " + job_name + " is " + job['id'])
                            if(action is not None):
                                if(action == "cancel"):
                                    cancel_job(ip_address, local_bearer_token, job['id'])
                                elif(action == "delete"):
                                    delete_job(ip_address, local_bearer_token, job['id'])
                                else:
                                    print("Action not defined for " + action)
                                    
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

def get_all_update_jobs(omivv_ip, bearer_token):
    """ Get the update job details"""
    url = "https://" + omivv_ip + "/Spectre/api/rest/v1//Services/UpdateService/Jobs"
    head = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.get(url, verify=False, headers=head)
    if (response.status_code == 200):
        json_response = json.dumps(response.json(), indent=4, sort_keys=True)
        print(json_response)
        return json_response
    else:
        print("Get all update jobs failed.")

def cancel_job(omivv_ip, bearer_token, job_id):
    """ Cancel Jobs based on Id"""
    url = "https://" + omivv_ip + "/Spectre/api/rest/v1//Services/UpdateService/Jobs/" + job_id + "/Cancel"
    head = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.put(url, data={}, verify=False, headers=head)
    if (response.status_code == 200):
        print("Cancel job request success for id: " + job_id)
        print(response)
    else:
        print("Cancel job request failed for id: " + job_id)

def delete_job(omivv_ip, bearer_token, job_id):
    """ Delete Jobs based on Id"""
    url = "https://" + omivv_ip + "/Spectre/api/rest/v1/Services/UpdateService/Jobs/" + job_id
    head = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.delete(url, verify=False, headers=head, json=None)
    if (response.status_code == 200):
        print("Delete job request Success for id: " + job_id)
        return 
    else:
        print("Delete job request failed for id: " + job_id)

def get_job_details(omivv_ip, bearer_token, job_id):
    """ Get the update job details"""
    url = "https://" + omivv_ip + "/Spectre/api/rest/v1//Services/UpdateService/Jobs/" + job_id
    head = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.get(url, verify=False, headers=head)
    if (response.status_code == 200):
        json_response = json.dumps(response.json(), indent=4, sort_keys=True)
        return json_response
    else:
        print("Get all update jobs failed.")
    
def set_operational_context(omivv_ip, vcenter_id, session_token, vcenter_username, vcenter_domain, vcenter_password):
    base_url = "https://" + omivv_ip + "/Spectre/api/rest/v1/Services/ConsoleService/OperationalContext"
    postBodyData = {"consoleId": vcenter_id,
                    "consoleUserCredential": {"username": vcenter_username, "domain": vcenter_domain,
                                              "password": vcenter_password}}
    head = {'Authorization': 'Bearer ' + session_token}
    jsonReponse = requests.post(base_url, json=postBodyData, verify=False, headers=head)
    if (jsonReponse.status_code != 204):
        print("setOperationalContext failed.")

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
    
    
    PARSER.add_argument("--action", "-action", required=True,
                        help="want to delete or update the job. [delete] or [update] the job.")
    PARSER.add_argument("--jobName", "-jn", required=True,
                        help="name of the job")
    
    
    ARGS = PARSER.parse_args()
    if(ARGS.password == None and ARGS.bearertoken == None):
        print("Pass either the password or the bearer token")
    
    get_vcenter_tree(ARGS.ip, ARGS.user, ARGS.password, ARGS.bearertoken, ARGS.vcenterip,  ARGS.vcusername, ARGS.vcdomain, ARGS.vcpassword, ARGS.action, ARGS.jobName)
