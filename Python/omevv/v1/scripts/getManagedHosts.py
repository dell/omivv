from typing import Any, Dict, List, Optional, Union
import argparse as argparse
from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.api.host_inventory import get_managed_hosts
from omevv_apis_client.models import ManagedHost
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
import constants
import base64

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

    def get_managed_hosts(self):
        response: Response[Union[ErrorObject, List[ManagedHost]]] = \
            get_managed_hosts.sync_detailed(uuid=self.uuid, client=self.client)
        return response.parsed


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
    ARGS = PARSER.parse_args()
    if ARGS.ip is not None and ARGS is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        ManageHostWrapper(base_url=base_url, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID).get_managed_hosts()
        # TODO: Error handling and response formatting
    else:
        print("Required parameters missing. Please review module help.")
