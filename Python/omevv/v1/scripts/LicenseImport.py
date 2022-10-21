#
# LicenseImport. Python script using Redfish API with OEM extension to perform import of iDRAC OMEA license(s).
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
Description: LicenseImport. Python script using Redfish API with OEM extension to perform import of iDRAC OME Advanced+ license(s) to a single node.
script_examples:

1. this example will import iDRAC OMEA license from NFS share
    python LicenseImport.py -ip 192.168.0.120 -u root -p calvin -ipaddress 192.168.0.130 -sharetype NFS -sharename /nfs -username <share username> -password <share password> -licensefilename iDRAC_OMEA_license.xml --retry 2')

'''

import requests, json, sys, re, time, os, warnings, argparse

from datetime import datetime

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(
    description="Python script using Redfish API with OEM extension to import iDRAC OMEA license(s)")
parser.add_argument('-ip', help='iDRAC IP address', required=True)
parser.add_argument('-u', help='iDRAC username', required=True)
parser.add_argument('-p', help='iDRAC password', required=True)
parser.add_argument('-sharetype',
                    help='Pass in the share type of the network share to import iDRAC license,supported values:CIFS/NFS/HTTP/HTTPS',
                    required=True)
parser.add_argument('-ipaddress', help='Pass in the IP address of the network share to import iDRAC license',
                    required=True)
parser.add_argument('-sharename', help='Pass in the network share name for export / import iDRAC license',
                    required=True)
parser.add_argument('-username', help='Pass in the network share username',
                    required=True)
parser.add_argument('-password', help='Pass in the network share username password',
                    required=True)
parser.add_argument('--workgroup', help='Pass in the workgroup of your CIFS network share. This argument is optional',
                    required=False)
parser.add_argument('--ignorecertwarning',
                    help='Supported values are On and Off. This argument is only required if using HTTPS for share type',
                    required=False)
parser.add_argument('-licensefilename', help='Pass in name of the license file on the network share you want to import',
                    required=True)
parser.add_argument('--retry',
                    help='Pass in the number of times the command needs to be re-tried in case of exception,default value is 2',
                    required=False)
args = vars(parser.parse_args())

idrac_ip = args["ip"]
idrac_username = args["u"]
idrac_password = args["p"]
job_id = ""
licenseimporturl = ""
retry = 2
payload = {"FQDD": "iDRAC.Embedded.1", "ImportOptions": "Force"}


def get_userinput():
    global retry
    if args["licensefilename"]:
        payload["LicenseName"] = args["licensefilename"]
    if args["ipaddress"]:
        payload["IPAddress"] = args["ipaddress"]
    if args["sharetype"]:
        payload["ShareType"] = args["sharetype"]
    if args["sharename"]:
        payload["ShareName"] = args["sharename"]
    if args["username"]:
        payload["UserName"] = args["username"]
    if args["password"]:
        payload["Password"] = args["password"]
    if args["workgroup"]:
        payload["Workgroup"] = args["workgroup"]
    if args["ignorecertwarning"]:
        payload["IgnoreCertificateWarning"] = args["ignorecertwarning"]
    if args["retry"]:
        retry = args["retry"]

    print("\n- WARNING, arguments and values for License Import method\n")
    for i in payload.items():
        if i[0] == "ShareParameters":
            for ii in i[1].items():
                if ii[0] == "Password":
                    print("Password: **********")
                else:
                    print("%s: %s" % (ii[0], ii[1]))
        else:
            print("%s: %s" % (i[0], i[1]))


def import_idrac_license_network_share():
    global retry, job_id
    try:
        headers = {'content-type': 'application/json'}
        method = "ImportLicenseFromNetworkShare"
        url = 'https://%s/redfish/v1/Dell/Managers/iDRAC.Embedded.1/DellLicenseManagementService/Actions/DellLicenseManagementService.ImportLicenseFromNetworkShare' % (
            idrac_ip)

        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False,
                                 auth=(idrac_username, idrac_password))
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
            sys.exit()
        # 400 series status codes
        else:
            print("\n- FAIL: POST command failed for %s method, status code %s\n" % (method, status_code))
            print("\n- POST command failure results:\n %s" % data)
            sys.exit()

        job_id = response.headers.get('Location')
        if not (job_id):
            print("- FAIL, unable to find job ID in headers POST response, headers output is:\n%s" % response.headers)
            sys.exit()
        print("- PASS, job ID %s successfuly created for %s method\n" % (job_id, method))

    except Exception as e:
        print("\n- FAIL: Exception %s occured" % e)
        if retry > 0:
            retry = retry - 1
            time.sleep(5)
            import_idrac_license_network_share()
        else:
            print("- FAIL: Exception %s occured even after retrying %s times" % (e, retry))
            sys.exit()


def loop_job_status():
    start_time = datetime.now()
    time.sleep(1)
    while True:
        req = requests.get('https://%s%s' % (idrac_ip, job_id),
                           auth=(idrac_username, idrac_password), verify=False)
        current_time = (datetime.now() - start_time)
        statusCode = req.status_code
        print("Statuscode", statusCode)
        data = req.json()
        if statusCode == 200:
            pass
        else:
            print("\n- FAIL, Command failed to check job status, return code is %s" % statusCode)
            print("Extended Info Message: {0}".format(req.json()))
            sys.exit()
        print(req.text)

        if str(current_time)[0:7] >= "0:05:00":
            print("\n- FAIL: Timeout of 5 minutes has been hit, script stopped\n")
            sys.exit()
        elif "Fail" in data[u'Message'] or "fail" in data[u'Message'] or data[u'JobState'] == "Failed":
            print("\n- FAIL: job ID %s failed, failed message is: %s" % (job_id, data[u'Message']))
            sys.exit()
        elif data[u'JobState'] == "Completed":
            if data[u'Message'] == "The command was successful":
                print("\n--- PASS, Final Detailed Job Status Results ---\n")
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


if __name__ == "__main__":

    get_userinput()
    import_idrac_license_network_share()

    if job_id:
        # call job func only if Job id is returned
        loop_job_status()




