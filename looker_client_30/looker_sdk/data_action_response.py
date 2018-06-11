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

from looker_client_30.looker_sdk.validation_error import ValidationError  # noqa: F401,E501


class DataActionResponse(object):
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
        'webhook_id': 'str',
        'success': 'bool',
        'refresh_query': 'bool',
        'validation_errors': 'ValidationError',
        'message': 'str'
    }

    attribute_map = {
        'webhook_id': 'webhook_id',
        'success': 'success',
        'refresh_query': 'refresh_query',
        'validation_errors': 'validation_errors',
        'message': 'message'
    }

    def __init__(self, webhook_id=None, success=None, refresh_query=None, validation_errors=None, message=None):  # noqa: E501
        """DataActionResponse - a model defined in Swagger"""  # noqa: E501

        self._webhook_id = None
        self._success = None
        self._refresh_query = None
        self._validation_errors = None
        self._message = None
        self.discriminator = None

        if webhook_id is not None:
            self.webhook_id = webhook_id
        if success is not None:
            self.success = success
        if refresh_query is not None:
            self.refresh_query = refresh_query
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if message is not None:
            self.message = message

    @property
    def webhook_id(self):
        """Gets the webhook_id of this DataActionResponse.  # noqa: E501

        ID of the webhook event that sent this data action. In some error conditions, this may be null.  # noqa: E501

        :return: The webhook_id of this DataActionResponse.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this DataActionResponse.

        ID of the webhook event that sent this data action. In some error conditions, this may be null.  # noqa: E501

        :param webhook_id: The webhook_id of this DataActionResponse.  # noqa: E501
        :type: str
        """

        self._webhook_id = webhook_id

    @property
    def success(self):
        """Gets the success of this DataActionResponse.  # noqa: E501

        Whether the data action was successful.  # noqa: E501

        :return: The success of this DataActionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DataActionResponse.

        Whether the data action was successful.  # noqa: E501

        :param success: The success of this DataActionResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def refresh_query(self):
        """Gets the refresh_query of this DataActionResponse.  # noqa: E501

        When true, indicates that the client should refresh (rerun) the source query because the data may have been changed by the action.  # noqa: E501

        :return: The refresh_query of this DataActionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_query

    @refresh_query.setter
    def refresh_query(self, refresh_query):
        """Sets the refresh_query of this DataActionResponse.

        When true, indicates that the client should refresh (rerun) the source query because the data may have been changed by the action.  # noqa: E501

        :param refresh_query: The refresh_query of this DataActionResponse.  # noqa: E501
        :type: bool
        """

        self._refresh_query = refresh_query

    @property
    def validation_errors(self):
        """Gets the validation_errors of this DataActionResponse.  # noqa: E501

        Validation errors returned by the data action server.  # noqa: E501

        :return: The validation_errors of this DataActionResponse.  # noqa: E501
        :rtype: ValidationError
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this DataActionResponse.

        Validation errors returned by the data action server.  # noqa: E501

        :param validation_errors: The validation_errors of this DataActionResponse.  # noqa: E501
        :type: ValidationError
        """

        self._validation_errors = validation_errors

    @property
    def message(self):
        """Gets the message of this DataActionResponse.  # noqa: E501

        Optional message returned by the data action server describing the state of the action that took place. This can be used to implement custom failure messages. If a failure is related to a particular form field, the server should send back a validation error instead. The Looker web UI does not currently display any message if the action indicates 'success', but may do so in the future.  # noqa: E501

        :return: The message of this DataActionResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DataActionResponse.

        Optional message returned by the data action server describing the state of the action that took place. This can be used to implement custom failure messages. If a failure is related to a particular form field, the server should send back a validation error instead. The Looker web UI does not currently display any message if the action indicates 'success', but may do so in the future.  # noqa: E501

        :param message: The message of this DataActionResponse.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, DataActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other