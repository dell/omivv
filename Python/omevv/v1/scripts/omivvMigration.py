import argparse
import sys
import csv
import time
import warnings
from webbrowser import get
from GetOMIVVProfileDetails import ProfileDetails
from registerVcenter import RegisterVcenter
from omevv_apis_client.models import Credential
from CreateRepoProfile import CreateRepo
from createBaselineProfile import CreateBaselineProfile
from omevvServerManagement import HostsManagementWrapper
from getManagementHostComplianceData import HostManagementComplianceWrapper
from autoManageCompliantHosts import AutoManageCompliantHostsWrapper
from utilities import Utilities

from omevv_apis_client.api.group_management import get_groups_for_clusters
from omevv_apis_client.models.get_group_for_cluster_request import GetGroupForClusterRequest
from omevv_apis_client import AuthenticatedClient

import requests,json,base64,constants

class OmivvMigration:
    def __init__(self):
        pass

    def create_payload(self, base_url, uuid, vcUsercredential, clust_ids):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        self.headers = {constants.vcGuidHeader: uuid}
        self.headers["Authorization"] = basicAuth
        self.headers["Content-Type"] = 'application/json'
        self.uuid = uuid
        self.clust_ids = clust_ids
        self.retry = 3
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=self.headers). \
            with_timeout(constants.generalTimeOut_sec)
                
        self.json_body = GetGroupForClusterRequest(clust_ids=self.clust_ids)
 
    def fetch_groups_for_clusters(self):        
        try:
            response: Response[Dict[str, Any]] = \
                get_groups_for_clusters.sync_detailed(uuid=self.uuid, client=self.client, json_body=self.json_body)
            
            if response.status_code == 200:
                return json.loads(response.content)
            else:
                print(json.loads(response.content))
                sys.exit()

        except Exception as e:
            print("Exception occured fetching group id(s) ",e," retrying ..")
            if self.retry > 0:
                self.retry = self.retry - 1
                time.sleep(5)
                self.fetch_groups_for_clusters()
            else:
                print("Failed after 3 retries,exiting")
                sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script for limited migration from OMIVV to OMEVV"
    );
    
    parser.add_argument('-omivvip', help='OMIVV ip', required=True)
    parser.add_argument('-user', help='OMIVV username', required=True)
    parser.add_argument('-pswd', help='OMIVV password', required=True)
    parser.add_argument('-domain', help='OMIVV domain', required=False, default="")
    parser.add_argument('-cip', help='console ip', required=False)
    parser.add_argument('-cname', help='console name', required=False)
    parser.add_argument('-cuser', help='console username', required=True)
    parser.add_argument('-cpwd', help='console password', required=True)
    parser.add_argument('-cdomain', help='console domain', required=False,default ="")
    parser.add_argument('-omeip', help='ome appliance ip', required=True)
    parser.add_argument("-omeusername", help="ome username", required=True)
    parser.add_argument("-omepassword", help="ome password", required=True)

    args = vars(parser.parse_args());
    if args['cname'] == "" and args['cip'] == "":
        print('Console ip or Console Name is required.Please pass one of them')

    omivv_ip = args['omivvip']
    omivv_user = args['user']
    omivv_pswd = args['pswd']
    omivv_domain = args['domain']
    console_username = args['cuser']
    console_domain = args['cdomain']
    console_pwd = args['cpwd']
    console_ip = args['cip']
    console_hostname = args['cname']
    ome_ip = args['omeip']
    ome_username = args['omeusername']
    ome_password = args['omepassword']

    profile_obj = ProfileDetails(omivv_ip,omivv_user,omivv_pswd,omivv_domain)
    bearer_token = profile_obj.get_bearer_token()
    try:
        console_list = profile_obj.get_console_details(bearer_token=bearer_token)

        console_data = []
        for console in console_list:
            profile_dict = dict(console._asdict())
            console_data.append(profile_dict)
        console_data = [{"id": each['id'],
                      "ip": each['ip'],
                      "registeredWithVlcm": each['registeredWithVlcm']
                      } for each in console_data]

    except Exception as e:
        print("Exception occured ",e)

    try:
        repoList = profile_obj.get_repoprof_details(console_ip, console_hostname, console_username, console_domain,
                                                    console_pwd, bearer_token=bearer_token)
        repo_data = []
        for repo_profile in repoList:
            profile_dict = dict(repo_profile._asdict())
            if profile_dict['data'].protocolType == 'NFS':                
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

    try:
        cluster_pro_list = profile_obj.get_cluster_pro_details(console_ip, console_hostname, console_username,
                                                               console_domain,
                                                               console_pwd,
                                                               bearer_token=bearer_token)
        cluster_prof_data = []
        for cluster_profile in cluster_pro_list:
            profile_dict = dict(cluster_profile._asdict())
            cluster_prof_data.append(profile_dict)
        cluster_prof_data = [{"id": each['id'],
                      "profileName": each['data'].profileName,
                      "description": each['data'].description,
                      "clusters": each['data'].clusters,
                      "repo": each['data'].repo
                      } for each in cluster_prof_data]
    except Exception as e:
        print("Exception occurred ", e)
   
    profile_obj.logout(bearer_token)
  
    cluster_ids = []
    for cluster_prof in cluster_prof_data:
        for cluster in cluster_prof['clusters']:
            cluster_ids.append(cluster.id)

    unregister_val = input("Confirm unregister vCenter (Y/N): ")
    if unregister_val == "Y":
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ome_ip)
        credential = Credential(username=ome_username, password=ome_password)
        registervcenterhelper = RegisterVcenter()
        extensions = []
        if (console_data[0])['registeredWithVlcm'] == True:
            extensions = ["WEBCLIENT_PHA", "VLCM"]
        else:
            extensions = ["WEBCLIENT_PHA"]
        registervcenterhelper.create_payload(base_url=base_url, omeIp=ome_ip, omeUsercredential=credential, vcusername=console_username, \
                                             vcpassword=console_pwd, console_address=console_ip, description=None, extensions=extensions)
        success, uuid = registervcenterhelper.register_vcenter()
        if success == False:
            sys.exit()
            print("unregister vCenter to proceed ahead")

    else:
        print("unregister vCenter to proceed ahead")
        sys.exit()

    discover_server = input("Discover Server Device (Y/N): ")
    if discover_server != "Y":
        print("discover server device to proceed ahead")
        sys.exit()

    create_repo_obj = CreateRepo(ome_ip,console_username,console_pwd,uuid)

    create_repo_obj.create_payload((repo_data[0])['profileName'],(repo_data[0])["description"],(repo_data[0])["repoType"], \
                                   (repo_data[0])["uri"],(repo_data[0])["protocolType"],None,None,None)
    repo_output = create_repo_obj.create_repo_profile()
    if isinstance(repo_output, str):
        repo_id = repo_output.partition("id ")[2]
    else:
        print(repo_output)
        sys.exit()

    #find group id by cluster id
    base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ome_ip)
    credential = Credential(username=console_username, password=console_pwd)
    omivvmigrationhelper = OmivvMigration()
    omivvmigrationhelper.create_payload(base_url=base_url, uuid=uuid, vcUsercredential=credential, clust_ids=cluster_ids)
    response_content = omivvmigrationhelper.fetch_groups_for_clusters()
    group_ids = []
    for group_info in response_content:
        if group_info['clustId'] in cluster_ids:
            group_ids.append(group_info['groupId'])

    #auto manage hosts
    hostmgmtcompliancehelper = HostManagementComplianceWrapper()
    automanagecomplianthosthelper = AutoManageCompliantHostsWrapper()

    for compliance_filter in ["COMPLIANT","NONCOMPLIANT"]:        
        hostmgmtcompliancehelper.create_payload(base_url=base_url, omeIp=ome_ip, vcUsercredential=credential, \
                                                vCenterUUID=uuid, compliance_filter=compliance_filter)  
        success,response = hostmgmtcompliancehelper.get_managed_hosts_compliance()
        if success:
            manage_host_ids = automanagecomplianthosthelper.getHostIds(response)

    if len(manage_host_ids) > 0:
        jobname = f"API ManageJob-{time.ctime()}"
        hostmgmthelper = HostsManagementWrapper()
        hostmgmthelper.create_payload(base_url=base_url, omeIp=ome_ip, vcUsercredential=credential, \
                                            vCenterUUID=uuid, payload={}, jobname=jobname, \
                                            jobdescription=None, host_ids=manage_host_ids)
        hostmgmthelper.run_manage_job()

    time.sleep(20)
    #migrate baseline profile in OMEVV
    create_baseline_prof_obj = CreateBaselineProfile()

    create_baseline_prof_obj.create_payload(name=(cluster_prof_data[0])['profileName'],description=(cluster_prof_data[0])['description'], \
                                            firmware_repoid=repo_id,driver_repoid=None,configuration_repoid=None,createdby=None, \
                                            group_idslist=group_ids,time="03:00",retry=3,monday=False,tuesday=False,wednesday=False, \
                                            thursday=False,friday=False,saturday=False,sunday=True)

    baselineprofile_id=create_baseline_prof_obj.create_baselineprofile(vc_username=console_username,vc_pwd=console_pwd,
                                                                 omevv_ip=ome_ip,vc_uuid=uuid,retry=3)