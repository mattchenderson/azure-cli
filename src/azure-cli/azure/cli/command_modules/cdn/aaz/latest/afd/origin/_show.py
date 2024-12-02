# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "afd origin show",
)
class Show(AAZCommand):
    """Get an existing origin within an origin group.
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/origingroups/{}/origins/{}", "2024-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.origin_group_name = AAZStrArg(
            options=["--origin-group-name"],
            help="Name of the origin group which is unique within the profile.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.origin_name = AAZStrArg(
            options=["-n", "--name", "--origin-name"],
            help="Name of the origin which is unique within the profile.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AFDOriginsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AFDOriginsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/originGroups/{originGroupName}/origins/{originName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "originGroupName", self.ctx.args.origin_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "originName", self.ctx.args.origin_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.azure_origin = AAZObjectType(
                serialized_name="azureOrigin",
            )
            _ShowHelper._build_schema_resource_reference_read(properties.azure_origin)
            properties.deployment_status = AAZStrType(
                serialized_name="deploymentStatus",
                flags={"read_only": True},
            )
            properties.enabled_state = AAZStrType(
                serialized_name="enabledState",
            )
            properties.enforce_certificate_name_check = AAZBoolType(
                serialized_name="enforceCertificateNameCheck",
            )
            properties.host_name = AAZStrType(
                serialized_name="hostName",
                flags={"required": True},
            )
            properties.http_port = AAZIntType(
                serialized_name="httpPort",
            )
            properties.https_port = AAZIntType(
                serialized_name="httpsPort",
            )
            properties.origin_group_name = AAZStrType(
                serialized_name="originGroupName",
                flags={"read_only": True},
            )
            properties.origin_host_header = AAZStrType(
                serialized_name="originHostHeader",
            )
            properties.priority = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.shared_private_link_resource = AAZObjectType(
                serialized_name="sharedPrivateLinkResource",
            )
            properties.weight = AAZIntType()

            shared_private_link_resource = cls._schema_on_200.properties.shared_private_link_resource
            shared_private_link_resource.group_id = AAZStrType(
                serialized_name="groupId",
            )
            shared_private_link_resource.private_link = AAZObjectType(
                serialized_name="privateLink",
            )
            _ShowHelper._build_schema_resource_reference_read(shared_private_link_resource.private_link)
            shared_private_link_resource.private_link_location = AAZStrType(
                serialized_name="privateLinkLocation",
            )
            shared_private_link_resource.request_message = AAZStrType(
                serialized_name="requestMessage",
            )
            shared_private_link_resource.status = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_resource_reference_read = None

    @classmethod
    def _build_schema_resource_reference_read(cls, _schema):
        if cls._schema_resource_reference_read is not None:
            _schema.id = cls._schema_resource_reference_read.id
            return

        cls._schema_resource_reference_read = _schema_resource_reference_read = AAZObjectType()

        resource_reference_read = _schema_resource_reference_read
        resource_reference_read.id = AAZStrType()

        _schema.id = cls._schema_resource_reference_read.id


__all__ = ["Show"]
