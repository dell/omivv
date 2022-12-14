from typing import Any, Dict, List, Optional, Union
import argparse
import constants
import base64
import csv
import time
import sys
import json
from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.api.host_inventory import get_managed_hosts
from omevv_apis_client.models.get_managed_hosts_maintenance_mode import GetManagedHostsMaintenanceMode
from omevv_apis_client.models import ManagedHost
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
from omevv_apis_client.types import Response


class ManageHostWrapper:
    def __init__(self, base_url, vcUsercredential, vCenterUUID):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        headers = {constants.vcGuidHeader: vCenterUUID}
        headers["Authorization"] = basicAuth
        self.uuid = vCenterUUID
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=headers). \
            with_timeout(constants.generalTimeOut_sec)

    def get_managed_hosts(self, maintenanceMode, serviceTag, consoleEntityId):
        try:
            response: Response[Union[ErrorObject, List[ManagedHost]]] = \
                get_managed_hosts.sync_detailed(uuid=self.uuid, client=self.client, maintenance_mode=maintenanceMode, \
                                                service_tag=serviceTag, console_entity_id=consoleEntityId)
            if response.status_code == 200:
                return response.parsed
            else:
                if response.parsed.message:
                    raise Exception(response.parsed.message)
                else:
                    raise Exception(json.loads(response.content)["message"])
        except Exception as e:
            print("FAILED: Exception occured while querying managed hosts \"%s\"" % e)
            sys.exit(1)


def filter_maintenancemode(value):
    switch = {
        "OUTSIDE_MAINTENANCEMODE": GetManagedHostsMaintenanceMode.OUTSIDE_MAINTENANCEMODE,
        "INSIDE_MAINTENANCEMODE": GetManagedHostsMaintenanceMode.INSIDE_MAINTENANCEMODE
        }
    return switch.get(value, None)


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
    PARSER.add_argument("--serviceTag", required=False, default=None,
                        help="filter result for serviceTag")
    PARSER.add_argument("--maintenanceMode", required=False, default=None,
                        help="filter result by maintenanceMode(INSIDE_MAINTENANCEMODE/OUTSIDE_MAINTENANCEMODE)",
                        choices=["INSIDE_MAINTENANCEMODE","OUTSIDE_MAINTENANCEMODE"])
    PARSER.add_argument("--consoleEntityId", required=False, default=None,
                        help="filter result by consoleEntityId")
    ARGS = PARSER.parse_args()

    base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
    credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
    serviceTag = ARGS.serviceTag
    maintenanceMode = filter_maintenancemode(ARGS.maintenanceMode)
    consoleEntityId = ARGS.consoleEntityId
    managehostwrapper = ManageHostWrapper(base_url=base_url, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID)
    managed_hosts = managehostwrapper.get_managed_hosts(maintenanceMode=maintenanceMode, serviceTag=serviceTag, consoleEntityId=consoleEntityId)

    if managed_hosts:
        csv_headers = managed_hosts[0].to_dict().keys()
        timestamp = time.strftime("%Y%m%d%H%M%S")
        reportname = f"ManagedHostReport_{timestamp}.csv"
        with open(reportname,"w") as fh:
            writer = csv.DictWriter(fh, fieldnames=csv_headers)
            writer.writeheader()
            [writer.writerow(i.to_dict()) for i in managed_hosts]
        print(f"SUCCESS: Results written to {reportname}")
    else:
        print("SUCCESS: No Managed Hosts found.")
