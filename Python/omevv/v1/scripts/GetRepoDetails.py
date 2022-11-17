import argparse
import sys
import csv
import time
import warnings
from webbrowser import get

import requests,json,base64
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(
    description="Python script to fetch repository profile details from OMIVV"
);
parser.add_argument('-ip', help='OMIVV IP address', required=True);
parser.add_argument('-user', help='OMIVV username', required=True);
parser.add_argument('-pswd', help='OMIVV password', required=True);
parser.add_argument('-domain', help='OMIVV domain', required=False,default="");
parser.add_argument('-cip', help='console ip', required=False);
parser.add_argument('-cname', help='console name', required=False);

args = vars(parser.parse_args());
ip = args['ip'];
user = args['user'];
pswd = args['pswd'];
domain = args['domain'];

if args['cname'] == "" and args['cip'] == "":
    raise Exception('Console ip or Console Name is required.Please pass one of them');
cip = args['cip']
cname = args['cname']
cid = "";

retry = 3;
payload ={};


def create_payload():
    cred_json = {"username":user.strip(),"domain":domain.strip(),"password":pswd.strip()};
    payload['apiUserCredential'] = cred_json;




def encode_cred(username,pwd):
    cred_str = username+":"+pwd;
    cred_str_bytes = cred_str.encode("ascii");
    base64_bytes = base64.b64encode(cred_str_bytes);
    base64_string = base64_bytes.decode("ascii");
    return base64_string;


def create_login():
    global retry;

    url = "https://%s/Spectre/api/rest/v1/Services/AuthenticationService/login"%(ip);
    encoded_cred = encode_cred(user, pswd);
    try:
        headers = {'content-type': 'application/json'}
        cred_str = 'Basic ' + encoded_cred;
        headers['Authorization'] = cred_str;
        create_payload();
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False);
        data = response.json();
        status_code = response.status_code
        if status_code == 200:
            print("Sucesfully logged in");
            bearer_token = data["accessToken"];
        else:
            raise Exception("Error occured while logging in ", data);
    except Exception as e:
        print("Exception occured while logging in ", e,type(e), " retrying ..");
        if retry > 0:
            retry = retry - 1;
            time.sleep(5);
            create_login();
        # create_repo_profl();
        else:
            print("Failed after 3 retries,exiting");
            sys.exit();

    return bearer_token;

def get_vcentre_details():
    retry = 3
    bearer_token = create_login()
    file_name = "console_details.csv";
    url = "https://%s/Spectre/api/rest/v1/Services/ConsoleService/Consoles"%(ip);
    try:
        cred_str = 'Bearer ' + bearer_token;
        headers = {'Authorization' : cred_str};
        response = requests.get(url, headers=headers, verify=False);
        data = response.json();
        status_code = response.status_code;
        if status_code == 200:
            write_to_csv(data,file_name)
            print("Successfully retrieved console id");
        else:
            raise Exception("Error occured while fetching console id ", data);
    except Exception as e:
        print("Exception occured while fetching console id ", e,type(e), " retrying ..")
        if retry > 0:
            retry = retry - 1;
            time.sleep(5);
            get_vcentre_details()
        # create_repo_profl();
        else:
            print("Failed after 3 retries,exiting");
            sys.exit();




def write_to_csv(data,file):
    fh = open(file, 'w')
    csv_writer = csv.writer(fh)
    count = 0
    for row in data:
        if count == 0:
            header = row.keys()
            csv_writer.writerow(header)
            count += 1
        if row['ip'] == cip or row['hostname'] == cname:
            cid = id;

        csv_writer.writerow(row.values())
    fh.close()


def set_context():
    #1.call get_vcentre_details() method to save in csv
    # and also to set the context id for which the console ip or host name matches
    #2.check if consoleid is non empty and use that to create the context
    # using uri:https://<ip>/Spectre/api/rest/v1/Services/ConsoleService/OperationalContext
    pass

def get_repo_details():
    #1.set the context using set_context() method
    #if success ,fetch the repo details and save in csv file.(retry 3times)
    #if error occurs raise exception and exit.
    pass

if __name__ == "__main__":
    get_vcentre_details()
