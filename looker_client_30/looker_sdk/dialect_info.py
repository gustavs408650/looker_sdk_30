# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from looker_client_30.looker_sdk.dialect_info_options import DialectInfoOptions  # noqa: F401,E501


class DialectInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'label': 'str',
        'label_for_database_equivalent': 'str',
        'default_port': 'str',
        'default_max_connections': 'str',
        'supported_options': 'DialectInfoOptions',
        'installed': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'label_for_database_equivalent': 'label_for_database_equivalent',
        'default_port': 'default_port',
        'default_max_connections': 'default_max_connections',
        'supported_options': 'supported_options',
        'installed': 'installed',
        'can': 'can'
    }

    def __init__(self, name=None, label=None, label_for_database_equivalent=None, default_port=None, default_max_connections=None, supported_options=None, installed=None, can=None):  # noqa: E501
        """DialectInfo - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._label = None
        self._label_for_database_equivalent = None
        self._default_port = None
        self._default_max_connections = None
        self._supported_options = None
        self._installed = None
        self._can = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if label_for_database_equivalent is not None:
            self.label_for_database_equivalent = label_for_database_equivalent
        if default_port is not None:
            self.default_port = default_port
        if default_max_connections is not None:
            self.default_max_connections = default_max_connections
        if supported_options is not None:
            self.supported_options = supported_options
        if installed is not None:
            self.installed = installed
        if can is not None:
            self.can = can

    @property
    def name(self):
        """Gets the name of this DialectInfo.  # noqa: E501

        The name of the dialect  # noqa: E501

        :return: The name of this DialectInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DialectInfo.

        The name of the dialect  # noqa: E501

        :param name: The name of this DialectInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this DialectInfo.  # noqa: E501

        The human-readable label of the connection  # noqa: E501

        :return: The label of this DialectInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DialectInfo.

        The human-readable label of the connection  # noqa: E501

        :param label: The label of this DialectInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def label_for_database_equivalent(self):
        """Gets the label_for_database_equivalent of this DialectInfo.  # noqa: E501

        What the dialect calls the equivalent of a normal SQL table  # noqa: E501

        :return: The label_for_database_equivalent of this DialectInfo.  # noqa: E501
        :rtype: str
        """
        return self._label_for_database_equivalent

    @label_for_database_equivalent.setter
    def label_for_database_equivalent(self, label_for_database_equivalent):
        """Sets the label_for_database_equivalent of this DialectInfo.

        What the dialect calls the equivalent of a normal SQL table  # noqa: E501

        :param label_for_database_equivalent: The label_for_database_equivalent of this DialectInfo.  # noqa: E501
        :type: str
        """

        self._label_for_database_equivalent = label_for_database_equivalent

    @property
    def default_port(self):
        """Gets the default_port of this DialectInfo.  # noqa: E501

        Default port number  # noqa: E501

        :return: The default_port of this DialectInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_port

    @default_port.setter
    def default_port(self, default_port):
        """Sets the default_port of this DialectInfo.

        Default port number  # noqa: E501

        :param default_port: The default_port of this DialectInfo.  # noqa: E501
        :type: str
        """

        self._default_port = default_port

    @property
    def default_max_connections(self):
        """Gets the default_max_connections of this DialectInfo.  # noqa: E501

        Default number max connections  # noqa: E501

        :return: The default_max_connections of this DialectInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_max_connections

    @default_max_connections.setter
    def default_max_connections(self, default_max_connections):
        """Sets the default_max_connections of this DialectInfo.

        Default number max connections  # noqa: E501

        :param default_max_connections: The default_max_connections of this DialectInfo.  # noqa: E501
        :type: str
        """

        self._default_max_connections = default_max_connections

    @property
    def supported_options(self):
        """Gets the supported_options of this DialectInfo.  # noqa: E501

        Option support details  # noqa: E501

        :return: The supported_options of this DialectInfo.  # noqa: E501
        :rtype: DialectInfoOptions
        """
        return self._supported_options

    @supported_options.setter
    def supported_options(self, supported_options):
        """Sets the supported_options of this DialectInfo.

        Option support details  # noqa: E501

        :param supported_options: The supported_options of this DialectInfo.  # noqa: E501
        :type: DialectInfoOptions
        """

        self._supported_options = supported_options

    @property
    def installed(self):
        """Gets the installed of this DialectInfo.  # noqa: E501

        Is the supporting driver installed  # noqa: E501

        :return: The installed of this DialectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this DialectInfo.

        Is the supporting driver installed  # noqa: E501

        :param installed: The installed of this DialectInfo.  # noqa: E501
        :type: bool
        """

        self._installed = installed

    @property
    def can(self):
        """Gets the can of this DialectInfo.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this DialectInfo.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this DialectInfo.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this DialectInfo.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DialectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
