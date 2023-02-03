import datetime
import time
from typing import Union, List, Dict, Any
import argparse
from omevv_apis_client import AuthenticatedClient
from omevv_apis_client.api.console_inventory import get_console_clusters
from omevv_apis_client.api.group_management import get_group_by_id
from omevv_apis_client.api.job_management import get_update_service_job_by_id
from omevv_apis_client.models import FirmwareUpdateRequestRebootOptions, \
    FirmwareUpdateRequestEnterMaintenanceModeOption, HostFirmwareComponents, Schedule, FirmwareDriftResponseModel, Job, \
    ManagedHost, Group, ConsoleEntity
from omevv_apis_client.models import ErrorObject
from omevv_apis_client.models import Credential
from omevv_apis_client.models.update_request import UpdateRequest
import constants
import base64
import json
from omevv_apis_client.types import Response
from omevv_apis_client.api.update_management import trigger_update
from omevv_apis_client.api.update_management import get_firmware_drift_report_by_host_id, can_trigger_update
from omevv_apis_client.models.firmware_update_request import FirmwareUpdateRequest
from omevv_apis_client.api.host_inventory import get_managed_hosts


class FWUpdateWrapper:
    def __init__(self, base_url, vcUsercredential, vCenterUUID):
        credential = vcUsercredential.username + ":" + vcUsercredential.password
        basicAuth = "Basic %s" % base64.b64encode(credential.encode('utf-8')).decode()
        headers = {constants.vcGuidHeader: vCenterUUID}
        headers["Authorization"] = basicAuth
        self.uuid = vCenterUUID
        self.client = AuthenticatedClient(base_url=base_url, token=None, verify_ssl=False). \
            with_headers(headers=headers). \
            with_timeout(constants.generalTimeOut_sec)

    def check_response_code_and_return(self, response, message):
        if response.status_code == 200:
            response_dict = json.loads(response.content.decode("utf-8").replace("'", '"'))
            return response_dict, response.status_code
        else:
            print("ERROR: " + message)
            print("Error code: ", response["errorCode"])
            print("Error Message: ", response["message"])
            exit(1)

    def get_managed_host_list(self):
        response: Response[Union[ErrorObject, List[ManagedHost]]] = get_managed_hosts.sync_detailed(uuid=self.uuid,
                                                                                                    client=self.client)
        response_dict, response.status_code = self.check_response_code_and_return(response,
                                                                                  message="Unable to get the managed host list")
        return response_dict, response.status_code

    def get_group_detail(self, omevv_group_id):
        response: Response[Union[ErrorObject, Group]] = get_group_by_id.sync_detailed(uuid=self.uuid,
                                                                                      client=self.client,
                                                                                      gid=omevv_group_id)
        response_dict, response.status_code = self.check_response_code_and_return(response,
                                                                                  message="Failed to get group detail")
        return response_dict, response.status_code

    def get_cluster_detail(self, cluster_id):
        response: Response[list[ConsoleEntity]] = get_console_clusters.sync_detailed(uuid=self.uuid, client=self.client,
                                                                                     entityid=cluster_id)
        response_dict, response.status_code = self.check_response_code_and_return(response,
                                                                                  message="Failed to get cluster detail")
        return response_dict, response.status_code

    def can_fw_update(self, omevv_group_id):
        response: Response[bool] = can_trigger_update.sync_detailed(uuid=self.uuid, client=self.client,
                                                                    json_body=omevv_group_id)
        response_dict = json.loads(response.content.decode("utf-8").replace("'", '"'))
        return response_dict, response.status_code

    def get_firmware_drift_report_by_host_id(self, omevv_group_id, host_id):
        response: Response[Union[ErrorObject, FirmwareDriftResponseModel]] = get_firmware_drift_report_by_host_id. \
            sync_detailed(uuid=self.uuid, client=self.client, gid=omevv_group_id, hid=host_id)
        if response.status_code == 404:
            print("ERROR: The server cannot find the requested resource, check provided OME appliance IP is valid")
            exit(1)
        else:
            response_dict = json.loads(response.content.decode("utf-8").replace("'", '"'))
            return response_dict, response.status_code

    def firmware_update(self,
                        job_name,
                        job_description,
                        reboot_options,
                        checkv_san_health,
                        exit_maintenance_mode,
                        drs_check,
                        maintenance_mode_count_check,
                        evacuate_v_ms,
                        reset_i_drac,
                        delete_jobs_queue,
                        enter_maintenance_mode_option,
                        enter_maintenance_modetimeout,
                        firmware_components,
                        host_id,
                        omevv_group_id
                        ):
        target_host = HostFirmwareComponents(host_id, firmwarecomponents=firmware_components)
        firmware_body = FirmwareUpdateRequest(reboot_options=reboot_options,
                                              # checkv_san_health=checkv_san_health,
                                              exit_maintenance_mode=exit_maintenance_mode,
                                              drs_check=drs_check,
                                              # maintenance_mode_count_check=maintenance_mode_count_check,
                                              evacuate_v_ms=evacuate_v_ms,
                                              reset_i_drac=reset_i_drac,
                                              delete_jobs_queue=delete_jobs_queue,
                                              # enter_maintenance_mode_option=enter_maintenance_mode_option,
                                              enter_maintenance_modetimeout=enter_maintenance_modetimeout,
                                              targets=[target_host])
        if job_name == "":
            job_name = 'vSphere_Host_Host_id(' + str(host_id) + ")_" + str(datetime.datetime.now())
        if job_description == "":
            job_description = 'Initiated via script'
        json_body = UpdateRequest(job_name,
                                  job_description,
                                  firmware=firmware_body,
                                  schedule=Schedule(run_now=True, date_time=datetime.datetime.now()))
        response: Response[Union[ErrorObject, int]] = \
            trigger_update.sync_detailed(uuid=self.uuid, client=self.client, gid=omevv_group_id,
                                         json_body=json_body)
        response_content = json.loads(response.content.decode("utf-8").replace("'", '"'))
        return response.parsed, response_content, response.status_code

    def firmware_update_job_by_id(self, job_id):
        response: Response[Union[ErrorObject, Job]] = \
            get_update_service_job_by_id.sync_detailed(uuid=self.uuid, client=self.client, id=job_id)
        response_dict = json.loads(response.content.decode("utf-8").replace("'", '"'))
        return response_dict, response.status_code


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
    PARSER.add_argument("--host_id", "-hid", type=int, required=True,
                        default=None, help="hid of the host")
    PARSER.add_argument("--reboot_options", "-ro", required=False, default='SAFEREBOOT',
                        help="Reboot host. Supported values are: SAFEREBOOT, FORCEREBOOT, NEXTREBOOT. "
                             "Default=SAFEREBOOT")
    PARSER.add_argument("--exit_maintenance_mode", "-exmm", required=False, default='True',
                        help="Whether you want exits the maintenance mode after firmware update completes(boolean). "
                             "Default = True")
    PARSER.add_argument("--drs_check", "-drs", required=False,
                        default='True', help="Check DRS is enables for the cluster(boolean). Default=True")
    PARSER.add_argument("--evacuate_v_ms", "-evm", required=False,
                        default='True', help="Evacuate powered off and suspended VMs(boolean). Default=True")
    PARSER.add_argument("--reset_i_drac", "-rid", required=False,
                        default='False', help="Reset iDRAC and the perform update(boolean). Default=False")
    PARSER.add_argument("--delete_jobs_queue", "-delj", required=False,
                        default='True', help="Delete job queue and then perform update(boolean). Default=True")
    PARSER.add_argument("--enter_maintenance_modetimeout", "-enmm", required=False,
                        default=60, help="Enter maintenance mode timeout value(int). Default=60mins")
    PARSER.add_argument("--job_name", "-jn", required=False,
                        default="", help="Firmware update name.")
    PARSER.add_argument("--job_description", "-jd", required=False,
                        default="", help="Job description, optional")
    ARGS = PARSER.parse_args()

    if ARGS.ip is not None and ARGS.vcusername is not None and ARGS.vcpassword is not None and ARGS.vcUUID is not None \
            and ARGS.host_id is not None:
        base_url = 'https://{ip}/omevv/GatewayService/v1/'.format(ip=ARGS.ip)
        credential = Credential(username=ARGS.vcusername, password=ARGS.vcpassword)

        # Verifying given host_id is managed by OMEVV
        response_content, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                        vCenterUUID=ARGS.vcUUID).get_managed_host_list()
        if not any(d1.get('id') == ARGS.host_id for d1 in response_content):
            print("ERROR: Provided host_id(" + str(ARGS.host_id) + ") is not managed by OMEVV")
            exit(1)
        print("Host is managed by OMEVV")
        omevv_group_id = next(element for element in response_content if element['id'] == ARGS.host_id)["omevvpGroupId"]

        # Get groupType and consoleEntityId
        response_content, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                        vCenterUUID=ARGS.vcUUID).get_group_detail(omevv_group_id)
        groupType = response_content["groupType"]
        # Checking host is from the cluster group. Fail if the datacenter host is given
        if groupType != "CLUSTER":
            print("ERROR: Provided host_id(" + str(ARGS.host_id) + ") does not belongs to a cluster. Host group type "
                                                                   "is " + str(groupType))
            exit(1)
        consoleEntityId = response_content["consoleEntityId"]
        # Get vSANEnabled status
        response_content, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                        vCenterUUID=ARGS.vcUUID).get_cluster_detail(consoleEntityId)
        # Checking provided host is vSphere host
        if response_content[0]["vsanEnabled"]:
            print("ERROR: Provided host_id(" + str(ARGS.host_id) + ") does not belongs to vSphere cluster")
            exit(1)
        print("Host is a vSphere host")

        # checking no Firmware update is running for the host
        response_content, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                        vCenterUUID=ARGS.vcUUID).can_fw_update(omevv_group_id)
        if status_code == 400:
            print("ERROR: Firmware update job is already running for the cluster or host within a cluster, "
                  "only one firmware update job withing a cluster can run at a time")
            exit(1)

        # Getting the host drift report
        host_compliance, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                       vCenterUUID=ARGS.vcUUID). \
            get_firmware_drift_report_by_host_id(omevv_group_id=omevv_group_id, host_id=ARGS.host_id)
        if status_code == 200:
            if host_compliance["complianceStatus"] != "NonCompliant":
                print("Either the host compliance status is already compliant or Unknown or Not Applicable. Visit "
                      "Baseline Compliance page and verify the host compliance status. Firmware update cannot be "
                      "attempted.")
                exit(1)
            else:
                all_components = host_compliance["hostComplianceReports"][0]["componentCompliances"]
                exclude_components = ["EQUAL", "UNKNOWN"]
                final_components = [d for d in all_components if d['updateAction'] not in exclude_components]
                sourceName_list = [sub['sourceName'] for sub in final_components]
                print("Following component(s) going to be updated:")
                print(*[sub['componentName'] for sub in final_components], sep="\n")
        else:
            print("ERROR: Unable to get the firmware drift for the host.")
            print("Error code: ", host_compliance["errorCode"])
            print("Error Message: ", host_compliance["message"])
            exit(1)
        # Scheduling the firmware update for the host
        job_id, response_content, status_code = FWUpdateWrapper(base_url=base_url,
                                                                vcUsercredential=credential,
                                                                vCenterUUID=ARGS.vcUUID).firmware_update(
            job_name=ARGS.job_name,
            job_description=ARGS.job_description,
            reboot_options=FirmwareUpdateRequestRebootOptions(ARGS.reboot_options),
            drs_check=ARGS.drs_check,
            evacuate_v_ms=ARGS.evacuate_v_ms,
            reset_i_drac=ARGS.reset_i_drac,
            delete_jobs_queue=ARGS.delete_jobs_queue,
            enter_maintenance_modetimeout=ARGS.enter_maintenance_modetimeout,
            exit_maintenance_mode=ARGS.exit_maintenance_mode,
            firmware_components=sourceName_list,
            host_id=ARGS.host_id,
            omevv_group_id=omevv_group_id,
            enter_maintenance_mode_option=FirmwareUpdateRequestEnterMaintenanceModeOption('ENSURE_ACCESSIBILITY'),
            maintenance_mode_count_check=False,
            checkv_san_health=False
        )

        if status_code == 202:
            # Tracking firmware update to until completion.
            time.sleep(60)
            job_detail, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                      vCenterUUID=ARGS.vcUUID). \
                firmware_update_job_by_id(job_id)
            print("Firmware update job has been triggered. Job name is: " + job_detail['jobName'])
            print("Waiting for the job to be completed...")
            if status_code == 200:
                while job_detail['state'] == "RUNNING":
                    time.sleep(30)
                    job_detail, status_code = FWUpdateWrapper(base_url=base_url, vcUsercredential=credential,
                                                              vCenterUUID=ARGS.vcUUID).firmware_update_job_by_id(job_id)
                if job_detail['state'] == "CANCELLED" or job_detail['state'] == "ABORTED":
                    print("Job is either cancelled or aborted")
                if job_detail['state'] == "COMPLETED" and job_detail['lastExecutionHistory'][
                    'statusSummary'] == "SUCCESSFUL":
                    print("Firmware update is completed successfully")
                else:
                    print("ERROR: Firmware update job is failed. Login to vCenter and then OMEVV, then refer the job "
                          "page and Log page for more detail.")
                    print(job_detail)
                    exit(1)
            else:
                print("ERROR: Unable to get the Firmware update job status.")
                print("Error code: ", job_detail["errorCode"])
                print("Error Message: ", job_detail["message"])
                exit(1)
        else:
            print("ERROR: Firmware update job creation failed.")
            print("Error code: ", response_content["errorCode"])
            print("Error Message: ", response_content["message"])
            exit(1)
