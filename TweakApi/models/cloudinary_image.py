# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.0
    
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


class CloudinaryImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, public_id=None, version=None, signature=None, width=None, height=None, format=None, resource_type=None, created_at=None, tags=None, bytes=None, type=None, etag=None, url=None, secure_url=None, original_filename=None, is_base64=False, id=None):
        """
        CloudinaryImage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'public_id': 'str',
            'version': 'str',
            'signature': 'str',
            'width': 'float',
            'height': 'float',
            'format': 'str',
            'resource_type': 'str',
            'created_at': 'str',
            'tags': 'list[str]',
            'bytes': 'float',
            'type': 'str',
            'etag': 'str',
            'url': 'str',
            'secure_url': 'str',
            'original_filename': 'str',
            'is_base64': 'bool',
            'id': 'str'
        }

        self.attribute_map = {
            'public_id': 'publicId',
            'version': 'version',
            'signature': 'signature',
            'width': 'width',
            'height': 'height',
            'format': 'format',
            'resource_type': 'resourceType',
            'created_at': 'createdAt',
            'tags': 'tags',
            'bytes': 'bytes',
            'type': 'type',
            'etag': 'etag',
            'url': 'url',
            'secure_url': 'secureUrl',
            'original_filename': 'originalFilename',
            'is_base64': 'isBase64',
            'id': 'id'
        }

        self._public_id = public_id
        self._version = version
        self._signature = signature
        self._width = width
        self._height = height
        self._format = format
        self._resource_type = resource_type
        self._created_at = created_at
        self._tags = tags
        self._bytes = bytes
        self._type = type
        self._etag = etag
        self._url = url
        self._secure_url = secure_url
        self._original_filename = original_filename
        self._is_base64 = is_base64
        self._id = id


    @property
    def public_id(self):
        """
        Gets the public_id of this CloudinaryImage.


        :return: The public_id of this CloudinaryImage.
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """
        Sets the public_id of this CloudinaryImage.


        :param public_id: The public_id of this CloudinaryImage.
        :type: str
        """

        self._public_id = public_id

    @property
    def version(self):
        """
        Gets the version of this CloudinaryImage.


        :return: The version of this CloudinaryImage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CloudinaryImage.


        :param version: The version of this CloudinaryImage.
        :type: str
        """

        self._version = version

    @property
    def signature(self):
        """
        Gets the signature of this CloudinaryImage.


        :return: The signature of this CloudinaryImage.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this CloudinaryImage.


        :param signature: The signature of this CloudinaryImage.
        :type: str
        """

        self._signature = signature

    @property
    def width(self):
        """
        Gets the width of this CloudinaryImage.


        :return: The width of this CloudinaryImage.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this CloudinaryImage.


        :param width: The width of this CloudinaryImage.
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this CloudinaryImage.


        :return: The height of this CloudinaryImage.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this CloudinaryImage.


        :param height: The height of this CloudinaryImage.
        :type: float
        """

        self._height = height

    @property
    def format(self):
        """
        Gets the format of this CloudinaryImage.


        :return: The format of this CloudinaryImage.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this CloudinaryImage.


        :param format: The format of this CloudinaryImage.
        :type: str
        """

        self._format = format

    @property
    def resource_type(self):
        """
        Gets the resource_type of this CloudinaryImage.


        :return: The resource_type of this CloudinaryImage.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this CloudinaryImage.


        :param resource_type: The resource_type of this CloudinaryImage.
        :type: str
        """
        allowed_values = ["image"]
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def created_at(self):
        """
        Gets the created_at of this CloudinaryImage.


        :return: The created_at of this CloudinaryImage.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CloudinaryImage.


        :param created_at: The created_at of this CloudinaryImage.
        :type: str
        """

        self._created_at = created_at

    @property
    def tags(self):
        """
        Gets the tags of this CloudinaryImage.


        :return: The tags of this CloudinaryImage.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CloudinaryImage.


        :param tags: The tags of this CloudinaryImage.
        :type: list[str]
        """

        self._tags = tags

    @property
    def bytes(self):
        """
        Gets the bytes of this CloudinaryImage.


        :return: The bytes of this CloudinaryImage.
        :rtype: float
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """
        Sets the bytes of this CloudinaryImage.


        :param bytes: The bytes of this CloudinaryImage.
        :type: float
        """

        self._bytes = bytes

    @property
    def type(self):
        """
        Gets the type of this CloudinaryImage.


        :return: The type of this CloudinaryImage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloudinaryImage.


        :param type: The type of this CloudinaryImage.
        :type: str
        """

        self._type = type

    @property
    def etag(self):
        """
        Gets the etag of this CloudinaryImage.


        :return: The etag of this CloudinaryImage.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CloudinaryImage.


        :param etag: The etag of this CloudinaryImage.
        :type: str
        """

        self._etag = etag

    @property
    def url(self):
        """
        Gets the url of this CloudinaryImage.


        :return: The url of this CloudinaryImage.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CloudinaryImage.


        :param url: The url of this CloudinaryImage.
        :type: str
        """

        self._url = url

    @property
    def secure_url(self):
        """
        Gets the secure_url of this CloudinaryImage.


        :return: The secure_url of this CloudinaryImage.
        :rtype: str
        """
        return self._secure_url

    @secure_url.setter
    def secure_url(self, secure_url):
        """
        Sets the secure_url of this CloudinaryImage.


        :param secure_url: The secure_url of this CloudinaryImage.
        :type: str
        """

        self._secure_url = secure_url

    @property
    def original_filename(self):
        """
        Gets the original_filename of this CloudinaryImage.


        :return: The original_filename of this CloudinaryImage.
        :rtype: str
        """
        return self._original_filename

    @original_filename.setter
    def original_filename(self, original_filename):
        """
        Sets the original_filename of this CloudinaryImage.


        :param original_filename: The original_filename of this CloudinaryImage.
        :type: str
        """

        self._original_filename = original_filename

    @property
    def is_base64(self):
        """
        Gets the is_base64 of this CloudinaryImage.


        :return: The is_base64 of this CloudinaryImage.
        :rtype: bool
        """
        return self._is_base64

    @is_base64.setter
    def is_base64(self, is_base64):
        """
        Sets the is_base64 of this CloudinaryImage.


        :param is_base64: The is_base64 of this CloudinaryImage.
        :type: bool
        """

        self._is_base64 = is_base64

    @property
    def id(self):
        """
        Gets the id of this CloudinaryImage.


        :return: The id of this CloudinaryImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudinaryImage.


        :param id: The id of this CloudinaryImage.
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
