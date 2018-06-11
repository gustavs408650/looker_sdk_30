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


class RenderTask(object):
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
        'id': 'str',
        'created_at': 'str',
        'finalized_at': 'str',
        'status': 'str',
        'status_detail': 'str',
        'user_id': 'int',
        'runtime': 'float',
        'query_runtime': 'float',
        'render_runtime': 'float',
        'result_format': 'str',
        'look_id': 'int',
        'dashboard_id': 'int',
        'lookml_dashboard_id': 'str',
        'query_id': 'int',
        'width': 'int',
        'height': 'int',
        'dashboard_style': 'str',
        'dashboard_filters': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'finalized_at': 'finalized_at',
        'status': 'status',
        'status_detail': 'status_detail',
        'user_id': 'user_id',
        'runtime': 'runtime',
        'query_runtime': 'query_runtime',
        'render_runtime': 'render_runtime',
        'result_format': 'result_format',
        'look_id': 'look_id',
        'dashboard_id': 'dashboard_id',
        'lookml_dashboard_id': 'lookml_dashboard_id',
        'query_id': 'query_id',
        'width': 'width',
        'height': 'height',
        'dashboard_style': 'dashboard_style',
        'dashboard_filters': 'dashboard_filters',
        'can': 'can'
    }

    def __init__(self, id=None, created_at=None, finalized_at=None, status=None, status_detail=None, user_id=None, runtime=None, query_runtime=None, render_runtime=None, result_format=None, look_id=None, dashboard_id=None, lookml_dashboard_id=None, query_id=None, width=None, height=None, dashboard_style=None, dashboard_filters=None, can=None):  # noqa: E501
        """RenderTask - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._finalized_at = None
        self._status = None
        self._status_detail = None
        self._user_id = None
        self._runtime = None
        self._query_runtime = None
        self._render_runtime = None
        self._result_format = None
        self._look_id = None
        self._dashboard_id = None
        self._lookml_dashboard_id = None
        self._query_id = None
        self._width = None
        self._height = None
        self._dashboard_style = None
        self._dashboard_filters = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if finalized_at is not None:
            self.finalized_at = finalized_at
        if status is not None:
            self.status = status
        if status_detail is not None:
            self.status_detail = status_detail
        if user_id is not None:
            self.user_id = user_id
        if runtime is not None:
            self.runtime = runtime
        if query_runtime is not None:
            self.query_runtime = query_runtime
        if render_runtime is not None:
            self.render_runtime = render_runtime
        if result_format is not None:
            self.result_format = result_format
        if look_id is not None:
            self.look_id = look_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if lookml_dashboard_id is not None:
            self.lookml_dashboard_id = lookml_dashboard_id
        if query_id is not None:
            self.query_id = query_id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if dashboard_style is not None:
            self.dashboard_style = dashboard_style
        if dashboard_filters is not None:
            self.dashboard_filters = dashboard_filters
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this RenderTask.  # noqa: E501

        Id of this render task  # noqa: E501

        :return: The id of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RenderTask.

        Id of this render task  # noqa: E501

        :param id: The id of this RenderTask.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this RenderTask.  # noqa: E501

        Date/Time render task was created  # noqa: E501

        :return: The created_at of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RenderTask.

        Date/Time render task was created  # noqa: E501

        :param created_at: The created_at of this RenderTask.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def finalized_at(self):
        """Gets the finalized_at of this RenderTask.  # noqa: E501

        Date/Time render task was completed  # noqa: E501

        :return: The finalized_at of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._finalized_at

    @finalized_at.setter
    def finalized_at(self, finalized_at):
        """Sets the finalized_at of this RenderTask.

        Date/Time render task was completed  # noqa: E501

        :param finalized_at: The finalized_at of this RenderTask.  # noqa: E501
        :type: str
        """

        self._finalized_at = finalized_at

    @property
    def status(self):
        """Gets the status of this RenderTask.  # noqa: E501

        Render task status: enqueued_for_query, querying, enqueued_for_render, rendering, success, failure  # noqa: E501

        :return: The status of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RenderTask.

        Render task status: enqueued_for_query, querying, enqueued_for_render, rendering, success, failure  # noqa: E501

        :param status: The status of this RenderTask.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this RenderTask.  # noqa: E501

        Additional information about the current status  # noqa: E501

        :return: The status_detail of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this RenderTask.

        Additional information about the current status  # noqa: E501

        :param status_detail: The status_detail of this RenderTask.  # noqa: E501
        :type: str
        """

        self._status_detail = status_detail

    @property
    def user_id(self):
        """Gets the user_id of this RenderTask.  # noqa: E501

        The user account permissions in which the render task will execute  # noqa: E501

        :return: The user_id of this RenderTask.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RenderTask.

        The user account permissions in which the render task will execute  # noqa: E501

        :param user_id: The user_id of this RenderTask.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def runtime(self):
        """Gets the runtime of this RenderTask.  # noqa: E501

        Total seconds elapsed for render task  # noqa: E501

        :return: The runtime of this RenderTask.  # noqa: E501
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this RenderTask.

        Total seconds elapsed for render task  # noqa: E501

        :param runtime: The runtime of this RenderTask.  # noqa: E501
        :type: float
        """

        self._runtime = runtime

    @property
    def query_runtime(self):
        """Gets the query_runtime of this RenderTask.  # noqa: E501

        Number of seconds elapsed running queries  # noqa: E501

        :return: The query_runtime of this RenderTask.  # noqa: E501
        :rtype: float
        """
        return self._query_runtime

    @query_runtime.setter
    def query_runtime(self, query_runtime):
        """Sets the query_runtime of this RenderTask.

        Number of seconds elapsed running queries  # noqa: E501

        :param query_runtime: The query_runtime of this RenderTask.  # noqa: E501
        :type: float
        """

        self._query_runtime = query_runtime

    @property
    def render_runtime(self):
        """Gets the render_runtime of this RenderTask.  # noqa: E501

        Number of seconds elapsed rendering data  # noqa: E501

        :return: The render_runtime of this RenderTask.  # noqa: E501
        :rtype: float
        """
        return self._render_runtime

    @render_runtime.setter
    def render_runtime(self, render_runtime):
        """Sets the render_runtime of this RenderTask.

        Number of seconds elapsed rendering data  # noqa: E501

        :param render_runtime: The render_runtime of this RenderTask.  # noqa: E501
        :type: float
        """

        self._render_runtime = render_runtime

    @property
    def result_format(self):
        """Gets the result_format of this RenderTask.  # noqa: E501

        Output format: pdf, png, or jpg  # noqa: E501

        :return: The result_format of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        """Sets the result_format of this RenderTask.

        Output format: pdf, png, or jpg  # noqa: E501

        :param result_format: The result_format of this RenderTask.  # noqa: E501
        :type: str
        """

        self._result_format = result_format

    @property
    def look_id(self):
        """Gets the look_id of this RenderTask.  # noqa: E501

        Id of look to render  # noqa: E501

        :return: The look_id of this RenderTask.  # noqa: E501
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """Sets the look_id of this RenderTask.

        Id of look to render  # noqa: E501

        :param look_id: The look_id of this RenderTask.  # noqa: E501
        :type: int
        """

        self._look_id = look_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this RenderTask.  # noqa: E501

        Id of dashboard to render  # noqa: E501

        :return: The dashboard_id of this RenderTask.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this RenderTask.

        Id of dashboard to render  # noqa: E501

        :param dashboard_id: The dashboard_id of this RenderTask.  # noqa: E501
        :type: int
        """

        self._dashboard_id = dashboard_id

    @property
    def lookml_dashboard_id(self):
        """Gets the lookml_dashboard_id of this RenderTask.  # noqa: E501

        Id of lookml dashboard to render  # noqa: E501

        :return: The lookml_dashboard_id of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._lookml_dashboard_id

    @lookml_dashboard_id.setter
    def lookml_dashboard_id(self, lookml_dashboard_id):
        """Sets the lookml_dashboard_id of this RenderTask.

        Id of lookml dashboard to render  # noqa: E501

        :param lookml_dashboard_id: The lookml_dashboard_id of this RenderTask.  # noqa: E501
        :type: str
        """

        self._lookml_dashboard_id = lookml_dashboard_id

    @property
    def query_id(self):
        """Gets the query_id of this RenderTask.  # noqa: E501

        Id of query to render  # noqa: E501

        :return: The query_id of this RenderTask.  # noqa: E501
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this RenderTask.

        Id of query to render  # noqa: E501

        :param query_id: The query_id of this RenderTask.  # noqa: E501
        :type: int
        """

        self._query_id = query_id

    @property
    def width(self):
        """Gets the width of this RenderTask.  # noqa: E501

        Output width in pixels  # noqa: E501

        :return: The width of this RenderTask.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this RenderTask.

        Output width in pixels  # noqa: E501

        :param width: The width of this RenderTask.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this RenderTask.  # noqa: E501

        Output height in pixels. Flowed layouts may ignore this value.  # noqa: E501

        :return: The height of this RenderTask.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this RenderTask.

        Output height in pixels. Flowed layouts may ignore this value.  # noqa: E501

        :param height: The height of this RenderTask.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def dashboard_style(self):
        """Gets the dashboard_style of this RenderTask.  # noqa: E501

        Dashboard layout style: single_column or tiled  # noqa: E501

        :return: The dashboard_style of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_style

    @dashboard_style.setter
    def dashboard_style(self, dashboard_style):
        """Sets the dashboard_style of this RenderTask.

        Dashboard layout style: single_column or tiled  # noqa: E501

        :param dashboard_style: The dashboard_style of this RenderTask.  # noqa: E501
        :type: str
        """

        self._dashboard_style = dashboard_style

    @property
    def dashboard_filters(self):
        """Gets the dashboard_filters of this RenderTask.  # noqa: E501

        Filter values to apply to the dashboard queries, in URL query format  # noqa: E501

        :return: The dashboard_filters of this RenderTask.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_filters

    @dashboard_filters.setter
    def dashboard_filters(self, dashboard_filters):
        """Sets the dashboard_filters of this RenderTask.

        Filter values to apply to the dashboard queries, in URL query format  # noqa: E501

        :param dashboard_filters: The dashboard_filters of this RenderTask.  # noqa: E501
        :type: str
        """

        self._dashboard_filters = dashboard_filters

    @property
    def can(self):
        """Gets the can of this RenderTask.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this RenderTask.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this RenderTask.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this RenderTask.  # noqa: E501
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
        if not isinstance(other, RenderTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
