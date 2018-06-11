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


class UserPublic(object):
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
        'id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'display_name': 'str',
        'avatar_url': 'str',
        'url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'display_name': 'display_name',
        'avatar_url': 'avatar_url',
        'url': 'url',
        'can': 'can'
    }

    def __init__(self, id=None, first_name=None, last_name=None, display_name=None, avatar_url=None, url=None, can=None):  # noqa: E501
        """UserPublic - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._display_name = None
        self._avatar_url = None
        self._url = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if display_name is not None:
            self.display_name = display_name
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if url is not None:
            self.url = url
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this UserPublic.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this UserPublic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserPublic.

        Unique Id  # noqa: E501

        :param id: The id of this UserPublic.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this UserPublic.  # noqa: E501

        First Name  # noqa: E501

        :return: The first_name of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserPublic.

        First Name  # noqa: E501

        :param first_name: The first_name of this UserPublic.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserPublic.  # noqa: E501

        Last Name  # noqa: E501

        :return: The last_name of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserPublic.

        Last Name  # noqa: E501

        :param last_name: The last_name of this UserPublic.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def display_name(self):
        """Gets the display_name of this UserPublic.  # noqa: E501

        Full name for display (available only if both first_name and last_name are set)  # noqa: E501

        :return: The display_name of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserPublic.

        Full name for display (available only if both first_name and last_name are set)  # noqa: E501

        :param display_name: The display_name of this UserPublic.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this UserPublic.  # noqa: E501

        URL for the avatar image (may be generic)  # noqa: E501

        :return: The avatar_url of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this UserPublic.

        URL for the avatar image (may be generic)  # noqa: E501

        :param avatar_url: The avatar_url of this UserPublic.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def url(self):
        """Gets the url of this UserPublic.  # noqa: E501

        Link to get this item  # noqa: E501

        :return: The url of this UserPublic.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UserPublic.

        Link to get this item  # noqa: E501

        :param url: The url of this UserPublic.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """Gets the can of this UserPublic.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this UserPublic.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this UserPublic.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this UserPublic.  # noqa: E501
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
        if not isinstance(other, UserPublic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
