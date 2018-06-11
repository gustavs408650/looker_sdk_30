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

from looker_client_30.looker_sdk.models_not_validated import ModelsNotValidated  # noqa: F401,E501
from looker_client_30.looker_sdk.project_error import ProjectError  # noqa: F401,E501


class ProjectValidation(object):
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
        'errors': 'list[ProjectError]',
        'project_digest': 'str',
        'models_not_validated': 'list[ModelsNotValidated]'
    }

    attribute_map = {
        'errors': 'errors',
        'project_digest': 'project_digest',
        'models_not_validated': 'models_not_validated'
    }

    def __init__(self, errors=None, project_digest=None, models_not_validated=None):  # noqa: E501
        """ProjectValidation - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._project_digest = None
        self._models_not_validated = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if project_digest is not None:
            self.project_digest = project_digest
        if models_not_validated is not None:
            self.models_not_validated = models_not_validated

    @property
    def errors(self):
        """Gets the errors of this ProjectValidation.  # noqa: E501

        A list of project errors  # noqa: E501

        :return: The errors of this ProjectValidation.  # noqa: E501
        :rtype: list[ProjectError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ProjectValidation.

        A list of project errors  # noqa: E501

        :param errors: The errors of this ProjectValidation.  # noqa: E501
        :type: list[ProjectError]
        """

        self._errors = errors

    @property
    def project_digest(self):
        """Gets the project_digest of this ProjectValidation.  # noqa: E501

        A hash value computed from the project's current state  # noqa: E501

        :return: The project_digest of this ProjectValidation.  # noqa: E501
        :rtype: str
        """
        return self._project_digest

    @project_digest.setter
    def project_digest(self, project_digest):
        """Sets the project_digest of this ProjectValidation.

        A hash value computed from the project's current state  # noqa: E501

        :param project_digest: The project_digest of this ProjectValidation.  # noqa: E501
        :type: str
        """

        self._project_digest = project_digest

    @property
    def models_not_validated(self):
        """Gets the models_not_validated of this ProjectValidation.  # noqa: E501

        A list of models which were not fully validated  # noqa: E501

        :return: The models_not_validated of this ProjectValidation.  # noqa: E501
        :rtype: list[ModelsNotValidated]
        """
        return self._models_not_validated

    @models_not_validated.setter
    def models_not_validated(self, models_not_validated):
        """Sets the models_not_validated of this ProjectValidation.

        A list of models which were not fully validated  # noqa: E501

        :param models_not_validated: The models_not_validated of this ProjectValidation.  # noqa: E501
        :type: list[ModelsNotValidated]
        """

        self._models_not_validated = models_not_validated

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
        if not isinstance(other, ProjectValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
