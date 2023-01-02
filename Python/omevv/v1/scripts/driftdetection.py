import argparse
import warnings
from omevv_apis_client import AuthenticatedClient
import requests, json
from omevv_apis_client.models import Credential
import constants
import base64
from omevv_apis_client.types import Response

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class ModifyDriftDetectionScheduleWrapper:
    def __init__(self):
        pass
        
    def create_payload(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, baseline_profile_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, time):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {constants.vcGuidHeader: vCenterUUID}
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.baseline_profile_id = baseline_profile_id
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

        self.payload["jobSchedule"] = {
            "monday": self.monday,
            "tuesday": self.tuesday,
            "wednesday": self.wednesday,
            "thursday": self.thursday,
            "friday": self.friday,
            "saturday": self.saturday,
            "sunday": self.sunday,
            "time": self.time
        }

    def modifyDriftDetectionSchedule(self):
        headers = self.headers
        url = 'https://%s/omevv/GatewayService/v1/Consoles/%s/BaselineProfiles/%s'%(self.omeIp, self.uuid, self.baseline_profile_id)
        try:
            response = requests.put(url, data=json.dumps(self.payload), headers=headers, verify=False);
            status_code = response.status_code
            if status_code == 200:
              return "Drift detection job schedule is updated successfully"
            elif status_code == 400 or status_code == 500 or status_code == 404:
                data = response.json()
                return "Error occured while modifying drift detection schedule : "+ str(data)
            else:
                data = response.json()
                raise Exception("Error occured while creating manage job ",data);
        except Exception as e:
            print(e);
 
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
        if ARGS.monday is None and ARGS.tuesday is None and ARGS.wednesday is None and ARGS.thursday is None and ARGS.friday is None and ARGS.saturday is None and ARGS.sunday is None and ARGS.time is None:
            print("No job schedule argument given")
        else:           
            base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
            credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
            payload = {}
            driftdetectionhelper = ModifyDriftDetectionScheduleWrapper()
            driftdetectionhelper.create_payload(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, baseline_profile_id=ARGS.baseline_profile_id, monday=ARGS.monday, tuesday=ARGS.tuesday, wednesday=ARGS.wednesday, thursday=ARGS.thursday, friday=ARGS.friday, saturday=ARGS.saturday, sunday=ARGS.sunday, time=ARGS.time)
            print(driftdetectionhelper.modifyDriftDetectionSchedule())
    else:
        print("Required parameters missing. Please review module help.")