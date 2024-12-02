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
    "cdn custom-domain update",
)
class Update(AAZCommand):
    """Update a new custom domain within an endpoint.
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/endpoints/{}/customdomains/{}", "2024-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.custom_domain_name = AAZStrArg(
            options=["-n", "--name", "--custom-domain-name"],
            help="Name of the custom domain within an endpoint.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.endpoint_name = AAZStrArg(
            options=["--endpoint-name"],
            help="Name of the endpoint under the profile which is unique globally.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the CDN profile which is unique within the resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.hostname = AAZStrArg(
            options=["--hostname"],
            arg_group="Properties",
            help="The host name of the custom domain. Must be a domain name.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CustomDomainsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CustomDomainsCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CustomDomainsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}",
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
                    "customDomainName", self.ctx.args.custom_domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "endpointName", self.ctx.args.endpoint_name,
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
            _UpdateHelper._build_schema_custom_domain_read(cls._schema_on_200)

            return cls._schema_on_200

    class CustomDomainsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "customDomainName", self.ctx.args.custom_domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "endpointName", self.ctx.args.endpoint_name,
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
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_custom_domain_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("hostName", AAZStrType, ".hostname", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_custom_domain_read = None

    @classmethod
    def _build_schema_custom_domain_read(cls, _schema):
        if cls._schema_custom_domain_read is not None:
            _schema.id = cls._schema_custom_domain_read.id
            _schema.name = cls._schema_custom_domain_read.name
            _schema.properties = cls._schema_custom_domain_read.properties
            _schema.system_data = cls._schema_custom_domain_read.system_data
            _schema.type = cls._schema_custom_domain_read.type
            return

        cls._schema_custom_domain_read = _schema_custom_domain_read = AAZObjectType()

        custom_domain_read = _schema_custom_domain_read
        custom_domain_read.id = AAZStrType(
            flags={"read_only": True},
        )
        custom_domain_read.name = AAZStrType(
            flags={"read_only": True},
        )
        custom_domain_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        custom_domain_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        custom_domain_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_custom_domain_read.properties
        properties.custom_https_parameters = AAZObjectType(
            serialized_name="customHttpsParameters",
        )
        properties.custom_https_provisioning_state = AAZStrType(
            serialized_name="customHttpsProvisioningState",
            flags={"read_only": True},
        )
        properties.custom_https_provisioning_substate = AAZStrType(
            serialized_name="customHttpsProvisioningSubstate",
            flags={"read_only": True},
        )
        properties.host_name = AAZStrType(
            serialized_name="hostName",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_state = AAZStrType(
            serialized_name="resourceState",
            flags={"read_only": True},
        )
        properties.validation_data = AAZStrType(
            serialized_name="validationData",
        )

        custom_https_parameters = _schema_custom_domain_read.properties.custom_https_parameters
        custom_https_parameters.certificate_source = AAZStrType(
            serialized_name="certificateSource",
            flags={"required": True},
        )
        custom_https_parameters.minimum_tls_version = AAZStrType(
            serialized_name="minimumTlsVersion",
        )
        custom_https_parameters.protocol_type = AAZStrType(
            serialized_name="protocolType",
            flags={"required": True},
        )

        disc_azure_key_vault = _schema_custom_domain_read.properties.custom_https_parameters.discriminate_by("certificate_source", "AzureKeyVault")
        disc_azure_key_vault.certificate_source_parameters = AAZObjectType(
            serialized_name="certificateSourceParameters",
            flags={"required": True},
        )

        certificate_source_parameters = _schema_custom_domain_read.properties.custom_https_parameters.discriminate_by("certificate_source", "AzureKeyVault").certificate_source_parameters
        certificate_source_parameters.delete_rule = AAZStrType(
            serialized_name="deleteRule",
            flags={"required": True},
        )
        certificate_source_parameters.resource_group_name = AAZStrType(
            serialized_name="resourceGroupName",
            flags={"required": True},
        )
        certificate_source_parameters.secret_name = AAZStrType(
            serialized_name="secretName",
            flags={"required": True},
        )
        certificate_source_parameters.secret_version = AAZStrType(
            serialized_name="secretVersion",
        )
        certificate_source_parameters.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
            flags={"required": True},
        )
        certificate_source_parameters.type_name = AAZStrType(
            serialized_name="typeName",
            flags={"required": True},
        )
        certificate_source_parameters.update_rule = AAZStrType(
            serialized_name="updateRule",
            flags={"required": True},
        )
        certificate_source_parameters.vault_name = AAZStrType(
            serialized_name="vaultName",
            flags={"required": True},
        )

        disc_cdn = _schema_custom_domain_read.properties.custom_https_parameters.discriminate_by("certificate_source", "Cdn")
        disc_cdn.certificate_source_parameters = AAZObjectType(
            serialized_name="certificateSourceParameters",
            flags={"required": True},
        )

        certificate_source_parameters = _schema_custom_domain_read.properties.custom_https_parameters.discriminate_by("certificate_source", "Cdn").certificate_source_parameters
        certificate_source_parameters.certificate_type = AAZStrType(
            serialized_name="certificateType",
            flags={"required": True},
        )
        certificate_source_parameters.type_name = AAZStrType(
            serialized_name="typeName",
            flags={"required": True},
        )

        system_data = _schema_custom_domain_read.system_data
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

        _schema.id = cls._schema_custom_domain_read.id
        _schema.name = cls._schema_custom_domain_read.name
        _schema.properties = cls._schema_custom_domain_read.properties
        _schema.system_data = cls._schema_custom_domain_read.system_data
        _schema.type = cls._schema_custom_domain_read.type


__all__ = ["Update"]
