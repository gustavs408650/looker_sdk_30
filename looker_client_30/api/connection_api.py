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


class ConnectionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_connections(self, **kwargs):  # noqa: E501
        """Get All Connections  # noqa: E501

        ### Get information about all connections.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_connections(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: list[DBConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.all_connections_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_connections_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_connections_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Connections  # noqa: E501

        ### Get information about all connections.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_connections_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: list[DBConnection]
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
                    " to method all_connections" % key
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
            '/connections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DBConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def all_dialect_infos(self, **kwargs):  # noqa: E501
        """Get All Dialect Infos  # noqa: E501

        ### Get information about all dialects.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_dialect_infos(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: list[DialectInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.all_dialect_infos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_dialect_infos_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_dialect_infos_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Dialect Infos  # noqa: E501

        ### Get information about all dialects.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.all_dialect_infos_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Requested fields.
        :return: list[DialectInfo]
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
                    " to method all_dialect_infos" % key
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
            '/dialect_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DialectInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connection(self, connection_name, **kwargs):  # noqa: E501
        """Get Connection  # noqa: E501

        ### Get information about a connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.connection(connection_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param str fields: Requested fields.
        :return: DBConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.connection_with_http_info(connection_name, **kwargs)  # noqa: E501
        else:
            (data) = self.connection_with_http_info(connection_name, **kwargs)  # noqa: E501
            return data

    def connection_with_http_info(self, connection_name, **kwargs):  # noqa: E501
        """Get Connection  # noqa: E501

        ### Get information about a connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.connection_with_http_info(connection_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param str fields: Requested fields.
        :return: DBConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_name', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_name' is set
        if ('connection_name' not in params or
                params['connection_name'] is None):
            raise ValueError("Missing the required parameter `connection_name` when calling `connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_name' in params:
            path_params['connection_name'] = params['connection_name']  # noqa: E501

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
            '/connections/{connection_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DBConnection',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_connection(self, **kwargs):  # noqa: E501
        """Create Connection  # noqa: E501

        ### Create a connection using the specified configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_connection(async=True)
        >>> result = thread.get()

        :param async bool
        :param DBConnection body: Connection
        :return: DBConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_connection_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_connection_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_connection_with_http_info(self, **kwargs):  # noqa: E501
        """Create Connection  # noqa: E501

        ### Create a connection using the specified configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_connection_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param DBConnection body: Connection
        :return: DBConnection
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
                    " to method create_connection" % key
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
            '/connections', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DBConnection',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_connection(self, connection_name, **kwargs):  # noqa: E501
        """Delete Connection  # noqa: E501

        ### Delete a connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_connection(connection_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_connection_with_http_info(connection_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_connection_with_http_info(connection_name, **kwargs)  # noqa: E501
            return data

    def delete_connection_with_http_info(self, connection_name, **kwargs):  # noqa: E501
        """Delete Connection  # noqa: E501

        ### Delete a connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_connection_with_http_info(connection_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_name' is set
        if ('connection_name' not in params or
                params['connection_name'] is None):
            raise ValueError("Missing the required parameter `connection_name` when calling `delete_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_name' in params:
            path_params['connection_name'] = params['connection_name']  # noqa: E501

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
            '/connections/{connection_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_connection_override(self, connection_name, override_context, **kwargs):  # noqa: E501
        """Delete Connection  # noqa: E501

        ### Delete a connection override.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_connection_override(connection_name, override_context, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param str override_context: Context of connection override (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_connection_override_with_http_info(connection_name, override_context, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_connection_override_with_http_info(connection_name, override_context, **kwargs)  # noqa: E501
            return data

    def delete_connection_override_with_http_info(self, connection_name, override_context, **kwargs):  # noqa: E501
        """Delete Connection  # noqa: E501

        ### Delete a connection override.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_connection_override_with_http_info(connection_name, override_context, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param str override_context: Context of connection override (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_name', 'override_context']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_connection_override" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_name' is set
        if ('connection_name' not in params or
                params['connection_name'] is None):
            raise ValueError("Missing the required parameter `connection_name` when calling `delete_connection_override`")  # noqa: E501
        # verify the required parameter 'override_context' is set
        if ('override_context' not in params or
                params['override_context'] is None):
            raise ValueError("Missing the required parameter `override_context` when calling `delete_connection_override`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_name' in params:
            path_params['connection_name'] = params['connection_name']  # noqa: E501
        if 'override_context' in params:
            path_params['override_context'] = params['override_context']  # noqa: E501

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
            '/connections/{connection_name}/connection_override/{override_context}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_connection(self, connection_name, **kwargs):  # noqa: E501
        """Test Connection  # noqa: E501

        ### Test an existing connection.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_connection(connection_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param list[str] tests: Array of names of tests to run
        :return: list[DBConnectionTestResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.test_connection_with_http_info(connection_name, **kwargs)  # noqa: E501
        else:
            (data) = self.test_connection_with_http_info(connection_name, **kwargs)  # noqa: E501
            return data

    def test_connection_with_http_info(self, connection_name, **kwargs):  # noqa: E501
        """Test Connection  # noqa: E501

        ### Test an existing connection.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_connection_with_http_info(connection_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param list[str] tests: Array of names of tests to run
        :return: list[DBConnectionTestResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_name', 'tests']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_name' is set
        if ('connection_name' not in params or
                params['connection_name'] is None):
            raise ValueError("Missing the required parameter `connection_name` when calling `test_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_name' in params:
            path_params['connection_name'] = params['connection_name']  # noqa: E501

        query_params = []
        if 'tests' in params:
            query_params.append(('tests', params['tests']))  # noqa: E501
            collection_formats['tests'] = 'csv'  # noqa: E501

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
            '/connections/{connection_name}/test', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DBConnectionTestResult]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_connection_config(self, **kwargs):  # noqa: E501
        """Test Connection Configuration  # noqa: E501

        ### Test a connection configuration.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_connection_config(async=True)
        >>> result = thread.get()

        :param async bool
        :param DBConnection body: Connection
        :param list[str] tests: Array of names of tests to run
        :return: list[DBConnectionTestResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.test_connection_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.test_connection_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def test_connection_config_with_http_info(self, **kwargs):  # noqa: E501
        """Test Connection Configuration  # noqa: E501

        ### Test a connection configuration.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_connection_config_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param DBConnection body: Connection
        :param list[str] tests: Array of names of tests to run
        :return: list[DBConnectionTestResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'tests']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_connection_config" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tests' in params:
            query_params.append(('tests', params['tests']))  # noqa: E501
            collection_formats['tests'] = 'csv'  # noqa: E501

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
            '/connections/test', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DBConnectionTestResult]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_connection(self, connection_name, body, **kwargs):  # noqa: E501
        """Update Connection  # noqa: E501

        ### Update a connection using the specified configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_connection(connection_name, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param DBConnection body: Connection (required)
        :return: DBConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_connection_with_http_info(connection_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_connection_with_http_info(connection_name, body, **kwargs)  # noqa: E501
            return data

    def update_connection_with_http_info(self, connection_name, body, **kwargs):  # noqa: E501
        """Update Connection  # noqa: E501

        ### Update a connection using the specified configuration.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_connection_with_http_info(connection_name, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str connection_name: Name of connection (required)
        :param DBConnection body: Connection (required)
        :return: DBConnection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_name', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_name' is set
        if ('connection_name' not in params or
                params['connection_name'] is None):
            raise ValueError("Missing the required parameter `connection_name` when calling `update_connection`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_name' in params:
            path_params['connection_name'] = params['connection_name']  # noqa: E501

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
            '/connections/{connection_name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DBConnection',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
