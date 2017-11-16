# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class DesignComment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, comment=None, position=None, page_index=0.0, status=None, type=None, created=None, modified=None, id=None, design_id=None, comment_id=None, commenter_id=None, design=None, replies=None, commenter=None, reply_of=None):
        """
        DesignComment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'comment': 'str',
            'position': 'Axes',
            'page_index': 'float',
            'status': 'str',
            'type': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'design_id': 'str',
            'comment_id': 'str',
            'commenter_id': 'str',
            'design': 'Design',
            'replies': 'list[DesignComment]',
            'commenter': 'TeamMember',
            'reply_of': 'DesignComment'
        }

        self.attribute_map = {
            'comment': 'comment',
            'position': 'position',
            'page_index': 'pageIndex',
            'status': 'status',
            'type': 'type',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'design_id': 'designId',
            'comment_id': 'commentId',
            'commenter_id': 'commenterId',
            'design': 'design',
            'replies': 'replies',
            'commenter': 'commenter',
            'reply_of': 'replyOf'
        }

        self._comment = comment
        self._position = position
        self._page_index = page_index
        self._status = status
        self._type = type
        self._created = created
        self._modified = modified
        self._id = id
        self._design_id = design_id
        self._comment_id = comment_id
        self._commenter_id = commenter_id
        self._design = design
        self._replies = replies
        self._commenter = commenter
        self._reply_of = reply_of


    @property
    def comment(self):
        """
        Gets the comment of this DesignComment.


        :return: The comment of this DesignComment.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this DesignComment.


        :param comment: The comment of this DesignComment.
        :type: str
        """

        self._comment = comment

    @property
    def position(self):
        """
        Gets the position of this DesignComment.


        :return: The position of this DesignComment.
        :rtype: Axes
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this DesignComment.


        :param position: The position of this DesignComment.
        :type: Axes
        """

        self._position = position

    @property
    def page_index(self):
        """
        Gets the page_index of this DesignComment.


        :return: The page_index of this DesignComment.
        :rtype: float
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this DesignComment.


        :param page_index: The page_index of this DesignComment.
        :type: float
        """

        if not page_index:
            raise ValueError("Invalid value for `page_index`, must not be `None`")
        if page_index < 0.0:
            raise ValueError("Invalid value for `page_index`, must be a value greater than or equal to `0.0`")

        self._page_index = page_index

    @property
    def status(self):
        """
        Gets the status of this DesignComment.


        :return: The status of this DesignComment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DesignComment.


        :param status: The status of this DesignComment.
        :type: str
        """
        allowed_values = ["unsolved", "resolved"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this DesignComment.


        :return: The type of this DesignComment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DesignComment.


        :param type: The type of this DesignComment.
        :type: str
        """
        allowed_values = ["comment", "rejection", "reaction"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def created(self):
        """
        Gets the created of this DesignComment.


        :return: The created of this DesignComment.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DesignComment.


        :param created: The created of this DesignComment.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this DesignComment.


        :return: The modified of this DesignComment.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this DesignComment.


        :param modified: The modified of this DesignComment.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this DesignComment.


        :return: The id of this DesignComment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DesignComment.


        :param id: The id of this DesignComment.
        :type: str
        """

        self._id = id

    @property
    def design_id(self):
        """
        Gets the design_id of this DesignComment.


        :return: The design_id of this DesignComment.
        :rtype: str
        """
        return self._design_id

    @design_id.setter
    def design_id(self, design_id):
        """
        Sets the design_id of this DesignComment.


        :param design_id: The design_id of this DesignComment.
        :type: str
        """

        self._design_id = design_id

    @property
    def comment_id(self):
        """
        Gets the comment_id of this DesignComment.


        :return: The comment_id of this DesignComment.
        :rtype: str
        """
        return self._comment_id

    @comment_id.setter
    def comment_id(self, comment_id):
        """
        Sets the comment_id of this DesignComment.


        :param comment_id: The comment_id of this DesignComment.
        :type: str
        """

        self._comment_id = comment_id

    @property
    def commenter_id(self):
        """
        Gets the commenter_id of this DesignComment.


        :return: The commenter_id of this DesignComment.
        :rtype: str
        """
        return self._commenter_id

    @commenter_id.setter
    def commenter_id(self, commenter_id):
        """
        Sets the commenter_id of this DesignComment.


        :param commenter_id: The commenter_id of this DesignComment.
        :type: str
        """

        self._commenter_id = commenter_id

    @property
    def design(self):
        """
        Gets the design of this DesignComment.


        :return: The design of this DesignComment.
        :rtype: Design
        """
        return self._design

    @design.setter
    def design(self, design):
        """
        Sets the design of this DesignComment.


        :param design: The design of this DesignComment.
        :type: Design
        """

        self._design = design

    @property
    def replies(self):
        """
        Gets the replies of this DesignComment.


        :return: The replies of this DesignComment.
        :rtype: list[DesignComment]
        """
        return self._replies

    @replies.setter
    def replies(self, replies):
        """
        Sets the replies of this DesignComment.


        :param replies: The replies of this DesignComment.
        :type: list[DesignComment]
        """

        self._replies = replies

    @property
    def commenter(self):
        """
        Gets the commenter of this DesignComment.


        :return: The commenter of this DesignComment.
        :rtype: TeamMember
        """
        return self._commenter

    @commenter.setter
    def commenter(self, commenter):
        """
        Sets the commenter of this DesignComment.


        :param commenter: The commenter of this DesignComment.
        :type: TeamMember
        """

        self._commenter = commenter

    @property
    def reply_of(self):
        """
        Gets the reply_of of this DesignComment.


        :return: The reply_of of this DesignComment.
        :rtype: DesignComment
        """
        return self._reply_of

    @reply_of.setter
    def reply_of(self, reply_of):
        """
        Sets the reply_of of this DesignComment.


        :param reply_of: The reply_of of this DesignComment.
        :type: DesignComment
        """

        self._reply_of = reply_of

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
