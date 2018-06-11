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

from looker_client_30.looker_sdk.look_with_query import LookWithQuery  # noqa: F401,E501
from looker_client_30.looker_sdk.query import Query  # noqa: F401,E501
from looker_client_30.looker_sdk.result_maker_with_id_vis_config_and_dynamic_fields import ResultMakerWithIdVisConfigAndDynamicFields  # noqa: F401,E501


class DashboardElement(object):
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
        'dashboard_id': 'str',
        'look_id': 'str',
        'query_id': 'int',
        'type': 'str',
        'listen': 'dict(str, str)',
        'refresh_interval': 'str',
        'refresh_interval_to_i': 'int',
        'note_text': 'str',
        'note_text_as_html': 'str',
        'note_display': 'str',
        'note_state': 'str',
        'title_hidden': 'bool',
        'title_text': 'str',
        'title': 'str',
        'subtitle_text': 'str',
        'body_text': 'str',
        'body_text_as_html': 'str',
        'look': 'LookWithQuery',
        'query': 'Query',
        'edit_uri': 'str',
        'merge_result_id': 'str',
        'result_maker_id': 'int',
        'result_maker': 'ResultMakerWithIdVisConfigAndDynamicFields',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'dashboard_id': 'dashboard_id',
        'look_id': 'look_id',
        'query_id': 'query_id',
        'type': 'type',
        'listen': 'listen',
        'refresh_interval': 'refresh_interval',
        'refresh_interval_to_i': 'refresh_interval_to_i',
        'note_text': 'note_text',
        'note_text_as_html': 'note_text_as_html',
        'note_display': 'note_display',
        'note_state': 'note_state',
        'title_hidden': 'title_hidden',
        'title_text': 'title_text',
        'title': 'title',
        'subtitle_text': 'subtitle_text',
        'body_text': 'body_text',
        'body_text_as_html': 'body_text_as_html',
        'look': 'look',
        'query': 'query',
        'edit_uri': 'edit_uri',
        'merge_result_id': 'merge_result_id',
        'result_maker_id': 'result_maker_id',
        'result_maker': 'result_maker',
        'can': 'can'
    }

    def __init__(self, id=None, dashboard_id=None, look_id=None, query_id=None, type=None, listen=None, refresh_interval=None, refresh_interval_to_i=None, note_text=None, note_text_as_html=None, note_display=None, note_state=None, title_hidden=None, title_text=None, title=None, subtitle_text=None, body_text=None, body_text_as_html=None, look=None, query=None, edit_uri=None, merge_result_id=None, result_maker_id=None, result_maker=None, can=None):  # noqa: E501
        """DashboardElement - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._dashboard_id = None
        self._look_id = None
        self._query_id = None
        self._type = None
        self._listen = None
        self._refresh_interval = None
        self._refresh_interval_to_i = None
        self._note_text = None
        self._note_text_as_html = None
        self._note_display = None
        self._note_state = None
        self._title_hidden = None
        self._title_text = None
        self._title = None
        self._subtitle_text = None
        self._body_text = None
        self._body_text_as_html = None
        self._look = None
        self._query = None
        self._edit_uri = None
        self._merge_result_id = None
        self._result_maker_id = None
        self._result_maker = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if look_id is not None:
            self.look_id = look_id
        if query_id is not None:
            self.query_id = query_id
        if type is not None:
            self.type = type
        if listen is not None:
            self.listen = listen
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if refresh_interval_to_i is not None:
            self.refresh_interval_to_i = refresh_interval_to_i
        if note_text is not None:
            self.note_text = note_text
        if note_text_as_html is not None:
            self.note_text_as_html = note_text_as_html
        if note_display is not None:
            self.note_display = note_display
        if note_state is not None:
            self.note_state = note_state
        if title_hidden is not None:
            self.title_hidden = title_hidden
        if title_text is not None:
            self.title_text = title_text
        if title is not None:
            self.title = title
        if subtitle_text is not None:
            self.subtitle_text = subtitle_text
        if body_text is not None:
            self.body_text = body_text
        if body_text_as_html is not None:
            self.body_text_as_html = body_text_as_html
        if look is not None:
            self.look = look
        if query is not None:
            self.query = query
        if edit_uri is not None:
            self.edit_uri = edit_uri
        if merge_result_id is not None:
            self.merge_result_id = merge_result_id
        if result_maker_id is not None:
            self.result_maker_id = result_maker_id
        if result_maker is not None:
            self.result_maker = result_maker
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this DashboardElement.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardElement.

        Unique Id  # noqa: E501

        :param id: The id of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this DashboardElement.  # noqa: E501

        Id of Dashboard  # noqa: E501

        :return: The dashboard_id of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this DashboardElement.

        Id of Dashboard  # noqa: E501

        :param dashboard_id: The dashboard_id of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def look_id(self):
        """Gets the look_id of this DashboardElement.  # noqa: E501

        Id Of Look  # noqa: E501

        :return: The look_id of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """Sets the look_id of this DashboardElement.

        Id Of Look  # noqa: E501

        :param look_id: The look_id of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._look_id = look_id

    @property
    def query_id(self):
        """Gets the query_id of this DashboardElement.  # noqa: E501

        Id Of Query  # noqa: E501

        :return: The query_id of this DashboardElement.  # noqa: E501
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this DashboardElement.

        Id Of Query  # noqa: E501

        :param query_id: The query_id of this DashboardElement.  # noqa: E501
        :type: int
        """

        self._query_id = query_id

    @property
    def type(self):
        """Gets the type of this DashboardElement.  # noqa: E501

        Type  # noqa: E501

        :return: The type of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DashboardElement.

        Type  # noqa: E501

        :param type: The type of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def listen(self):
        """Gets the listen of this DashboardElement.  # noqa: E501

        Listen  # noqa: E501

        :return: The listen of this DashboardElement.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._listen

    @listen.setter
    def listen(self, listen):
        """Sets the listen of this DashboardElement.

        Listen  # noqa: E501

        :param listen: The listen of this DashboardElement.  # noqa: E501
        :type: dict(str, str)
        """

        self._listen = listen

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this DashboardElement.  # noqa: E501

        Refresh Interval  # noqa: E501

        :return: The refresh_interval of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this DashboardElement.

        Refresh Interval  # noqa: E501

        :param refresh_interval: The refresh_interval of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._refresh_interval = refresh_interval

    @property
    def refresh_interval_to_i(self):
        """Gets the refresh_interval_to_i of this DashboardElement.  # noqa: E501

        Refresh Interval as integer  # noqa: E501

        :return: The refresh_interval_to_i of this DashboardElement.  # noqa: E501
        :rtype: int
        """
        return self._refresh_interval_to_i

    @refresh_interval_to_i.setter
    def refresh_interval_to_i(self, refresh_interval_to_i):
        """Sets the refresh_interval_to_i of this DashboardElement.

        Refresh Interval as integer  # noqa: E501

        :param refresh_interval_to_i: The refresh_interval_to_i of this DashboardElement.  # noqa: E501
        :type: int
        """

        self._refresh_interval_to_i = refresh_interval_to_i

    @property
    def note_text(self):
        """Gets the note_text of this DashboardElement.  # noqa: E501

        Note Text  # noqa: E501

        :return: The note_text of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._note_text

    @note_text.setter
    def note_text(self, note_text):
        """Sets the note_text of this DashboardElement.

        Note Text  # noqa: E501

        :param note_text: The note_text of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._note_text = note_text

    @property
    def note_text_as_html(self):
        """Gets the note_text_as_html of this DashboardElement.  # noqa: E501

        Note Text as Html  # noqa: E501

        :return: The note_text_as_html of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._note_text_as_html

    @note_text_as_html.setter
    def note_text_as_html(self, note_text_as_html):
        """Sets the note_text_as_html of this DashboardElement.

        Note Text as Html  # noqa: E501

        :param note_text_as_html: The note_text_as_html of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._note_text_as_html = note_text_as_html

    @property
    def note_display(self):
        """Gets the note_display of this DashboardElement.  # noqa: E501

        Note Display  # noqa: E501

        :return: The note_display of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._note_display

    @note_display.setter
    def note_display(self, note_display):
        """Sets the note_display of this DashboardElement.

        Note Display  # noqa: E501

        :param note_display: The note_display of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._note_display = note_display

    @property
    def note_state(self):
        """Gets the note_state of this DashboardElement.  # noqa: E501

        Note State  # noqa: E501

        :return: The note_state of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._note_state

    @note_state.setter
    def note_state(self, note_state):
        """Sets the note_state of this DashboardElement.

        Note State  # noqa: E501

        :param note_state: The note_state of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._note_state = note_state

    @property
    def title_hidden(self):
        """Gets the title_hidden of this DashboardElement.  # noqa: E501

        Whether title is hidden  # noqa: E501

        :return: The title_hidden of this DashboardElement.  # noqa: E501
        :rtype: bool
        """
        return self._title_hidden

    @title_hidden.setter
    def title_hidden(self, title_hidden):
        """Sets the title_hidden of this DashboardElement.

        Whether title is hidden  # noqa: E501

        :param title_hidden: The title_hidden of this DashboardElement.  # noqa: E501
        :type: bool
        """

        self._title_hidden = title_hidden

    @property
    def title_text(self):
        """Gets the title_text of this DashboardElement.  # noqa: E501

        Text tile title  # noqa: E501

        :return: The title_text of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._title_text

    @title_text.setter
    def title_text(self, title_text):
        """Sets the title_text of this DashboardElement.

        Text tile title  # noqa: E501

        :param title_text: The title_text of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._title_text = title_text

    @property
    def title(self):
        """Gets the title of this DashboardElement.  # noqa: E501

        Title of dashboard element  # noqa: E501

        :return: The title of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DashboardElement.

        Title of dashboard element  # noqa: E501

        :param title: The title of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subtitle_text(self):
        """Gets the subtitle_text of this DashboardElement.  # noqa: E501

        Text tile subtitle text  # noqa: E501

        :return: The subtitle_text of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._subtitle_text

    @subtitle_text.setter
    def subtitle_text(self, subtitle_text):
        """Sets the subtitle_text of this DashboardElement.

        Text tile subtitle text  # noqa: E501

        :param subtitle_text: The subtitle_text of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._subtitle_text = subtitle_text

    @property
    def body_text(self):
        """Gets the body_text of this DashboardElement.  # noqa: E501

        Text tile body text  # noqa: E501

        :return: The body_text of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._body_text

    @body_text.setter
    def body_text(self, body_text):
        """Sets the body_text of this DashboardElement.

        Text tile body text  # noqa: E501

        :param body_text: The body_text of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._body_text = body_text

    @property
    def body_text_as_html(self):
        """Gets the body_text_as_html of this DashboardElement.  # noqa: E501

        Text tile body text as Html  # noqa: E501

        :return: The body_text_as_html of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._body_text_as_html

    @body_text_as_html.setter
    def body_text_as_html(self, body_text_as_html):
        """Sets the body_text_as_html of this DashboardElement.

        Text tile body text as Html  # noqa: E501

        :param body_text_as_html: The body_text_as_html of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._body_text_as_html = body_text_as_html

    @property
    def look(self):
        """Gets the look of this DashboardElement.  # noqa: E501

        Look  # noqa: E501

        :return: The look of this DashboardElement.  # noqa: E501
        :rtype: LookWithQuery
        """
        return self._look

    @look.setter
    def look(self, look):
        """Sets the look of this DashboardElement.

        Look  # noqa: E501

        :param look: The look of this DashboardElement.  # noqa: E501
        :type: LookWithQuery
        """

        self._look = look

    @property
    def query(self):
        """Gets the query of this DashboardElement.  # noqa: E501

        Query  # noqa: E501

        :return: The query of this DashboardElement.  # noqa: E501
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this DashboardElement.

        Query  # noqa: E501

        :param query: The query of this DashboardElement.  # noqa: E501
        :type: Query
        """

        self._query = query

    @property
    def edit_uri(self):
        """Gets the edit_uri of this DashboardElement.  # noqa: E501

        Relative path of URI of LookML file to edit the dashboard element (LookML dashboard only).  # noqa: E501

        :return: The edit_uri of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._edit_uri

    @edit_uri.setter
    def edit_uri(self, edit_uri):
        """Sets the edit_uri of this DashboardElement.

        Relative path of URI of LookML file to edit the dashboard element (LookML dashboard only).  # noqa: E501

        :param edit_uri: The edit_uri of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._edit_uri = edit_uri

    @property
    def merge_result_id(self):
        """Gets the merge_result_id of this DashboardElement.  # noqa: E501

        ID of merge result  # noqa: E501

        :return: The merge_result_id of this DashboardElement.  # noqa: E501
        :rtype: str
        """
        return self._merge_result_id

    @merge_result_id.setter
    def merge_result_id(self, merge_result_id):
        """Sets the merge_result_id of this DashboardElement.

        ID of merge result  # noqa: E501

        :param merge_result_id: The merge_result_id of this DashboardElement.  # noqa: E501
        :type: str
        """

        self._merge_result_id = merge_result_id

    @property
    def result_maker_id(self):
        """Gets the result_maker_id of this DashboardElement.  # noqa: E501

        ID of the ResultMakerLookup entry.  # noqa: E501

        :return: The result_maker_id of this DashboardElement.  # noqa: E501
        :rtype: int
        """
        return self._result_maker_id

    @result_maker_id.setter
    def result_maker_id(self, result_maker_id):
        """Sets the result_maker_id of this DashboardElement.

        ID of the ResultMakerLookup entry.  # noqa: E501

        :param result_maker_id: The result_maker_id of this DashboardElement.  # noqa: E501
        :type: int
        """

        self._result_maker_id = result_maker_id

    @property
    def result_maker(self):
        """Gets the result_maker of this DashboardElement.  # noqa: E501

        Data about the result maker.  # noqa: E501

        :return: The result_maker of this DashboardElement.  # noqa: E501
        :rtype: ResultMakerWithIdVisConfigAndDynamicFields
        """
        return self._result_maker

    @result_maker.setter
    def result_maker(self, result_maker):
        """Sets the result_maker of this DashboardElement.

        Data about the result maker.  # noqa: E501

        :param result_maker: The result_maker of this DashboardElement.  # noqa: E501
        :type: ResultMakerWithIdVisConfigAndDynamicFields
        """

        self._result_maker = result_maker

    @property
    def can(self):
        """Gets the can of this DashboardElement.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this DashboardElement.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this DashboardElement.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this DashboardElement.  # noqa: E501
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
        if not isinstance(other, DashboardElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
