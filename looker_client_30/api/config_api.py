# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from looker_client_30.api_client import ApiClient


class ConfigApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_legacy_features(self, **kwargs):  # noqa: E501
        """Get All Legacy Features  # noqa: E501

        ### Get all legacy features.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_legacy_features(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[LegacyFeature]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.all_legacy_features_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_legacy_features_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_legacy_features_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Legacy Features  # noqa: E501

        ### Get all legacy features.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_legacy_features_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[LegacyFeature]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_legacy_features" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/legacy_features', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LegacyFeature]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def all_timezones(self, **kwargs):  # noqa: E501
        """Get All Timezones  # noqa: E501

        ### Get a list of timezones that Looker supports (e.g. useful for scheduling tasks).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_timezones(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Timezone]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.all_timezones_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_timezones_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_timezones_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Timezones  # noqa: E501

        ### Get a list of timezones that Looker supports (e.g. useful for scheduling tasks).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_timezones_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Timezone]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_timezones" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/timezones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Timezone]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def backup_configuration(self, **kwargs):  # noqa: E501
        """Get Backup Configuration  # noqa: E501

        ### Get the current Looker internal database backup configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.backup_configuration(async=True)
        >>> result = thread.get()

        :param async bool
        :return: BackupConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.backup_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.backup_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def backup_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """Get Backup Configuration  # noqa: E501

        ### Get the current Looker internal database backup configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.backup_configuration_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: BackupConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method backup_configuration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/backup_configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BackupConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def legacy_feature(self, legacy_feature_id, **kwargs):  # noqa: E501
        """Get Legacy Feature  # noqa: E501

        ### Get information about the legacy feature with a specific id.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.legacy_feature(legacy_feature_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int legacy_feature_id: id of legacy feature (required)
        :return: LegacyFeature
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.legacy_feature_with_http_info(legacy_feature_id, **kwargs)  # noqa: E501
        else:
            (data) = self.legacy_feature_with_http_info(legacy_feature_id, **kwargs)  # noqa: E501
            return data

    def legacy_feature_with_http_info(self, legacy_feature_id, **kwargs):  # noqa: E501
        """Get Legacy Feature  # noqa: E501

        ### Get information about the legacy feature with a specific id.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.legacy_feature_with_http_info(legacy_feature_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int legacy_feature_id: id of legacy feature (required)
        :return: LegacyFeature
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['legacy_feature_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method legacy_feature" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'legacy_feature_id' is set
        if ('legacy_feature_id' not in params or
                params['legacy_feature_id'] is None):
            raise ValueError("Missing the required parameter `legacy_feature_id` when calling `legacy_feature`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'legacy_feature_id' in params:
            path_params['legacy_feature_id'] = params['legacy_feature_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/legacy_features/{legacy_feature_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegacyFeature',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_backup_configuration(self, body, **kwargs):  # noqa: E501
        """Update Backup Configuration  # noqa: E501

        ### Update the Looker internal database backup configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_backup_configuration(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param BackupConfiguration body: Options for Backup Configuration (required)
        :return: BackupConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_backup_configuration_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_backup_configuration_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_backup_configuration_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update Backup Configuration  # noqa: E501

        ### Update the Looker internal database backup configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_backup_configuration_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param BackupConfiguration body: Options for Backup Configuration (required)
        :return: BackupConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_backup_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_backup_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/backup_configuration', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BackupConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_legacy_feature(self, legacy_feature_id, body, **kwargs):  # noqa: E501
        """Update Legacy Feature  # noqa: E501

        ### Update information about the legacy feature with a specific id.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_legacy_feature(legacy_feature_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int legacy_feature_id: id of legacy feature (required)
        :param LegacyFeature body: Legacy Feature (required)
        :return: LegacyFeature
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_legacy_feature_with_http_info(legacy_feature_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_legacy_feature_with_http_info(legacy_feature_id, body, **kwargs)  # noqa: E501
            return data

    def update_legacy_feature_with_http_info(self, legacy_feature_id, body, **kwargs):  # noqa: E501
        """Update Legacy Feature  # noqa: E501

        ### Update information about the legacy feature with a specific id.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_legacy_feature_with_http_info(legacy_feature_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int legacy_feature_id: id of legacy feature (required)
        :param LegacyFeature body: Legacy Feature (required)
        :return: LegacyFeature
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['legacy_feature_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_legacy_feature" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'legacy_feature_id' is set
        if ('legacy_feature_id' not in params or
                params['legacy_feature_id'] is None):
            raise ValueError("Missing the required parameter `legacy_feature_id` when calling `update_legacy_feature`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_legacy_feature`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'legacy_feature_id' in params:
            path_params['legacy_feature_id'] = params['legacy_feature_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/legacy_features/{legacy_feature_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegacyFeature',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_whitelabel_configuration(self, body, **kwargs):  # noqa: E501
        """Update Whitelabel configuration  # noqa: E501

        ### Update the whitelabel configuration   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_whitelabel_configuration(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param WhitelabelConfiguration body: Whitelabel configuration (required)
        :return: WhitelabelConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_whitelabel_configuration_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_whitelabel_configuration_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_whitelabel_configuration_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update Whitelabel configuration  # noqa: E501

        ### Update the whitelabel configuration   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_whitelabel_configuration_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param WhitelabelConfiguration body: Whitelabel configuration (required)
        :return: WhitelabelConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_whitelabel_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_whitelabel_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/whitelabel_configuration', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhitelabelConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def versions(self, **kwargs):  # noqa: E501
        """Get ApiVersion  # noqa: E501

        ### Get information about all API versions supported by this Looker instance.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.versions(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: ApiVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.versions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.versions_with_http_info(**kwargs)  # noqa: E501
            return data

    def versions_with_http_info(self, **kwargs):  # noqa: E501
        """Get ApiVersion  # noqa: E501

        ### Get information about all API versions supported by this Looker instance.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.versions_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: ApiVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method versions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiVersion',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def whitelabel_configuration(self, **kwargs):  # noqa: E501
        """Get Whitelabel configuration  # noqa: E501

        ### This feature is enabled only by special license. ### Gets the whitelabel configuration, which includes hiding documentation links, custom favicon uploading, etc.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.whitelabel_configuration(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: WhitelabelConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.whitelabel_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.whitelabel_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def whitelabel_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """Get Whitelabel configuration  # noqa: E501

        ### This feature is enabled only by special license. ### Gets the whitelabel configuration, which includes hiding documentation links, custom favicon uploading, etc.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.whitelabel_configuration_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: WhitelabelConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method whitelabel_configuration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/whitelabel_configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhitelabelConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
