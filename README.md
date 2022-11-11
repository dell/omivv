## OMEVVP Overview

The integration of OpenManage Integration for VMware vCenter allows IT administrators dramatically improved control over their physical environment. An integrated easy-to-use graphical user interface (GUI) is provided to manage physical servers for hardware monitoring, update of server BIOS and firmware and hypervisor deployment on bare-metal Dell™ PowerEdge™ servers. OpenManage Enterprise Integration for VMware vCenter (OMEVV) is the successor to the OpenManage Integration for VMware vCenter (OMIVV).

This ability is now extended to OpenManage Enterprise (OME) users through the OMEVV plugin and provides new features in the administration portal compared to OMIVV. The OMEVV plugin can be installed on an existing instance of OME and can be registered with vCenter using the VMware remote plug in architecture , allowing for easier use with remote or cloudhosted vCenters. The OMEVV plug-in offers VMware users additional security and performance benefits through the OMEVV backend.

## Learning more about OMEVVP

For complete information concerning OMEVVP, see the documents at https://www.dell.com/support/manuals/en-al/openmanage-enterprise-integration-vmware-vcenter/omevv_rn_1.0/dell-openmanage-enterprise-integration-for-vmware-vcenter-plugin-version-1.0?guid=guid-8f6e7b28-1c4b-4833-9959-db40f9f476bc&lang=en-us .

For an overview of the OPENAPI compliant REST API for OMEVVP, see https://developer.dell.com/apis/14348/versions/1.0/docs/Getting%20Started/Access-product-documentation.md

To migrate from OMIVV to OMEVV please additionally see the whitepaper at:
https://dl.dell.com/content/manual179056-migrating-from-omivv-to-omevv.pdf?language=en-us

## OMEVVP REST API with OPENAPI based Scripting Library

This GitHub library contains example Python and PowerShell scripts that illustrate the usage of the iDRAC REST API with Redfish to perform the following actions:

vCenter operations
*	Register OMEVVP with vCenter (Webclient and PHA)
*	Un-register OMEVVP with vCenter
*	Update OMEVVP registration with VLCM extension.

OMEVV Management Compliance operations
*	Retrive management compliance of vCenter infrastructure hosts.
*	Identify and remediate licenses on unsupported hosts.
*	Fix SNMP trap destination setting on non-compliant servers.
*	Include vCenter server device for management using OMEVV 
*	Exclude/Remove vCenter server device from management using OMEVV 

Device Monitoring operations
*	Get server hardware inventory
*	Get server firmware inventory

Device Management operations
*	Perform a single server device firmware update (Standalone or clustered)
*	Perform cluster aware firmware update

Compatibility
*	PowerEdge 12G/13G/14G/15G servers
*	Minimum iDRAC 7/8 FW 2.40.40.40, iDRAC9 FW 3.00.00.00
*	Python 3.x
*	OME 3.9
*	vCenter 7.0U2+
*	ESXI 6.7U3+
*	OME Enterprise Adv+ licence on server nodes.

## Support

Please note this code is provided as-is and currently not supported by Dell EMC.

## Report problems or provide feedback

If you run into any problems or would like to provide feedback, please open an issue here https://github.com/dell/omivv/issues 
