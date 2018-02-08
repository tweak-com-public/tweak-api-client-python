# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.7-beta.3
    
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


class BuilderAssetBackgroundFolder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, path=None, thumbnail=None, id=None):
        """
        BuilderAssetBackgroundFolder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'path': 'str',
            'thumbnail': 'CloudinaryImage',
            'id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'thumbnail': 'thumbnail',
            'id': 'id'
        }

        self._name = name
        self._path = path
        self._thumbnail = thumbnail
        self._id = id


    @property
    def name(self):
        """
        Gets the name of this BuilderAssetBackgroundFolder.


        :return: The name of this BuilderAssetBackgroundFolder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuilderAssetBackgroundFolder.


        :param name: The name of this BuilderAssetBackgroundFolder.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this BuilderAssetBackgroundFolder.


        :return: The path of this BuilderAssetBackgroundFolder.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this BuilderAssetBackgroundFolder.


        :param path: The path of this BuilderAssetBackgroundFolder.
        :type: str
        """

        self._path = path

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this BuilderAssetBackgroundFolder.


        :return: The thumbnail of this BuilderAssetBackgroundFolder.
        :rtype: CloudinaryImage
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this BuilderAssetBackgroundFolder.


        :param thumbnail: The thumbnail of this BuilderAssetBackgroundFolder.
        :type: CloudinaryImage
        """

        self._thumbnail = thumbnail

    @property
    def id(self):
        """
        Gets the id of this BuilderAssetBackgroundFolder.


        :return: The id of this BuilderAssetBackgroundFolder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuilderAssetBackgroundFolder.


        :param id: The id of this BuilderAssetBackgroundFolder.
        :type: str
        """

        self._id = id

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
