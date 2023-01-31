#
# LicenseImport. Python script using Redfish API with OEM extension to perform import of iDRAC OMEA license(s).
#
# _author_ = Ramya.R <Ramya.R@Dell.com>
# _version_ = 1.0
#
# Copyright (c) 2023 Dell EMC Corporation
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

'''
Description: LicenseImport. Python script using Redfish API with OEM extension to perform import of iDRAC OME Advanced+ license(s) to a single node.
script_examples:

1. this example will import iDRAC OMEA license from NFS share
    python LicenseImport.py -ip 192.168.0.120 -u root -p calvin -ipaddress 192.168.0.130 -sharetype NFS -sharename /nfs -username <share username> -password <share password> -licensefilename iDRAC_OMEA_license.xml -retry 2

2. To view the help menu for list of args to be passed:
    python LicenseImport.py -h

'''

import requests, json, sys, re, time, os, warnings, argparse

from datetime import datetime

warnings.filterwarnings("ignore")
import base64


class LicenseImport:
    def __init__(self):

        self.headers = {'content-type': 'application/json'}

        self.job_id = ""
        self.licenseimporturl = "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ImportLicenseFromNetworkShare"

        self.payload = {}

    def create_payload(self, licensename, shareip, sharetype, sharename, shareuname=None, sharepwd=None, workgroup=None,
                       ignorecertwarning=False,retry=3):
        self.retry=retry
        self.payload = {"FQDD": "iDRAC.Embedded.1", "ImportOptions": "Force", "UserName": shareuname,
                        "ShareType": sharetype,
                        "ShareName": sharename, "Password": sharepwd, "IPAddress": shareip, "LicenseName": licensename,
                        "Workgroup": workgroup, "IgnoreCertWarning": ignorecertwarning,
                        }
        self.payload = {k: v for k, v in self.payload.items() if v}

        print("\n Payload is: {}".format(self.payload))
        return self.payload

    def check_job_status(self, job_id, retry=3):
        flag = False
        self.retry = retry
        start_time = datetime.now()
        try:
            while True:
                req = requests.get(self.config_url + job_id,
                                   headers=self.headers, verify=False)
                current_time = (datetime.now() - start_time)
                statusCode = req.status_code
                print("Statuscode", statusCode)
                data = req.json()
                if statusCode == 200:
                    pass
                else:
                    print("\n- FAIL, Command failed to check job status, return code is %s" % statusCode)
                    print("Extended Info Message: {0}".format(req.json()))
                    return flag
                print(req.text)

                if str(current_time)[0:7] >= "0:05:00":
                    print("\n- FAIL: Timeout of 5 minutes has been hit, script stopped\n")
                    return flag
                elif "Fail" in data[u'Message'] or "fail" in data[u'Message'] or data[u'JobState'] == "Failed":
                    print("\n- FAIL: job ID %s failed, failed message is: %s" % (job_id, data[u'Message']))
                    return flag
                elif data[u'JobState'] == "Completed":
                    if data[u'Message'] == "The command was successful":
                        print("\n--- PASS, Final Detailed Job Status Results ---\n")
                        flag = True
                    else:
                        print("\n--- FAIL, Final Detailed Job Status Results ---\n")
                    for i in data.items():
                        if "odata" in i[0] or "MessageArgs" in i[0] or "TargetSettingsURI" in i[0]:
                            pass
                        else:
                            print("%s: %s" % (i[0], i[1]))
                    break
                else:
                    print("- WARNING, JobStatus not completed, current job status execution time is: \"%s\"" % (
                        str(current_time)[0:7]))
        except Exception as e:
            print("\n- FAIL: Exception occured- %s " % e)
            if retry > 0:
                retry = retry - 1
                time.sleep(5)
                self.check_job_status(job_id=self.job_id, retry=retry)

        return flag

    def import_idrac_license_network_share(self,idrac_ip, idrac_uname, idrac_pwd,payload, retry=3):

        self.idrac_ip = idrac_ip
        self.idrac_uname = idrac_uname
        self.idrac_pwd = idrac_pwd
        self.config_url = "https://" + self.idrac_ip

        try:
            credential = idrac_uname + ":" + idrac_pwd
            self.encoded_idrac_cred = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
            self.headers["Authorization"] = self.encoded_idrac_cred

            method = "ImportLicenseFromNetworkShare"

            print("- Performing POST on %s " % (self.config_url + self.licenseimporturl))
            response = requests.post(self.config_url + self.licenseimporturl, data=json.dumps(payload),
                                     headers=self.headers,
                                     verify=False)
            data = response.json()
            status_code = response.status_code
            if response.status_code == 202:
                print("\n- PASS: POST command passed for %s method, status code %s returned\n" % (
                    method, response.status_code))
            # 500 series status codes
            elif response.status_code >= 500:
                print("\n- FAIL:POST command failed for %s method, status code %s.Retry after sometime\n" % (
                    method, status_code))
                print("\n- POST command failure results:\n %s" % data)

            # 400 series status codes
            else:
                print("\n- FAIL: POST command failed for %s method, status code %s\n" % (method, status_code))
                print("\n- POST command failure results:\n %s" % data)

            self.job_id = response.headers.get('Location')
            if not (self.job_id):
                print(
                    "- FAIL, unable to find job ID in headers POST response, headers output is:\n%s" % response.headers)
                return ""
            print("- PASS, job ID %s successfuly created for %s method\n" % (self.job_id, method))

        except Exception as e:
            print("\n- FAIL: Exception occured- %s " % e)
            if retry > 0:
                retry = retry - 1
                time.sleep(5)
                self.import_idrac_license_network_share(idrac_ip, idrac_uname, idrac_pwd,payload, retry)
            else:
                print("- FAIL: Exception %s occured even after retrying %s times" % (e, self.retry))
                return False

        return self.job_id


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script using Redfish API with OEM extension to import iDRAC OMEA license(s)")

    parser.add_argument('-ip', help='iDRAC IP address', required=True)
    parser.add_argument('-u', help='iDRAC username. If no username is passed-default username of root is applied',
                        required=False, default="root")
    parser.add_argument('-p', help='iDRAC password', required=True)
    parser.add_argument('-sharetype',
                        help='Pass in the share type of the network share to import iDRAC license,supported values:CIFS/NFS/HTTP/HTTPS',
                        required=True)
    parser.add_argument('-ipaddress', help='Pass in the IP address of the network share to import iDRAC license',
                        required=True)
    parser.add_argument('-sharename', help='Pass in the network share name for export / import iDRAC license',
                        required=True)
    parser.add_argument('-username', help='Pass in the network share username',
                        required=False)
    parser.add_argument('-password', help='Pass in the network share username password',
                        required=False)
    parser.add_argument('-workgroup',
                        help='Pass in the workgroup of your CIFS network share. This argument is optional',
                        required=False)
    parser.add_argument('-ignorecertwarning',
                        help='Supported values are On and Off. This argument is only required if using HTTPS for share type',
                        required=False)
    parser.add_argument('-licensefilename',
                        help='Pass in name of the license file on the network share you want to import',
                        required=True)
    parser.add_argument('-retry',
                        help='Pass in the number of times the command needs to be re-tried in case of exception. The default value is retry=3',
                        required=False, type=int)
    args = vars(parser.parse_args())

    licenseobj = LicenseImport()

    payload = licenseobj.create_payload(licensename=args["licensefilename"], shareip=args["ipaddress"],
                                        sharetype=args["sharetype"],
                                        shareuname=args["username"], sharepwd=args["password"],
                                        workgroup=args["workgroup"],
                                        ignorecertwarning=args["ignorecertwarning"], sharename=args["sharename"],retry=args["retry"])

    job_id = licenseobj.import_idrac_license_network_share(idrac_ip=args["ip"], idrac_uname=args["u"], idrac_pwd=args["p"],payload=payload, retry=args["retry"])

    if job_id:
        # call job func only if Job id is returned
        flag = licenseobj.check_job_status(job_id, retry=args["retry"])
        if not (flag):
            print("- FAIL: Job for license import is not successful")



