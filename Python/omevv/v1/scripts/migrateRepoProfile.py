import argparse
import warnings
import requests,json
from GetOMIVVProfileDetails import ProfileDetails
from CreateRepoProfile import CreateRepo

class MigrateRepoProfile:
    def __init__(self):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script for migration of repository profiles from OMIVV to OMEVV"
    );
    
    parser.add_argument('-omivvip', help='OMIVV ip', required=True)
    parser.add_argument('-omivvuser', help='OMIVV username', required=True)
    parser.add_argument('-omivvpwd', help='OMIVV password', required=True)
    parser.add_argument('-omivvdomain', help='OMIVV domain', required=False, default="")
    parser.add_argument('-omivvconsoleip', help='console ip', required=False)
    parser.add_argument('-omivvconsolename', help='console name', required=False)
    parser.add_argument('-omivvconsoleusername', help='console username', required=True)
    parser.add_argument('-omivvconsolepwd', help='console password', required=True)
    parser.add_argument('-omivvconsoledomain', help='console domain', required=False,default ="")
    parser.add_argument('-omeip', help='ome appliance ip', required=True)
    parser.add_argument("-omevvconsoleuuid", help="uuid for omevv migration", required=True)
    parser.add_argument("-omevvconsoleusername", help="omevv console username", required=True)
    parser.add_argument("-omevvconsolepwd", help="omevv console password", required=True)

    args = vars(parser.parse_args());
    if args['omivvconsolename'] == "" and args['omivvconsoleip'] == "":
        print('Console ip or Console Name is required.Please pass one of them')

    omivv_ip = args['omivvip']
    omivv_user = args['omivvuser']
    omivv_pswd = args['omivvpwd']
    omivv_domain = args['omivvdomain']
    console_username = args['omivvconsoleusername']
    console_domain = args['omivvconsoledomain']
    console_pwd = args['omivvconsolepwd']
    console_ip = args['omivvconsoleip']
    console_hostname = args['omivvconsolename']
    ome_ip = args['omeip']
    omevv_console_uuid = args['omevvconsoleuuid']
    omevv_console_username = args['omevvconsoleusername']
    omevv_console_pwd = args['omevvconsolepwd']

    profile_obj = ProfileDetails(omivv_ip,omivv_user,omivv_pswd,omivv_domain)
    bearer_token = profile_obj.get_bearer_token()

    try:
        repoList = profile_obj.get_repoprof_details(console_ip, console_hostname, console_username, console_domain,
                                                    console_pwd, bearer_token=bearer_token)
        repo_data = []
        for repo_profile in repoList:
            profile_dict = dict(repo_profile._asdict())
            repo_data.append(profile_dict)
        repo_data = [{"id": each['id'],
                      "profileName": each['data'].name,
                      "description": each['data'].description,
                      "repoType": each['data'].repoType,
                      "protocolType": each['data'].protocolType,
                      "uri": each['data'].uri,
                      } for each in repo_data]

    except Exception as e:
        print("Exception occurred ", e)
        print("Migration Failed. Not able to retrieve repository profile details from OMIVV. Make sure all the services are up and running")
        profile_obj.logout(bearer_token)
        sys.exit()
  
    if len(repoList) == 0:
        print("Migration Failed. Not able to retrieve repository profile details from OMIVV. Make sure all the services are up and running")
        profile_obj.logout(bearer_token)
        sys.exit()

    profile_obj.logout(bearer_token)

    create_repo_obj = CreateRepo(ome_ip,omevv_console_username,omevv_console_pwd,omevv_console_uuid)

    for repository in repo_data:
        if repository["profileName"] == 'Dell Default Catalog' or repository["profileName"] == 'Validated MX stack Catalog' or repository["repoType"].upper() == 'DRIVER':
            continue
        
        elif repository["protocolType"] != 'NFS':
            print("Migrating repository profile having profile name {} and uri {} to OMEVV".format(repository["profileName"], repository["uri"]))
            share_username = input("Enter share username for {} share {} : ".format(repository["protocolType"], repository["uri"]))
            share_password = input("Enter share password for {} share {} : ".format(repository["protocolType"], repository["uri"]))
            args['spcred'] = str(share_username+"|"+share_password)
            create_repo_obj.create_payload(repository['profileName'],repository["description"],repository["repoType"], \
                                   repository["uri"],repository["protocolType"],args['spcred'],None,None)
        else:
            print("Migrating repository profile having profile name {} and uri {} to OMEVV".format(repository["profileName"], repository["uri"]))
            create_repo_obj.create_payload(repository['profileName'],repository["description"],repository["repoType"], \
                                   repository["uri"],repository["protocolType"],None,None,None)

        repo_output = create_repo_obj.create_repo_profile()
        print(repo_output)