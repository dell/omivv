#
#  Python script using OMIVV API to get cluster id by cluster name.
#
# _author_ = Prakash Ranjan <Prakash_Ranjan@Dell.com>
# _version_ = 0.1
#
# Copyright (c) 2020 Dell EMC Corporation
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
   Script to get Python script using OMIVV API to get cluster id by cluster name.

DESCRIPTION:
   This script exercises the Spectre REST API to get a Vcenter datacenters,
   clusters and host. For authentication X-Auth is used over Basic
   Authentication
   Note that the credentials entered are not stored to disk.

EXAMPLE:
   python get_cluster_id_by_cluster_name.py --ip <xx> --user <username> --password <pwd> --vcenterip <vcenterIP>
   --serviceTag <host_service_tag>
"""
import sys
import argparse
from argparse import RawTextHelpFormatter
import json
import requests
import urllib3

def get_vcenter_tree(ip_address, user_name, password, vcenter_ip, cluster_name):
    """Authenticate with OMIVV and enumerate reports."""

    try:
        bearer_token = get_bearer_token(ip_address, user_name, password)
        """ Get all registered vcenter """
        registered_vcenter_list =  get_registered_vcenter_list(ip_address, bearer_token)
        if(registered_vcenter_list is None):
            print("No vcenter is regsitered with this OMIVV")
            return
        else:
            vcenter_id = None;
            registered_vc_array = json.loads(registered_vcenter_list)
            for vc in registered_vc_array:
                if vcenter_ip.upper() == vc['ip'].upper():
                    vcenter_id = vc['id']

            vcenter_tree_response = get_vcenter_tree_from_omivv(ip_address,vcenter_id, bearer_token)
            found = False
            if vcenter_tree_response is not None:
                vcenter_datacenters = json.loads(vcenter_tree_response)
                vcenter_datacenters_List = vcenter_datacenters['datacenters']
                for vcenter_datacenter in vcenter_datacenters_List:
                    cluster_list = vcenter_datacenter["clusters"]
                    if cluster_list is not None:
                            for cluster in cluster_list:
                                if cluster['name'] == cluster_name:
                                    print("Cluster name: " + cluster_name + ",  Cluster id: " + cluster['id'])
                                    found = True
                                    break

                    if found:
                        break

            if found == False:
                print("Cluster " + cluster_name + " not found.")


        """ Log out from OMIVV """
        logout(ip_address, bearer_token)
    except:
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
        return json_response;
    else:
        print("Get registered vCenter list failed")

def get_vcenter_tree_from_omivv(OMIVV_ip, vcenter_id, session_token):
    url = "https://" + OMIVV_ip + "/Spectre/api/rest/v1/Services/ConsoleService/Consoles/" + vcenter_id
    head = {'Authorization': 'Bearer ' + session_token}
    response = requests.get(url, verify=False, headers=head)
    if (response.status_code == 200):
        json_response = json.dumps(response.json(), indent=4, sort_keys=True)
        return json_response
    else:
        print("Get registered vCenter list failed")


if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OMIVV Appliance IP")
    PARSER.add_argument("--user", "-u", required=False,
                        help="Username for OMIVV Appliance", default="admin")
    PARSER.add_argument("--password", "-p", required=True,
                        help="Password for OMIVV Appliance")
    PARSER.add_argument("--vcenterip", "-vcip", required=True,
                        help="IP for vcenter")
    PARSER.add_argument("--clustername", "-clustername", required=True,
                        help="cluster name")
    ARGS = PARSER.parse_args()
    get_vcenter_tree(ARGS.ip, ARGS.user, ARGS.password,ARGS.vcenterip, ARGS.clustername)
