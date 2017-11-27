# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.6
    
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


class Workflow(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, form=None, edited=None, created=None, modified=None, id=None, team_id=None, creator_id=None, team=None, templates=None, creator=None):
        """
        Workflow - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'form': 'list[object]',
            'edited': 'datetime',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'creator_id': 'str',
            'team': 'Team',
            'templates': 'list[Template]',
            'creator': 'TeamMember'
        }

        self.attribute_map = {
            'name': 'name',
            'form': 'form',
            'edited': 'edited',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'creator_id': 'creatorId',
            'team': 'team',
            'templates': 'templates',
            'creator': 'creator'
        }

        self._name = name
        self._form = form
        self._edited = edited
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._creator_id = creator_id
        self._team = team
        self._templates = templates
        self._creator = creator


    @property
    def name(self):
        """
        Gets the name of this Workflow.


        :return: The name of this Workflow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Workflow.


        :param name: The name of this Workflow.
        :type: str
        """

        self._name = name

    @property
    def form(self):
        """
        Gets the form of this Workflow.


        :return: The form of this Workflow.
        :rtype: list[object]
        """
        return self._form

    @form.setter
    def form(self, form):
        """
        Sets the form of this Workflow.


        :param form: The form of this Workflow.
        :type: list[object]
        """

        self._form = form

    @property
    def edited(self):
        """
        Gets the edited of this Workflow.


        :return: The edited of this Workflow.
        :rtype: datetime
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        """
        Sets the edited of this Workflow.


        :param edited: The edited of this Workflow.
        :type: datetime
        """

        self._edited = edited

    @property
    def created(self):
        """
        Gets the created of this Workflow.


        :return: The created of this Workflow.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Workflow.


        :param created: The created of this Workflow.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Workflow.


        :return: The modified of this Workflow.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Workflow.


        :param modified: The modified of this Workflow.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Workflow.


        :return: The id of this Workflow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Workflow.


        :param id: The id of this Workflow.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this Workflow.


        :return: The team_id of this Workflow.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Workflow.


        :param team_id: The team_id of this Workflow.
        :type: str
        """

        self._team_id = team_id

    @property
    def creator_id(self):
        """
        Gets the creator_id of this Workflow.


        :return: The creator_id of this Workflow.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this Workflow.


        :param creator_id: The creator_id of this Workflow.
        :type: str
        """

        self._creator_id = creator_id

    @property
    def team(self):
        """
        Gets the team of this Workflow.


        :return: The team of this Workflow.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Workflow.


        :param team: The team of this Workflow.
        :type: Team
        """

        self._team = team

    @property
    def templates(self):
        """
        Gets the templates of this Workflow.


        :return: The templates of this Workflow.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this Workflow.


        :param templates: The templates of this Workflow.
        :type: list[Template]
        """

        self._templates = templates

    @property
    def creator(self):
        """
        Gets the creator of this Workflow.


        :return: The creator of this Workflow.
        :rtype: TeamMember
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this Workflow.


        :param creator: The creator of this Workflow.
        :type: TeamMember
        """

        self._creator = creator

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
