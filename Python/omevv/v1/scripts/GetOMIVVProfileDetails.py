import argparse
import time
from omivv_models import consoleDecoder, repoProfileDecoder, ClusterProfileDecoder
from utilities import Utilities
import requests, json, base64


class ProfileDetails:
    def __init__(self, omivv_ip, omivv_username, omivv_pwd, domain):
        self.omivv_username = omivv_username.strip()
        self.headers = {'content-type': 'application/json'}
        self.domain = domain
        self.omivv_password = omivv_pwd.strip()
        self.login_url = "https://%s/Spectre/api/rest/v1/Services/AuthenticationService/login" % (omivv_ip)
        self.logoff_url = "https://%s/Spectre/api/rest/v1/Services/AuthenticationService/logoff" % omivv_ip
        self.console_url = "https://%s/Spectre/api/rest/v1/Services/ConsoleService/Consoles" % (omivv_ip)
        self.context_url = "https://%s/Spectre/api/rest/v1/Services/ConsoleService/OperationalContext" % (omivv_ip)
        self.repo_url = "https://%s/Spectre/api/rest/v1/Services/PluginProfileService/RepositoryProfiles" % (omivv_ip)
        self.baseline_url = "https://%s/Spectre/api/rest/v1/Services/PluginProfileService/ClusterProfiles" % omivv_ip
        self.omivv_encoded_cred = self.encode_cred(self.omivv_username, self.omivv_password)
        self.payload_cred_dict = {}
        self.payload_cred_dict['console'] = 'consoleUserCredential'
        self.payload_cred_dict['api'] = 'apiUserCredential'
        self.retry = 3
        # Generating the bearer token to be used in this script
        self.headers['Authorization'] = self.omivv_encoded_cred

    def get_bearer_token(self):
        """Create bearer token"""
        try:
            post_body_data = {"apiUserCredential": {"username": self.omivv_username,
                                                  "domain": "",
                                                  "password": self.omivv_password}}
            response = requests.post(self.login_url, json=post_body_data, verify=False)
            if response.status_code == 200:
                json_response = response.json()
                bearer_token = json_response['accessToken']
                return bearer_token
            else:
                print("Login to OMIVV failed")
        except:
            print("get_bearer_token: Unexpected error:", sys.exc_info()[0])

    def logout(self, session_token):
        """Log off OMIVV bearer token"""
        try:
            head = {'Authorization': 'Bearer ' + session_token}
            response = requests.post(self.logoff_url, verify=False, headers=head)
            if response.status_code != 200:
                print("Log out failed.")
        except:
            print("get_bearer_token: Unexpected error:", sys.exc_info()[0])

    def encode_cred(self, username, pwd):
        cred_str = username + ":" + pwd;
        cred_str_bytes = cred_str.encode("ascii");
        base64_bytes = base64.b64encode(cred_str_bytes);
        base64_string = base64_bytes.decode("ascii");
        return base64_string

    def create_payload(self, username, pwd, domain, type):
        payload = {}
        cred_json = {"username": username.strip(), "domain": domain.strip(), "password": pwd.strip()};
        payload[self.payload_cred_dict[type]] = cred_json
        return payload

    def create_context_payload(self, cid, console_username, console_domain, console_pwd):
        payload = {}
        payload['consoleId'] = cid
        cred_json = {"username": console_username.strip(), "domain": console_domain.strip(),
                     "password": console_pwd.strip()};
        payload["consoleUserCredential"] = cred_json
        return payload

    def get_console_details(self, bearer_token):
        console_list = []

        try:
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
                self.get_console_details(bearer_token=bearer_token)

            else:
                print("Failed after 3 retries,exiting")

        return console_list

    def set_context(self, console_ip, console_hostname, console_username, console_domain, console_pwd, bearer_token):
        console_id = ""
        isContextSet = False
        try:
            consoleList = self.get_console_details(bearer_token=bearer_token)
            for obj in consoleList:
                if obj.ip == console_ip or obj.hostname == console_hostname:
                    console_id = obj.id
                    break
            context_pyld = self.create_context_payload(console_id, console_username, console_domain, console_pwd)
            response = requests.post(self.context_url, data=json.dumps(context_pyld), headers=self.headers,
                                     verify=False);
            status_code = response.status_code
            if status_code == 204:
                isContextSet = True
        except Exception as e:
            print(e)

    def get_repoprof_details(self, console_ip, console_hostname, console_username, console_domain, console_pwd,
                             bearer_token):
        prof_list = []
        try:
            self.set_context(console_ip, console_hostname, console_username, console_domain, console_pwd,
                             bearer_token=bearer_token)
            response = requests.get(self.repo_url, headers=self.headers, verify=False)
            data = response.json();
            status_code = response.status_code;
            if status_code == 200:
                for prof in data:
                    s = json.dumps(prof)
                    profobj = json.loads(s, object_hook=repoProfileDecoder)
                    prof_list.append(profobj)
            else:
                raise Exception("Error Occurred while fetching the repo profile details ", response)

        except Exception as e:
            print("Exception occurred while creating repo ", e, " retrying ..");
            if self.retry > 0:
                self.retry = self.retry - 1
                time.sleep(5)
                self.get_repoprof_details(console_ip, console_hostname, console_username, console_domain, console_pwd,
                                          bearer_token=bearer_token)

            else:
                print("Failed after 3 retries, exiting")

        return prof_list

    def get_cluster_pro_details(self, console_ip, console_hostname, console_username, console_domain, console_pwd,
                                bearer_token):
        prof_list = []
        try:
            self.set_context(console_ip, console_hostname, console_username, console_domain, console_pwd)
            response = requests.get(self.baseline_url, headers=self.headers, verify=False)
            data = response.json();
            status_code = response.status_code;
            if status_code == 200:
                for prof in data:
                    s = json.dumps(prof)
                    profobj = json.loads(s, object_hook=ClusterProfileDecoder)
                    prof_list.append(profobj)
            else:
                raise Exception("Error Occurred while fetching the repo profile details ", response)

        except Exception as e:
            print("Exception occurred while creating repo ", e, " retrying ..");
            if self.retry > 0:
                self.retry = self.retry - 1
                time.sleep(5)
                self.get_cluster_pro_details(console_ip, console_hostname, console_username, console_domain, console_pwd,
                                          bearer_token=bearer_token)

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
    parser.add_argument('-cdomain', help='console domain', required=False, default="");
    parser.add_argument('-repoProfileFilePath',
                        help='complete file path where the omivv repo profile details need to saved', required=False);
    parser.add_argument('-bpFilePath',
                        help='complete file path where the omivv baseline profile details need to saved',
                        required=False);
    parser.add_argument('-consoleFilePath', help='complete file path where the console details need to saved',
                        required=False);
    args = vars(parser.parse_args());
    if args['cname'] == "" and args['cip'] == "":
        print('Console ip or Console Name is required.Please pass one of them');

    omivv_ip = args['ip'];
    omivv_user = args['user'];
    omivv_pswd = args['pswd'];
    omivv_domain = args['domain'];
    console_username = args['cuser']
    console_domain = args['cdomain']
    console_pwd = args['cpwd']
    console_ip = args['cip']
    console_hostname = args['cname']
    repo_prof_file_det = args['repoProfileFilePath']
    console_file_det = args['consoleFilePath']
    baseline_prof_file_det = args['bpFilePath']

    profile_obj = ProfileDetails(omivv_ip, omivv_user, omivv_pswd, omivv_domain)
    bearer_token = profile_obj.get_bearer_token()
    util = Utilities()
    try:
        console_list = profile_obj.get_console_details(bearer_token=bearer_token)
        if console_file_det is not None:
            util.write_to_csv(console_list, console_file_det)
    except Exception as e:
        print("Exception occurred ", e)
    try:
        repoList = profile_obj.get_repoprof_details(console_ip, console_hostname, console_username, console_domain,
                                                    console_pwd, bearer_token=bearer_token)
        if repo_prof_file_det is not None:
            list_data = []
            for profile in repoList:
                profile_dict = dict(profile._asdict())
                list_data.append(profile_dict)
            list_data = [{"id": each['id'],
                          "href": each['href'],
                          "objectType": each['objectType'],
                          "profileName": each['profileName'],
                          "description": each['description'],
                          "repoType": each['repoType']
                          } for each in list_data]
            util.write_to_csv(list_data, repo_prof_file_det)
        else:
            for repo in repoList:
                print(repo)
    except Exception as e:
        print("Exception occurred ", e)
    # Get cluster profile detail
    try:
        cluster_pro_list = profile_obj.get_cluster_pro_details(console_ip, console_hostname, console_username,
                                                               console_domain,
                                                               console_pwd,
                                                               bearer_token=bearer_token)
        if baseline_prof_file_det is not None:
            list_data = []
            for profile in cluster_pro_list:
                profile_dict = dict(profile._asdict())
                list_data.append(profile_dict)
            list_data = [{"id": each['id'],
                          "href": each['href'],
                          "objectType": each['objectType'],
                          "profileName": each['profileName'],
                          "description": each['description']
                          } for each in list_data]
            util.write_to_csv(list_data, baseline_prof_file_det)
        else:
            for cp in cluster_pro_list:
                print(cp)
    except Exception as e:
        print("Exception occurred ", e)

    profile_obj.logout(bearer_token)
