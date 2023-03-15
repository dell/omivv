#
# autoUpgradeOMEALicense: Python script to Auto upgrade OME advanced+ license to servers marked as unsupported in OMEVVP
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
Description: autoUpgradeOMEALicense. Python script to Auto upgrade OME advanced+ license to servers with OMEVVP:Compliance>status:UNSUPPORTED and idracLicenseStatus": "UNSUPPORTED"

script_examples:

1. this example will import iDRAC OMEA license for the list of servers mentioned in csv having OMEVVP Compliance>status:UNSUPPORTED and idracLicenseStatus": "UNSUPPORTED"
    python autoUpgradeOMEALicense.py -csvfilepath C:\\Users\\Administrator\\Desktop\\autoupgradeOMEALicense.csv -retry 2

2. To view the help menu for list of args to be passed:
    python autoUpgradeOMEALicense.py -h

3. Refer InputSampleFiles>autoUpgradeOMEALicenseSample.csv for the sample csv file
'''


import requests,argparse,sys
import pandas as pd

from omevv_apis_client.models import Credential
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from getManagementHostComplianceData import HostManagementComplianceWrapper
from LicenseImport import LicenseImport
import warnings


warnings.filterwarnings("ignore")


class AutoUpgradeOMEALicense:
    def __init__(self):
        self.failuremsgdict = {"compliance_failure": [], "licenseimport_failure": [], "inputs_required": []}
        self.passlist = []


    def parse_csv(self, filepath):
        try:
            df = pd.read_csv(filepath)

            # To check if the mandatory fields are filled-in
            self.skipdf = df[["servicetag","ome_ip", "vc_uname", "vc_pwd", "vc_uuid", "idrac_ip", "licensefilename", "shareip", "sharetype","sharename"]].isna().any(axis=1)

            self.failuremsgdict["inputs_required"]=self.failuremsgdict["inputs_required"] + list(df[self.skipdf]["servicetag"].values)

            #Create newdf to include the rows which have the mandatory fields filled-in
            self.newdf = df[~self.skipdf]
            self.newdf.fillna('', inplace=True)
        except Exception as e:
            print("\n FAIL:Exception occured",e)


    # <---- Function to check host compliance --->
    def hostcompliance_check(self, ome_ip, vc_uname, vc_pwd, vc_uuid):
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ome_ip)
        credential = Credential(username=vc_uname, password=vc_pwd)
        hostmgmtcompliancehelper = HostManagementComplianceWrapper()

        hostmgmtcompliancehelper.create_payload(base_url=base_url, omeIp=ome_ip, vcUsercredential=credential,
                                                vCenterUUID=vc_uuid, compliance_filter="UNSUPPORTED")
        print(hostmgmtcompliancehelper)
        status, response = hostmgmtcompliancehelper.get_managed_hosts_compliance()
        return status, response

    # <---- Function for license workflow: create payload,import license,monitor job for completion --->
    def licenseimport(self, licensefilename, shareip, sharetype, shareuname, sharepwd, workgroup, ignorecertwarning,
                      sharename, retry, idrac_ip, idrac_uname="root", idrac_pwd="calvin"):
        flag = False
        licenseobj = LicenseImport()

        #Check for license import support
        flag,msg= licenseobj.check_supported_idrac_version(idrac_ip=idrac_ip,idrac_username=idrac_uname,idrac_password=idrac_pwd,retry=retry)
        if flag:
            payload = licenseobj.create_payload(licensename=licensefilename, shareip=shareip,
                                                sharetype=sharetype,
                                                shareuname=shareuname, sharepwd=sharepwd,
                                                workgroup=workgroup,
                                                ignorecertwarning=ignorecertwarning, sharename=sharename,
                                                retry=retry)

            job_id = licenseobj.import_idrac_license_network_share(idrac_ip=idrac_ip, idrac_uname=idrac_uname,
                                                                   idrac_pwd=idrac_pwd, payload=payload,
                                                                   retry=retry)

            if job_id:
                # call job func only if Job id is returned
                flag = licenseobj.check_job_status(job_id, retry=retry)
        else:
            print(msg)

        return flag


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Python script using OMEVV API to Auto upgrade OME advanced+ license to servers with OMEVVP Compliance>status:UNSUPPORTED and idracLicenseStatus: UNSUPPORTED",add_help=False)
        parser.add_argument('-csvfilepath', help='Filepath to the csv file', required=True, default=None)
        parser.add_argument('-retry',
                            help='Pass in the number of times the command needs to be re-tried in case of exception. The default value is retry=3',
                            required=False, type=int,default=3)

        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,help='Create a csv with the cooresponding values filled-in '
        'for the following column names - servicetag|ome_ip|vc_uname|vc_pwd|vc_uuid|idrac_ip|idrac_uname|idrac_pwd|licensefilename|shareip|sharetype|sharename|shareuname|sharepwd|workgroup|ignorecertwarning'
        'Refer InputSampleFiles>autoUpgradeOMEALicenseSample.csv for the sample csv file')

        args = vars(parser.parse_args())
        print(args)

        autoupgradelicenseobj = AutoUpgradeOMEALicense()

        autoupgradelicenseobj.parse_csv(filepath=args["csvfilepath"])

        for index, row in autoupgradelicenseobj.newdf.iterrows():


            print(f"\n<------------ Executing for the service tag: {row['servicetag']}-------------------->")
            # <---- Get the host compliance --->
            status, response = autoupgradelicenseobj.hostcompliance_check(ome_ip=row["ome_ip"], vc_uuid=row["vc_uuid"],
                                                                          vc_uname=row["vc_uname"], vc_pwd=row["vc_pwd"])


            if status:
                print("\n -Success: The Host Compliance Check is executed successfully and corresponding response obtained")
                # for each entry: if idracLicenseStatus:UNSUPPORTED- create list of service tags
                service_taglist = [dict1.get("serviceTag") for dict1 in response if
                                   dict1.get("idracLicenseStatus") == "UNSUPPORTED"]
                if row["servicetag"] in service_taglist:
                    flag = autoupgradelicenseobj.licenseimport(licensefilename=row["licensefilename"],
                                                               shareip=row["shareip"], sharetype=row["sharetype"],
                                                               shareuname=row["shareuname"], sharepwd=row["sharepwd"],
                                                               workgroup=row["workgroup"],
                                                               ignorecertwarning=row["ignorecertwarning"],
                                                               sharename=row["sharename"], retry=args["retry"],
                                                               idrac_ip=row["idrac_ip"], idrac_uname=row["idrac_uname"],
                                                               idrac_pwd=row["idrac_pwd"])

                    if flag:
                        autoupgradelicenseobj.passlist.append(row["servicetag"])
                    else:
                        print(f"\n FAIL:License import for the Service Tag - {row['servicetag']} failed")
                        autoupgradelicenseobj.failuremsgdict["licenseimport_failure"].append(row["servicetag"])
                else:
                    msg = f"\n Skipping the host with Service Tag - {row['servicetag']} as the corresponding required details are not available/incorrect in csv." \
                          f"Execute command -h for details on required info to be added to the csv." \
                          f"Also check that the OMEVV Host Compliance status:UNSUPPORTED & idracLicenseStatus :UNSUPPORTED"
                    print(msg)
                    autoupgradelicenseobj.failuremsgdict["inputs_required"].append(row["servicetag"])


            else:
                # For following set of OME IPs compliance failed
                if not (status):
                    print(f"\n Skipping the license import for the host with Service Tag - {row['servicetag']} as the Host compliance check failed {response}")

                    autoupgradelicenseobj.failuremsgdict["compliance_failure"].append(row["ome_ip"])

            print('*' * 100)

        print('*' * 40 + " Consolidated Results " + '*' * 40)
        print("\n\n FAIL:For the following list of service tags: the OMEA LicenseImport failed as the required idrac/OME/VC/license details are not available in the csv provided.Refer help(-h) option for details on required info to be added to the csv")
        print(autoupgradelicenseobj.failuremsgdict["inputs_required"])

        print('*' * 100)
        print("\n\n FAIL:For the following list of service tags - the Host compliance check failed.Kindly check the execution log for more info")
        print(autoupgradelicenseobj.failuremsgdict["compliance_failure"])
        print('*' * 100)

        print("\n\n FAIL:For the following list of service tags -  the OMEA LicenseImport failed.Kindly check the execution log for more info")
        print(autoupgradelicenseobj.failuremsgdict["licenseimport_failure"])
        print('*' * 100)

        print(
            "\n\n PASS:For the following list of service tags - the upgrade to OME Advanced+ is successful.Kindly check the execution log for more info")
        print(autoupgradelicenseobj.passlist)
        print('*' * 100)

    except Exception as e:
        print("FAIL: Exception occured",e)
        sys.exit()



    
