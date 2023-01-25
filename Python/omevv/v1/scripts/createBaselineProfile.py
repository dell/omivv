#
# Baseline profile:Creating a Baseline profile in OMEVVP
# Baseline Profile enables user to capture the baseline configuration for system configuration, firmware, or driver versions
# and maintain the desired state for clusters by identifying the drift against the baseline.
#
#
#
# _author_ = Ramya.R <Ramya.R@Dell.com>
# _version_ = 1.0
#
# Copyright (c) 2022, Dell, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#

'''
Description: BaselineProfile. Creating a Baseline profile in OMEVVP
# Baseline Profile enables user to capture the baseline configuration for system configuration, firmware, or driver versions and maintain the desired state for clusters by identifying the drift against the baseline.

script_examples:
1. this example will CreateBaselineProfile with job schedule for monday,tuesday at time 14:15
python createBaselineProfile.py -ip 192.168.0.120 -vcuser <vc username> -name <baseline profile name> -desc ExampleBaselineProfile -vcpass <vc password> -vcuuid <vcuuid> -frid <Firmware repoid> -gid <groupid> -jsd monday,tuesday -jst 14:15 -retry 4

2. this example will CreateBaselineProfile with default job schedule sunday at time 03:00
python createBaselineProfile.py -ip 192.168.0.120 -vcuser <vc username> -name <baseline profile name> -vcpass <vc password> -vcuuid <vcuuid> -frid <Firmware repoid> -gid <groupid>

3. To view the help menu for list of args to be passed:
    python createBaselineProfile.py -h

'''

import time, warnings
import base64
warnings.filterwarnings("ignore")
import argparse


from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.api.baseline_profile_management import create_baseline_profiles
from omevv_apis_client.models import BaselineProfileCreateRequest,DaysAndTimeOfWeek
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.types import Response,UNSET

import constants
from typing import Any, Dict, List, Optional, Union



