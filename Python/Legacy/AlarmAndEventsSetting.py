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
   Script to set the alarms setting and enabling and disabling the MPR in OMIVV

DESCRIPTION:
   This script exercises the Spectre REST API to set the alarms setting and 
   enabling and disabling the MPR in OMIVV. For authentication X-Auth is 
   used over Basic Authentication
   Note that the credentials entered are not stored to disk.

EXAMPLE:
   python AlarmAndEventsSetting.py  --ip <xx>  --user <username> --password <pwd> --vcenterip <vcenterIP>
        --vcusername <vcUsername> --vcdomain <vcDomain> --vcpassword <vcpwd> 
"""
import sys
import argparse
from argparse import RawTextHelpFormatter
import json
import requests
import urllib3
import traceback


def get_or_set_alarms(ip_address, user_name, password, bearer_token, vcenter_ip,  vc_username, vc_domain, vc_password, get_action, enable_alarm, enable_mpr, set_alarm_options):
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

            if(enable_alarm != None):
                set_alarm_setting(ip_address, local_bearer_token, enable_alarm, enable_mpr, set_alarm_options)
                return
            
            if(get_action != None):
                alarms_setting = get_alarm_setting(ip_address, local_bearer_token)
                print(alarms_setting)
            
            
            
        """ Log out from OMIVV """
        if(bearer_token == None):
            logout(ip_address, local_bearer_token)
    except:
        traceback.print_exc()
        print("get_or_set_alarms: Unexpected error:", sys.exc_info()[0])


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

def set_operational_context(omivv_ip, vcenter_id, session_token, vcenter_username, vcenter_domain, vcenter_password):
    base_url = "https://" + omivv_ip + "/Spectre/api/rest/v1/Services/ConsoleService/OperationalContext"
    postBodyData = {"consoleId": vcenter_id,
                    "consoleUserCredential": {"username": vcenter_username, "domain": vcenter_domain,
                                              "password": vcenter_password}}
    head = {'Authorization': 'Bearer ' + session_token}
    jsonReponse = requests.post(base_url, json=postBodyData, verify=False, headers=head)
    if (jsonReponse.status_code != 204):
        print("setOperationalContext failed.")

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

def get_alarm_setting(omivvIP,bearerToken):
    """Get alarm setting from OMIVV"""
    url ="https://" + omivvIP + "/Spectre/api/rest/v1/Services/ConsoleService/AlarmsAndEvents"
    head = {'Authorization': 'Bearer ' + bearerToken}
    response = requests.get(url, verify=False, headers=head)
    if(response.status_code == 200):
        json_response = json.dumps(response.json(), indent=4, sort_keys=True)
        return json_response
    else:
        print("Get alarm setting from the OMIVV failed")
        

def set_alarm_setting(omivvIP,bearerToken,enable_alarm, enable_mpr, set_alarm_options):
    """Set alarm setting from OMIVV"""
    url ="https://" + omivvIP + "/Spectre/api/rest/v1/Services/ConsoleService/AlarmsAndEvents"
    head = {'Authorization': 'Bearer ' + bearerToken}
    e_alarm = False
    if(enable_alarm == "True"):
        e_alarm = True
    
    e_mpr = False
    if(enable_mpr == "True"):
        e_mpr = True
    attr_payload = {"alarmStatus": e_alarm, "mprAlarmStatus" : e_mpr, "eventPostType": set_alarm_options }
    response = requests.put(url, json=attr_payload, verify=False, headers=head)
    if(response.status_code == 200):
        print("Set alarm is successful.")
    else:
        print(response)
        print("Set alarm status is failed")

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
    
    
    PARSER.add_argument("--getAlarmSetting", "-getAlarm", required=False,default="True",
                        help="Get alarm settings from OMIVV")
    PARSER.add_argument("--setAlarmOptions", "-setAlarm", required=False,
                        help="Set alarm setting. Possible value: NO_EVENTS, ALL_EVENTS, CRITICAL_AND_WARNING_EVENTS, VIRTUALIZATION_EVENTS")
    PARSER.add_argument("--enableAlarm", "-enableAlarm", required=False, default=None,
                        help="Set alarm setting. Possible value: True, False")
    PARSER.add_argument("--enableMPR", "-enableMPR", required=False, default=False,
                        help="Set alarm setting. Possible value: True, False")
    
    
    ARGS = PARSER.parse_args()
    if(ARGS.password == None and ARGS.bearertoken == None):
        print("Pass either the password or the bearer token")
    get_or_set_alarms(ARGS.ip, ARGS.user, ARGS.password, ARGS.bearertoken, ARGS.vcenterip,  ARGS.vcusername, ARGS.vcdomain, ARGS.vcpassword, ARGS.getAlarmSetting, ARGS.enableAlarm, ARGS.enableMPR, ARGS.setAlarmOptions)
