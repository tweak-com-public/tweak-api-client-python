# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-alpha.4
    
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


class DesignExport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, created=None, id=None, design_id=None, requester_id=None, designs=None, requester=None):
        """
        DesignExport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'created': 'datetime',
            'id': 'str',
            'design_id': 'str',
            'requester_id': 'str',
            'designs': 'Design',
            'requester': 'TeamMember'
        }

        self.attribute_map = {
            'type': 'type',
            'created': 'created',
            'id': 'id',
            'design_id': 'designId',
            'requester_id': 'requesterId',
            'designs': 'designs',
            'requester': 'requester'
        }

        self._type = type
        self._created = created
        self._id = id
        self._design_id = design_id
        self._requester_id = requester_id
        self._designs = designs
        self._requester = requester


    @property
    def type(self):
        """
        Gets the type of this DesignExport.


        :return: The type of this DesignExport.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DesignExport.


        :param type: The type of this DesignExport.
        :type: str
        """
        allowed_values = ["proof", "pdf"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def created(self):
        """
        Gets the created of this DesignExport.


        :return: The created of this DesignExport.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DesignExport.


        :param created: The created of this DesignExport.
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this DesignExport.


        :return: The id of this DesignExport.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DesignExport.


        :param id: The id of this DesignExport.
        :type: str
        """

        self._id = id

    @property
    def design_id(self):
        """
        Gets the design_id of this DesignExport.


        :return: The design_id of this DesignExport.
        :rtype: str
        """
        return self._design_id

    @design_id.setter
    def design_id(self, design_id):
        """
        Sets the design_id of this DesignExport.


        :param design_id: The design_id of this DesignExport.
        :type: str
        """

        self._design_id = design_id

    @property
    def requester_id(self):
        """
        Gets the requester_id of this DesignExport.


        :return: The requester_id of this DesignExport.
        :rtype: str
        """
        return self._requester_id

    @requester_id.setter
    def requester_id(self, requester_id):
        """
        Sets the requester_id of this DesignExport.


        :param requester_id: The requester_id of this DesignExport.
        :type: str
        """

        self._requester_id = requester_id

    @property
    def designs(self):
        """
        Gets the designs of this DesignExport.


        :return: The designs of this DesignExport.
        :rtype: Design
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """
        Sets the designs of this DesignExport.


        :param designs: The designs of this DesignExport.
        :type: Design
        """

        self._designs = designs

    @property
    def requester(self):
        """
        Gets the requester of this DesignExport.


        :return: The requester of this DesignExport.
        :rtype: TeamMember
        """
        return self._requester

    @requester.setter
    def requester(self, requester):
        """
        Sets the requester of this DesignExport.


        :param requester: The requester of this DesignExport.
        :type: TeamMember
        """

        self._requester = requester

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