class CreateBaselineProfile:
    def __init__(self):

        self.headers = {'content-type': 'application/json'}
        self.baseline_profileid = ""
        self.payload = {}


    #<--- Function to get user inputs--->
    def create_payload(self,name,description,firmware_repoid,driver_repoid,time,retry,configuration_repoid,createdby,jobschedule_days,group_idslist=[]):
        self.retry = retry

        self.payload = {
            "name": name,
            "description": description,
            "firmwareRepoId": firmware_repoid,
            "driverRepoId": driver_repoid,
            "configurationRepoId": configuration_repoid,
            "createdBy": createdby,
            "groupIds": group_idslist,
            "jobSchedule": {
                "monday": False,
                "tuesday": False,
                "wednesday": False,
                "thursday": False,
                "friday": False,
                "saturday": False,
                "sunday": False,
                "time": time
            }
        }
        print(jobschedule_days)
        #jobscheduledays
        if jobschedule_days:
            #When multiple days are mentioned
            if "," in jobschedule_days:
                split_string = jobschedule_days.split(",")
                for day in split_string:
                    if day in self.payload["jobSchedule"]:
                        self.payload["jobSchedule"][day]= True
                    else:
                        print("\n FAIL, either missing argument or incorrect argument used. Please check script help-text for jsd.")
                        print("\n Proceeding with default value for jobschedule-day")
            else:
                if (self.payload["jobSchedule"].get(jobschedule_days,None)) !=None:
                    self.payload["jobSchedule"][jobschedule_days]= True
                else:
                    print("\n INFO, incorrect argument value for jobschedule-day. Please check script help-text for jsd.")
                    print("\n Proceeding with default value for jobschedule-day")



        self.day_of_week_obj=DaysAndTimeOfWeek(monday=self.payload["jobSchedule"]["monday"],tuesday=self.payload["jobSchedule"]["tuesday"],wednesday=self.payload["jobSchedule"]["wednesday"],thursday=self.payload["jobSchedule"]["thursday"],friday=self.payload["jobSchedule"]["friday"],saturday=self.payload["jobSchedule"]["saturday"],sunday=self.payload["jobSchedule"]["sunday"],time=self.payload["jobSchedule"]["time"])

        self.create_baseline_payload_obj = BaselineProfileCreateRequest(name=name,description=description,firmware_repo_id=firmware_repoid,driver_repo_id=driver_repoid,configuration_repo_id=configuration_repoid,created_by=createdby,group_ids=group_idslist,job_schedule=self.day_of_week_obj)
        print("\n payload attributes - ", self.create_baseline_payload_obj)




    #<--- Function to  create_baselineprofile--->
    def create_baselineprofile(self,payload,vc_username,vc_pwd,omevv_ip,vc_uuid,retry):

        self.vc_username=vc_username
        self.vc_pwd=vc_pwd
        self.omevv_ip=omevv_ip
        self.vc_uuid=vc_uuid


        try:
            credential = self.vc_username + ":" + self.vc_pwd
            self.encoded_vc_cred = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
            self.headers["Authorization"] = self.encoded_vc_cred
            self.headers.update({constants.vcGuidHeader: vc_uuid})



            self.base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=self.omevv_ip)
            self.client = AuthenticatedClient(base_url=self.base_url, token=None, verify_ssl=False). \
                with_headers(headers=self.headers) . \
                with_timeout(constants.generalTimeOut_sec)

            method = "CreateBaselineProfile"
            response: Response[Union[ErrorObject, int]] = create_baseline_profiles.sync_detailed(client=self.client,json_body=self.create_baseline_payload_obj,uuid=self.vc_uuid)
            print("\n Response - ",response)


            data = response.parsed
            status_code = response.status_code
            if response.status_code == 200:
                print("\n- PASS: POST command passed for %s method, status code %s returned\n" % (
                method, response.status_code))
            # 500 series status codes
            elif response.status_code >= 500:
                print("\n- FAIL:POST command failed for %s method, status code %s.Retry after sometime\n" % (
                method, status_code))
                print("\n- POST command failure results:\n %s" % data)
                return self.baseline_profileid
            # 400 series status codes
            else:
                print("\n- FAIL: POST command failed for %s method, status code %s\n" % (method, status_code))
                print("\n- POST command failure results:\n %s" % data)
                return self.baseline_profileid

            self.baseline_profileid = data
            if not (self.baseline_profileid):
                print("- FAIL, unable to find baselineprofile ID in POST response, response output is:\n%s" % data)
                return ""

            print("- PASS, Baseline ProfileID %s is successfully created for %s method\n" % (self.baseline_profileid, method))


        except Exception as e:

            print("\n- FAIL: Exception %s occured" % e)
            if retry > 0:
                retry = retry - 1
                time.sleep(5)
                self.create_baselineprofile(self.payload,self.vc_username,self.vc_pwd,self.omevv_ip,self.vc_uuid,retry=retry)
            else:
                print("- FAIL: Exception %s occured even after retrying %s times" % (e, self.retry))
                return ""

        return self.baseline_profileid



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script using OMEVV API to create baseline profile for system configuration, firmware, or driver versions")
    parser.add_argument('-ip', help='OMEVV IP address', required=True, default=None)
    parser.add_argument("-vcuser", required=True, help="username of vcenter", default=None)
    parser.add_argument("-vcpass", required=True, help="password of vcenter", default=None)
    parser.add_argument("-vcuuid", required=True, help="UUID of the relevant vCenter", default=None)

    parser.add_argument('-name', help="Name of the baseline profile.", required=True,default=None)
    parser.add_argument('-desc', help="Description for the baseline profile.", required=False,default=None)

    parser.add_argument('-frid', help="Firmware repository ID <integer> to associate the baseline profile",
                        required=True,default=None)
    parser.add_argument('-drid', help="driver repository ID <integer> to associate the baseline profile",
                        required=False,default=None)
    parser.add_argument('-crid', help="configurationRepoId <integer> to associate the baseline profile",
                        required=False,default=None)

    parser.add_argument('-cb', help="Created user, if not provided it is OMEVV by default", required=False,default=None)

    parser.add_argument('-gid', help="Pass in the groupId's e.g 1111", required=True,nargs='+')

    parser.add_argument("-jsd", help="job schedule - Enable days of the week for baseline profile job schedule."
                                      "Supported values are: monday,tuesday,wednesday,thursday,friday,saturday,sunday"
                                       "If you pass in multiple string values, make sure to use comma separator Default:sunday",
                        required=False,default="sunday")

    parser.add_argument("-jst", required=False,
                        help="Specify time for baseline profile job schedule-in 24 HR format: HH:SS. default value - 03:00",default="03:00")

    parser.add_argument('-retry',
                        help='Pass in the number of times the command needs to be re-tried in case of exception,default value is 2',
                        required=False,default=2)

    args = vars(parser.parse_args())
    print(args)

    baseline_obj=CreateBaselineProfile()
    payload=baseline_obj.create_payload(name=args["name"],description=args["desc"],firmware_repoid=args["frid"],driver_repoid=args["drid"],
                                                configuration_repoid=args["crid"],createdby=args["cb"],group_idslist=args["gid"],
                                                jobschedule_days=args["jsd"],time=args["jst"],retry=args["retry"])


    baselineprofile_id=baseline_obj.create_baselineprofile(payload=payload,vc_username=args["vcuser"],vc_pwd=args["vcpass"],
                                                                 omevv_ip=args["ip"],vc_uuid=args["vcuuid"],retry=args["retry"])

    if not(baselineprofile_id):
        print("- FAIL:The Creation of Baseline Profile is not successful")




