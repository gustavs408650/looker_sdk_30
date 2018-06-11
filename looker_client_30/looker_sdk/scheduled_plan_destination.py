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


class ScheduledPlanDestination(object):
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
        'scheduled_plan_id': 'int',
        'format': 'str',
        'apply_formatting': 'bool',
        'apply_vis': 'bool',
        'address': 'str',
        'looker_recipient': 'bool',
        'type': 'str',
        'parameters': 'str',
        'secret_parameters': 'str',
        'message': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'scheduled_plan_id': 'scheduled_plan_id',
        'format': 'format',
        'apply_formatting': 'apply_formatting',
        'apply_vis': 'apply_vis',
        'address': 'address',
        'looker_recipient': 'looker_recipient',
        'type': 'type',
        'parameters': 'parameters',
        'secret_parameters': 'secret_parameters',
        'message': 'message',
        'can': 'can'
    }

    def __init__(self, id=None, scheduled_plan_id=None, format=None, apply_formatting=None, apply_vis=None, address=None, looker_recipient=None, type=None, parameters=None, secret_parameters=None, message=None, can=None):  # noqa: E501
        """ScheduledPlanDestination - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._scheduled_plan_id = None
        self._format = None
        self._apply_formatting = None
        self._apply_vis = None
        self._address = None
        self._looker_recipient = None
        self._type = None
        self._parameters = None
        self._secret_parameters = None
        self._message = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if scheduled_plan_id is not None:
            self.scheduled_plan_id = scheduled_plan_id
        if format is not None:
            self.format = format
        if apply_formatting is not None:
            self.apply_formatting = apply_formatting
        if apply_vis is not None:
            self.apply_vis = apply_vis
        if address is not None:
            self.address = address
        if looker_recipient is not None:
            self.looker_recipient = looker_recipient
        if type is not None:
            self.type = type
        if parameters is not None:
            self.parameters = parameters
        if secret_parameters is not None:
            self.secret_parameters = secret_parameters
        if message is not None:
            self.message = message
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this ScheduledPlanDestination.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this ScheduledPlanDestination.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledPlanDestination.

        Unique Id  # noqa: E501

        :param id: The id of this ScheduledPlanDestination.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def scheduled_plan_id(self):
        """Gets the scheduled_plan_id of this ScheduledPlanDestination.  # noqa: E501

        Id of a scheduled plan you own  # noqa: E501

        :return: The scheduled_plan_id of this ScheduledPlanDestination.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_plan_id

    @scheduled_plan_id.setter
    def scheduled_plan_id(self, scheduled_plan_id):
        """Sets the scheduled_plan_id of this ScheduledPlanDestination.

        Id of a scheduled plan you own  # noqa: E501

        :param scheduled_plan_id: The scheduled_plan_id of this ScheduledPlanDestination.  # noqa: E501
        :type: int
        """

        self._scheduled_plan_id = scheduled_plan_id

    @property
    def format(self):
        """Gets the format of this ScheduledPlanDestination.  # noqa: E501

        Format requested by the given destination (i.e. PDF, etc.)  # noqa: E501

        :return: The format of this ScheduledPlanDestination.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ScheduledPlanDestination.

        Format requested by the given destination (i.e. PDF, etc.)  # noqa: E501

        :param format: The format of this ScheduledPlanDestination.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def apply_formatting(self):
        """Gets the apply_formatting of this ScheduledPlanDestination.  # noqa: E501

        Are values formatted? (containing currency symbols, digit separators, etc.  # noqa: E501

        :return: The apply_formatting of this ScheduledPlanDestination.  # noqa: E501
        :rtype: bool
        """
        return self._apply_formatting

    @apply_formatting.setter
    def apply_formatting(self, apply_formatting):
        """Sets the apply_formatting of this ScheduledPlanDestination.

        Are values formatted? (containing currency symbols, digit separators, etc.  # noqa: E501

        :param apply_formatting: The apply_formatting of this ScheduledPlanDestination.  # noqa: E501
        :type: bool
        """

        self._apply_formatting = apply_formatting

    @property
    def apply_vis(self):
        """Gets the apply_vis of this ScheduledPlanDestination.  # noqa: E501

        Whether visualization options are applied to the results.  # noqa: E501

        :return: The apply_vis of this ScheduledPlanDestination.  # noqa: E501
        :rtype: bool
        """
        return self._apply_vis

    @apply_vis.setter
    def apply_vis(self, apply_vis):
        """Sets the apply_vis of this ScheduledPlanDestination.

        Whether visualization options are applied to the results.  # noqa: E501

        :param apply_vis: The apply_vis of this ScheduledPlanDestination.  # noqa: E501
        :type: bool
        """

        self._apply_vis = apply_vis

    @property
    def address(self):
        """Gets the address of this ScheduledPlanDestination.  # noqa: E501

        Address for recipient. For email e.g. 'user@example.com'. For webhooks e.g. 'https://domain/path'. For Amazon S3 e.g. 's3://bucket-name/path/'. For SFTP e.g. 'sftp://host-name/path/'.   # noqa: E501

        :return: The address of this ScheduledPlanDestination.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ScheduledPlanDestination.

        Address for recipient. For email e.g. 'user@example.com'. For webhooks e.g. 'https://domain/path'. For Amazon S3 e.g. 's3://bucket-name/path/'. For SFTP e.g. 'sftp://host-name/path/'.   # noqa: E501

        :param address: The address of this ScheduledPlanDestination.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def looker_recipient(self):
        """Gets the looker_recipient of this ScheduledPlanDestination.  # noqa: E501

        Whether the recipient is a Looker user on the current instance (only applicable for email recipients)  # noqa: E501

        :return: The looker_recipient of this ScheduledPlanDestination.  # noqa: E501
        :rtype: bool
        """
        return self._looker_recipient

    @looker_recipient.setter
    def looker_recipient(self, looker_recipient):
        """Sets the looker_recipient of this ScheduledPlanDestination.

        Whether the recipient is a Looker user on the current instance (only applicable for email recipients)  # noqa: E501

        :param looker_recipient: The looker_recipient of this ScheduledPlanDestination.  # noqa: E501
        :type: bool
        """

        self._looker_recipient = looker_recipient

    @property
    def type(self):
        """Gets the type of this ScheduledPlanDestination.  # noqa: E501

        Type of the address ('email', 'webhook', 's3', or 'sftp')  # noqa: E501

        :return: The type of this ScheduledPlanDestination.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScheduledPlanDestination.

        Type of the address ('email', 'webhook', 's3', or 'sftp')  # noqa: E501

        :param type: The type of this ScheduledPlanDestination.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def parameters(self):
        """Gets the parameters of this ScheduledPlanDestination.  # noqa: E501

        JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username.  # noqa: E501

        :return: The parameters of this ScheduledPlanDestination.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ScheduledPlanDestination.

        JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username.  # noqa: E501

        :param parameters: The parameters of this ScheduledPlanDestination.  # noqa: E501
        :type: str
        """

        self._parameters = parameters

    @property
    def secret_parameters(self):
        """Gets the secret_parameters of this ScheduledPlanDestination.  # noqa: E501

        (Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password.  # noqa: E501

        :return: The secret_parameters of this ScheduledPlanDestination.  # noqa: E501
        :rtype: str
        """
        return self._secret_parameters

    @secret_parameters.setter
    def secret_parameters(self, secret_parameters):
        """Sets the secret_parameters of this ScheduledPlanDestination.

        (Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password.  # noqa: E501

        :param secret_parameters: The secret_parameters of this ScheduledPlanDestination.  # noqa: E501
        :type: str
        """

        self._secret_parameters = secret_parameters

    @property
    def message(self):
        """Gets the message of this ScheduledPlanDestination.  # noqa: E501

        Optional message to be included in scheduled emails  # noqa: E501

        :return: The message of this ScheduledPlanDestination.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ScheduledPlanDestination.

        Optional message to be included in scheduled emails  # noqa: E501

        :param message: The message of this ScheduledPlanDestination.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def can(self):
        """Gets the can of this ScheduledPlanDestination.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this ScheduledPlanDestination.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this ScheduledPlanDestination.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this ScheduledPlanDestination.  # noqa: E501
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
        if not isinstance(other, ScheduledPlanDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
