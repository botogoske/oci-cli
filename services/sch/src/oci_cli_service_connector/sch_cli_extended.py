# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.sch.src.oci_cli_service_connector.generated import serviceconnector_cli

serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_functions_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_logging_source_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_monitoring_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_notifications_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_object_storage_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_streaming_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_functions_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_logging_source_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_monitoring_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_notifications_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_object_storage_target_details.name)
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_streaming_target_details.name)


# Remove create-service-connector-logging-analytics-target-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.create_service_connector_logging_analytics_target_details.name)


# Remove update-service-connector-logging-analytics-target-details from oci sch service-connector
serviceconnector_cli.service_connector_group.commands.pop(serviceconnector_cli.update_service_connector_logging_analytics_target_details.name)
