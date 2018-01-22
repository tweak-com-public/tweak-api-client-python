# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.2
    
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


class DesignMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, modified=None, id=None, design_id=None, member_id=None, design=None, member=None):
        """
        DesignMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'design_id': 'str',
            'member_id': 'str',
            'design': 'Design',
            'member': 'TeamMember'
        }

        self.attribute_map = {
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'design_id': 'designId',
            'member_id': 'memberId',
            'design': 'design',
            'member': 'member'
        }

        self._created = created
        self._modified = modified
        self._id = id
        self._design_id = design_id
        self._member_id = member_id
        self._design = design
        self._member = member


    @property
    def created(self):
        """
        Gets the created of this DesignMember.


        :return: The created of this DesignMember.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DesignMember.


        :param created: The created of this DesignMember.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this DesignMember.


        :return: The modified of this DesignMember.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this DesignMember.


        :param modified: The modified of this DesignMember.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this DesignMember.


        :return: The id of this DesignMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DesignMember.


        :param id: The id of this DesignMember.
        :type: str
        """

        self._id = id

    @property
    def design_id(self):
        """
        Gets the design_id of this DesignMember.


        :return: The design_id of this DesignMember.
        :rtype: str
        """
        return self._design_id

    @design_id.setter
    def design_id(self, design_id):
        """
        Sets the design_id of this DesignMember.


        :param design_id: The design_id of this DesignMember.
        :type: str
        """

        self._design_id = design_id

    @property
    def member_id(self):
        """
        Gets the member_id of this DesignMember.


        :return: The member_id of this DesignMember.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this DesignMember.


        :param member_id: The member_id of this DesignMember.
        :type: str
        """

        self._member_id = member_id

    @property
    def design(self):
        """
        Gets the design of this DesignMember.


        :return: The design of this DesignMember.
        :rtype: Design
        """
        return self._design

    @design.setter
    def design(self, design):
        """
        Sets the design of this DesignMember.


        :param design: The design of this DesignMember.
        :type: Design
        """

        self._design = design

    @property
    def member(self):
        """
        Gets the member of this DesignMember.


        :return: The member of this DesignMember.
        :rtype: TeamMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this DesignMember.


        :param member: The member of this DesignMember.
        :type: TeamMember
        """

        self._member = member

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
