import argparse
import warnings
from omevv_apis_client import AuthenticatedClient
import requests, json
from omevv_apis_client.models import Credential
import constants
import base64
from omevv_apis_client.types import Response
from omevv_apis_client.api.baseline_profile_management import edit_baseline_profile
from omevv_apis_client.models.baseline_profile_modify_request import BaselineProfileModifyRequest
from omevv_apis_client.models.days_and_time_of_week import DaysAndTimeOfWeek

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class ModifyDriftDetectionScheduleWrapper:
    def __init__(self):
        pass
        
    def create_payload(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, baseline_profile_id, description, modified_by, firmware_repo_id, driver_repo_id, configuration_repo_id, addgroup_ids, remove_group_ids, monday, tuesday, wednesday, thursday, friday, saturday, sunday, time):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {constants.vcGuidHeader: vCenterUUID}
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.baseline_profile_id = baseline_profile_id
        self.description = description
        self.modified_by = modified_by
        self.firmware_repo_id = firmware_repo_id        
        self.driver_repo_id = driver_repo_id
        self.configuration_repo_id = configuration_repo_id    
        self.addgroup_ids = addgroup_ids
        self.remove_group_ids = remove_group_ids
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.time = time
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)

        self.job_schedule = DaysAndTimeOfWeek(monday=self.monday, tuesday=self.tuesday, wednesday=self.wednesday, thursday=self.thursday, friday=self.friday, saturday=self.saturday, time=self.time, sunday=self.sunday) 
        self.json_body = BaselineProfileModifyRequest(description=self.description, modified_by=self.modified_by, firmware_repo_id=self.firmware_repo_id, driver_repo_id=self.driver_repo_id, configuration_repo_id=self.configuration_repo_id, addgroup_ids=self.addgroup_ids, remove_group_ids=self.remove_group_ids, job_schedule=self.job_schedule)

    def modify_drift_detection_schedule(self):        
        global retry
        try:
            response: Response[Union[Any, ErrorObject]] = \
                edit_baseline_profile.sync_detailed(uuid=self.uuid, cpid=self.baseline_profile_id, client=self.client, json_body=self.json_body)
            
            if str(response.parsed) == "None":
                return "Drift detection schedule modified successfully"
            else:
                return response.parsed

        except Exception as e:
            print("Exception occured while modifying drift detection schedule ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                self.modify_drift_detection_schedule();
            else:
                print("Failed after 3 retries,exiting");
                sys.exit();

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True, help="OME Appliance IP")
    PARSER.add_argument("--vcusername", "-u", required=True,
                        help="username of vcenter")
    PARSER.add_argument("--vcpassword", "-p", required=True,
                        help="password of vcenter")
    PARSER.add_argument("--vcUUID", "-d", required=True, default=None,
                        help="UUID of the relevant vCenter")
    PARSER.add_argument("--baseline_profile_id", "-b", required=True, default=None, help="baseline profile id of baseline profile for which drift detection schedule needs to be modified")
    PARSER.add_argument("--description", "-des", required=False, default=None, help="description of baseline profile")
    PARSER.add_argument("--modified_by", "-mod", required=False, default=None, help="modified by user name")
    PARSER.add_argument("--firmware_repo_id", "-fir", required=False, default=None, help="firmware repo id for baseline profile")
    PARSER.add_argument("--driver_repo_id", "-dri", required=False, default=None, help="driver repo id for baseline profile")
    PARSER.add_argument("--configuration_repo_id", "-conf", required=False, default=None, help="configuration repo id for baseline profile")
    PARSER.add_argument("--addgroup_ids", "-add", nargs = '+', required=False, default=None, help="add group ids for baseline profile")
    PARSER.add_argument("--remove_group_ids", "-rem", nargs = '+', required=False, default=None, help="remove group ids for baseline profile")   
    PARSER.add_argument("--monday", "-mon", required=False, default=None, help="indicate the boolean value for monday")
    PARSER.add_argument("--tuesday", "-tues", required=False, default=None, help="indicate the boolean value for tuesday")
    PARSER.add_argument("--wednesday", "-wednes", required=False, default=None, help="indicate the boolean value for wednesday")
    PARSER.add_argument("--thursday", "-thurs", required=False, default=None, help="indicate the boolean value for thursday")
    PARSER.add_argument("--friday", "-fri", required=False, default=None, help="indicate the boolean value for friday")
    PARSER.add_argument("--saturday", "-sat", required=False, default=None, help="indicate the boolean value for saturday")
    PARSER.add_argument("--sunday", "-sun", required=False, default=None, help="indicate the boolean value for sunday")
    PARSER.add_argument("--time", "-t", required=False, default=None, help="time")
 
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.baseline_profile_id is not None:
        if ARGS.description is None and ARGS.modified_by is None and ARGS.firmware_repo_id is None and ARGS.driver_repo_id is None and ARGS.configuration_repo_id is None and ARGS.addgroup_ids is None and ARGS.remove_group_ids is None and ARGS.monday is None and ARGS.tuesday is None and ARGS.wednesday is None and ARGS.thursday is None and ARGS.friday is None and ARGS.saturday is None and ARGS.sunday is None and ARGS.time is None:
            print("No job schedule argument given")
        else:           
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
            payload = {}
            driftdetectionhelper = ModifyDriftDetectionScheduleWrapper()
            driftdetectionhelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, baseline_profile_id=ARGS.baseline_profile_id, description=ARGS.description, modified_by=ARGS.modified_by, firmware_repo_id=ARGS.firmware_repo_id, driver_repo_id=ARGS.driver_repo_id, configuration_repo_id=ARGS.configuration_repo_id, addgroup_ids=ARGS.addgroup_ids, remove_group_ids=ARGS.remove_group_ids, monday=ARGS.monday, tuesday=ARGS.tuesday, wednesday=ARGS.wednesday, thursday=ARGS.thursday, friday=ARGS.friday, saturday=ARGS.saturday, sunday=ARGS.sunday, time=ARGS.time)
            print(driftdetectionhelper.modify_drift_detection_schedule())
    else:
        print("Required parameters missing. Please review module help.")