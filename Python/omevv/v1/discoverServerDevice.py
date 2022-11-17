from typing import Any, Dict, List, Optional, Union
import argparse
from omevv_apis_client import AuthenticatedClient
#from omevv_apis_client.api.console_compliance_and_discovery import get_host_compliance
#from omevv_apis_client.models import ManagedHost
#from omevv_apis_client.models import HostCompliance
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
import constants
import base64
from omevv_apis_client.types import Response

class HostDiscoveryWrapper:
    def __init__(self, base_url, omeIp, vcUsercredential, vCenterUUID, payload, jobname, jobdescription, console_entity_id, device_username, device_password):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        headers = {constants.vcGuidHeader: vCenterUUID}
        headers["Authorization"] = basicAuth
        self.omeIp = omeIp
        self.uuid = vCenterUUID
        self.payload = payload
        self.jobname = jobname
        self.jobdescription = jobdescription
        self.console_entity_id = console_entity_id
        self.device_username = device_username
        self.device_password = device_password
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=headers). \
            with_timeout(constants.generalTimeOut_sec)

    def get_managed_hosts_compliance(self):
        response: Response[Union[ErrorObject, List[HostCompliance]]] = \
            get_host_compliance.sync_detailed(uuid=self.uuid, client=self.client)
        return response.parsed

    def create_payload(self):
        if self.jobname:
            self.payload["jobName"] = self.jobname;
        if self.jobdescription:
            self.payload["jobDescription"] = self.jobdescription;

        hostDiscoveryGroupPayload = []
        hostDiscoveryGroupPayload.append(
            {
                "consoleEntityIDs": [self.console_entity_id],
                "userName": self.device_username,
                "password": self.device_password,
                "useGlobalCredentials": True            
            }
        )

        if self.console_entity_id and self.device_username and self.device_password:
            self.payload["hostDiscoveryGroups"] = hostDiscoveryGroupPayload;

    def run_discovery(self):
        global retry
        retry = 3
        headers = self.headers
        url = 'https://{ip}/omevv/GatewayService/v1/Consoles/'+self.uuid+'/Hosts/Discover'.format(ip = self.omeIp)
        try:
            response = requests.post(url, data=json.dumps(self.payload), headers=headers, verify=False);
            data = response.json();
            status_code = response.status_code
            if status_code == 200:
              return "Discovery job is created successfully with id "+ str(data);
            else:
                raise Exception("Error occured while creating discovery job ",data);
        except Exception as e:
            print("Exception occured while creating discovery job ",e," retrying ..");
            if retry > 0:
                retry = retry - 1;
                time.sleep(5);
                run_discovery();

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
    PARSER.add_argument("--jobname", "-g", required=True, default=None, help="job name")
    PARSER.add_argument("--jobdescription", "-g", required=True, default=None, help="job description")
    PARSER.add_argument("--console_entity_id", "-g", required=True, default=None, help="console entity id of the server device")
    PARSER.add_argument("--device_username", "-g", required=True, default=None, help="username of device")
    PARSER.add_argument("--device_password", "-g", required=True, default=None, help="password of device")

    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.compliance_filter is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        payload = {}
        output=HostDiscoveryWrapper(base_url=base_url, omeIp=ARGS.ip, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, payload=payload, jobname=ARGS.jobname, jobdescription=ARGS.jobdescription, console_entity_id=ARGS.console_entity_id, device_username=ARGS.device_username, device_password=ARGS.device_password).create_payload()
        
    else:
        print("Required parameters missing. Please review module help.")