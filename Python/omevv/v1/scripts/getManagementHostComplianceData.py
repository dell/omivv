from typing import Any, Dict, List, Optional, Union
import argparse
from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.api.console_compliance_and_discovery import get_host_compliance
from omevv_apis_client.models import ManagedHost
from omevv_apis_client.models import HostCompliance
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
import constants
import base64
import xlwt
from omevv_apis_client.types import Response

class HostManagementComplianceWrapper:
    def __init__(self, base_url, vcUsercredential, vCenterUUID, compliance_filter):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        headers = {constants.vcGuidHeader: vCenterUUID}
        headers["Authorization"] = basicAuth
        self.uuid = vCenterUUID
        self.compliance_filter = compliance_filter
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=headers). \
            with_timeout(constants.generalTimeOut_sec)

    def get_managed_hosts_compliance(self):
        response: Response[Union[ErrorObject, List[HostCompliance]]] = \
            get_host_compliance.sync_detailed(uuid=self.uuid, client=self.client)
        return response.parsed

    def populate_headers(self, column_count):
        sheet1.write(column_count,0,"hostid")
        sheet1.write(column_count,1,"host name")
        sheet1.write(column_count,2,"model")
        sheet1.write(column_count,3,"service tag")
        sheet1.write(column_count,4,"console id")
        sheet1.write(column_count,5,"console entity id")
        sheet1.write(column_count,6,"hypervisor")
        sheet1.write(column_count,7,"idrac ip")
        sheet1.write(column_count,8,"idrac firmware version")
        sheet1.write(column_count,9,"idrac license type")
        sheet1.write(column_count,10,"idrac license description")
        sheet1.write(column_count,11,"idrac license expiration date")
        sheet1.write(column_count,12,"license entitlement id")
        sheet1.write(column_count,13,"idrac license status")
        sheet1.write(column_count,14,"snmp trap status")
        sheet1.write(column_count,15,"state")
        sheet1.write(column_count,16,"connection state")

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
    PARSER.add_argument("--compliance_filter", "-g", required=True, default=None, help="compliance_filter")
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None and ARGS.compliance_filter is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)
        output=HostManagementComplianceWrapper(base_url=base_url, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, compliance_filter=ARGS.compliance_filter).get_managed_hosts_compliance()
        
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
        
        column_count = 0;
        data_present = False;
        HostManagementComplianceWrapper(base_url=base_url, vcUsercredential=credential, vCenterUUID=ARGS.vcUUID, compliance_filter=ARGS.compliance_filter).populate_headers(column_count)  
        column_count = column_count + 1;
        for row_num,x in enumerate(output):
            if ARGS.compliance_filter == x.state:
                data_present = True;
                sheet1.write(column_count, 0, x.hostid)
                sheet1.write(column_count, 1, x.host_name)
                sheet1.write(column_count, 2, x.model)
                sheet1.write(column_count, 3, x.service_tag)
                sheet1.write(column_count, 4, x.console_id)
                sheet1.write(column_count, 5, x.console_entity_id)
                sheet1.write(column_count, 6, x.hypervisor)
                sheet1.write(column_count, 7, x.idrac_ip)
                sheet1.write(column_count, 8, x.idrac_firmware_version)
                column_count_copy = column_count
                if len(x.license_details) > 0 and x.license_details is not None:
                    for license_row,license in enumerate(x.license_details):
                        if license_row > 0:
                            column_count = column_count + 1;

                        sheet1.write(column_count, 9, license.idrac_license_type)
                        sheet1.write(column_count, 10, license.idrac_license_description)

                        if license.idrac_license_expiration_date is not None:
                            sheet1.write(column_count, 11, str(license.idrac_license_expiration_date))
                        else:
                            sheet1.write(column_count, 11, "Not Available")
                        
                        sheet1.write(column_count, 12, license.license_entitlement_id)
                
                column_count = column_count_copy
                sheet1.write(column_count, 13, x.idrac_license_status)
                sheet1.write(column_count, 14, x.snmp_trap_status)
                sheet1.write(column_count, 15, x.state)
                sheet1.write(column_count, 16, x.connection_state)

                column_count = column_count + 1;

            name = "export.xls"
            book.save(name)

        if data_present == False:
            print("There are no " +ARGS.compliance_filter+" hosts")

    else:
        print("Required parameters missing. Please review module help.")