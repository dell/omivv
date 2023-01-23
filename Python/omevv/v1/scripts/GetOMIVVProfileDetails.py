import argparse
import sys
import csv
import time
import warnings
from webbrowser import get
from omivv_models import consoleDecoder,repoProfileDecoder
from utilities import Utilities

import requests,json,base64

class RepoDetails:
    def __init__(self,omivv_ip,omivv_username,omivv_pwd,domain):
        self.omevv_username = omivv_username.strip()
        self.headers = {'content-type': 'application/json'}
        self.domain = domain
        self.omevv_password = omivv_pwd.strip()
        self.login_url = "https://%s/Spectre/api/rest/v1/Services/AuthenticationService/login"%(omevv_ip)
        self.console_url = "https://%s/Spectre/api/rest/v1/Services/ConsoleService/Consoles"%(omevv_ip)
        self.context_url = "https://%s/Spectre/api/rest/v1/Services/ConsoleService/OperationalContext"%(omevv_ip)
        self.repo_url = "https://%s/Spectre/api/rest/v1/Services/PluginProfileService/RepositoryProfiles"%(omevv_ip)
        self.omevv_encoded_cred = self.encode_cred(self.omivv_username, self.omivv_password)
        self.payload_cred_dict= {}
        self.payload_cred_dict['console'] = 'consoleUserCredential'
        self.payload_cred_dict['api'] = 'apiUserCredential'
        self.retry = 3


    def encode_cred(self,username, pwd):
        cred_str = username + ":" + pwd;
        cred_str_bytes = cred_str.encode("ascii");
        base64_bytes = base64.b64encode(cred_str_bytes);
        base64_string = base64_bytes.decode("ascii");
        return base64_string

    def create_payload(self,username,pwd,domain,type):
        payload = {}
        cred_json = {"username": username.strip(), "domain": domain.strip(), "password": pwd.strip()};
        payload[self.payload_cred_dict[type]] = cred_json
        return payload

    def create_context_payload(self,cid,console_username,console_domain,console_pwd):
        payload = {}
        payload['consoleId'] = cid
        cred_json = {"username": console_username.strip(), "domain": console_domain.strip(), "password": console_pwd.strip()};
        payload["consoleUserCredential"] = cred_json
        return payload


    def create_login(self):
       bearer_token = ""
       self.headers['Authorization'] = self.omevv_encoded_cred
       cred_json = self.create_payload(self.omevv_username,self.omevv_password,self.domain,"api")
       response = requests.post(self.login_url, data=json.dumps(cred_json), headers=self.headers, verify=False);
       data = response.json();
       status_code = response.status_code
       if status_code == 200:
           print("Sucesfully logged in");
           bearer_token = data["accessToken"];
           self.bearer_token = bearer_token
       else:
           raise Exception("Error occured while logging in ", data);

       return bearer_token

    def get_console_details(self):
        console_list = []

        try:
            bearer_token = self.create_login()
            cred_str = 'Bearer ' + bearer_token
            self.headers['Authorization'] = cred_str
            response = requests.get(self.console_url, headers=self.headers, verify=False)
            data = response.json();
            status_code = response.status_code;
            if status_code == 200:
                for con in data:
                    s = json.dumps(con)
                    conObj = json.loads(s, object_hook=consoleDecoder)
                    console_list.append(conObj)
            else:
                raise Exception("Error Occured while fetching the console list ", response)

        except Exception as e:
            print("Exception occured while getting consoles list ", e, " retrying ..");
            if self.retry > 0:
                self.retry = self.retry - 1
                time.sleep(5)
                self.get_console_details()

            else:
                print("Failed after 3 retries,exiting")



        return  console_list

    def set_context(self,console_ip,console_hostname,console_username,console_domain,console_pwd):
        console_id = ""
        isContextSet = False
        try:
                consoleList = self.get_console_details()
                for obj in consoleList:
                    if obj.ip == console_ip or obj.hostname == console_hostname:
                        console_id = obj.id
                        break
                context_pyld = self.create_context_payload(console_id,console_username,console_domain,console_pwd)
                response = requests.post(self.context_url, data=json.dumps(context_pyld), headers=self.headers, verify=False);
                status_code = response.status_code
                if status_code == 204:
                    isContextSet = True
        except Exception as e:
            print(e)




    def get_repoprof_details(self,console_ip,console_hostname,console_username,console_domain,console_pwd):
        prof_list = []
        try:
            self.set_context(console_ip,console_hostname,console_username,console_domain,console_pwd)
            response = requests.get(self.repo_url, headers=self.headers, verify=False)
            data = response.json();
            status_code = response.status_code;
            if status_code == 200:
                for prof in data:
                    s = json.dumps(prof)
                    profobj = json.loads(s, object_hook=repoProfileDecoder)
                    prof_list.append(profobj)
            else:
                raise Exception("Error Occured while fetching the repo profile details ",response)

        except Exception as e:
            print("Exception occured while creating repo ", e, " retrying ..");
            if self.retry > 0:
                self.retry = self.retry - 1
                time.sleep(5)
                self.get_repoprof_details(console_ip,console_hostname,console_username,console_domain,console_pwd)

            else:
                print("Failed after 3 retries,exiting")

        return prof_list







if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script to fetch repository profile details from OMIVV"
    );
    parser.add_argument('-user', help='OMIVV username', required=True);
    parser.add_argument('-pswd', help='OMIVV password', required=True);
    parser.add_argument('-domain', help='OMIVV domain', required=False, default="");
    parser.add_argument('-cip', help='console ip', required=False);
    parser.add_argument('-cname', help='console name', required=False);
    parser.add_argument('-cuser', help='console username', required=True);
    parser.add_argument('-cpwd', help='console password', required=True);
    parser.add_argument('-ip', help='OMIVV ip', required=True);
    parser.add_argument('-cdomain', help='console domain', required=False,default ="");
    parser.add_argument('-repoProfileFilePath', help='complete file path where the omivv repo profile details need to saved', required=False);
    parser.add_argument('-consoleFilePath', help='complete file path where the console details need to saved',
                        required=False);
    args = vars(parser.parse_args());
    if args['cname'] == "" and args['cip'] == "":
        print('Console ip or Console Name is required.Please pass one of them');

    omevv_ip = args['ip'];
    omevv_user = args['user'];
    omevv_pswd = args['pswd'];
    omevv_domain = args['domain'];
    console_username = args['cuser']
    console_domain = args['cdomain']
    console_pwd = args['cpwd']
    console_ip = args['cip']
    console_hostname = args['cname']
    repo_prof_file_det = args['repoProfileFilePath']
    console_file_det = args['consoleFilePath']

    repoObj = RepoDetails(omevv_ip,omevv_user,omevv_pswd,omevv_domain)
    util = Utilities()
    try:
        console_list = repoObj.get_console_details()
        if console_file_det is not None:
            util.write_to_csv(console_list,console_file_det)
    except Exception as e:
        print("Exception occured ",e)
    try:
        repoList = repoObj.get_repoprof_details(console_ip, console_hostname, console_username, console_domain, console_pwd)
        if repo_prof_file_det is not None:
            util.write_to_csv(repoList, repo_prof_file_det)
        else:
            for repo in repoList:
                print(repo)
    except Exception as e:
         print("Exception occured ", e)


