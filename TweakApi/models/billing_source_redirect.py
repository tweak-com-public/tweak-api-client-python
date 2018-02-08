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


class BillingSourceRedirect(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, return_url=None, status=None, url=None, id=None):
        """
        BillingSourceRedirect - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'return_url': 'str',
            'status': 'str',
            'url': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'return_url': 'returnUrl',
            'status': 'status',
            'url': 'url',
            'id': 'id'
        }

        self._return_url = return_url
        self._status = status
        self._url = url
        self._id = id


    @property
    def return_url(self):
        """
        Gets the return_url of this BillingSourceRedirect.


        :return: The return_url of this BillingSourceRedirect.
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """
        Sets the return_url of this BillingSourceRedirect.


        :param return_url: The return_url of this BillingSourceRedirect.
        :type: str
        """

        self._return_url = return_url

    @property
    def status(self):
        """
        Gets the status of this BillingSourceRedirect.


        :return: The status of this BillingSourceRedirect.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BillingSourceRedirect.


        :param status: The status of this BillingSourceRedirect.
        :type: str
        """

        self._status = status

    @property
    def url(self):
        """
        Gets the url of this BillingSourceRedirect.


        :return: The url of this BillingSourceRedirect.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this BillingSourceRedirect.


        :param url: The url of this BillingSourceRedirect.
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """
        Gets the id of this BillingSourceRedirect.


        :return: The id of this BillingSourceRedirect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingSourceRedirect.


        :param id: The id of this BillingSourceRedirect.
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
