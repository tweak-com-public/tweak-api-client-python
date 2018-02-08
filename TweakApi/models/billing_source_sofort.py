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


class BillingSourceSofort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country=None, bank_code=None, bic=None, bank_name=None, iban_last4=None, preferred_language=None, statement_descriptor=None, id=None):
        """
        BillingSourceSofort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country': 'str',
            'bank_code': 'str',
            'bic': 'str',
            'bank_name': 'str',
            'iban_last4': 'str',
            'preferred_language': 'str',
            'statement_descriptor': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'country': 'country',
            'bank_code': 'bankCode',
            'bic': 'bic',
            'bank_name': 'bankName',
            'iban_last4': 'ibanLast4',
            'preferred_language': 'preferredLanguage',
            'statement_descriptor': 'statementDescriptor',
            'id': 'id'
        }

        self._country = country
        self._bank_code = bank_code
        self._bic = bic
        self._bank_name = bank_name
        self._iban_last4 = iban_last4
        self._preferred_language = preferred_language
        self._statement_descriptor = statement_descriptor
        self._id = id


    @property
    def country(self):
        """
        Gets the country of this BillingSourceSofort.


        :return: The country of this BillingSourceSofort.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingSourceSofort.


        :param country: The country of this BillingSourceSofort.
        :type: str
        """

        self._country = country

    @property
    def bank_code(self):
        """
        Gets the bank_code of this BillingSourceSofort.


        :return: The bank_code of this BillingSourceSofort.
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """
        Sets the bank_code of this BillingSourceSofort.


        :param bank_code: The bank_code of this BillingSourceSofort.
        :type: str
        """

        self._bank_code = bank_code

    @property
    def bic(self):
        """
        Gets the bic of this BillingSourceSofort.


        :return: The bic of this BillingSourceSofort.
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """
        Sets the bic of this BillingSourceSofort.


        :param bic: The bic of this BillingSourceSofort.
        :type: str
        """

        self._bic = bic

    @property
    def bank_name(self):
        """
        Gets the bank_name of this BillingSourceSofort.


        :return: The bank_name of this BillingSourceSofort.
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """
        Sets the bank_name of this BillingSourceSofort.


        :param bank_name: The bank_name of this BillingSourceSofort.
        :type: str
        """

        self._bank_name = bank_name

    @property
    def iban_last4(self):
        """
        Gets the iban_last4 of this BillingSourceSofort.


        :return: The iban_last4 of this BillingSourceSofort.
        :rtype: str
        """
        return self._iban_last4

    @iban_last4.setter
    def iban_last4(self, iban_last4):
        """
        Sets the iban_last4 of this BillingSourceSofort.


        :param iban_last4: The iban_last4 of this BillingSourceSofort.
        :type: str
        """

        self._iban_last4 = iban_last4

    @property
    def preferred_language(self):
        """
        Gets the preferred_language of this BillingSourceSofort.


        :return: The preferred_language of this BillingSourceSofort.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """
        Sets the preferred_language of this BillingSourceSofort.


        :param preferred_language: The preferred_language of this BillingSourceSofort.
        :type: str
        """

        self._preferred_language = preferred_language

    @property
    def statement_descriptor(self):
        """
        Gets the statement_descriptor of this BillingSourceSofort.


        :return: The statement_descriptor of this BillingSourceSofort.
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """
        Sets the statement_descriptor of this BillingSourceSofort.


        :param statement_descriptor: The statement_descriptor of this BillingSourceSofort.
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def id(self):
        """
        Gets the id of this BillingSourceSofort.


        :return: The id of this BillingSourceSofort.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingSourceSofort.


        :param id: The id of this BillingSourceSofort.
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
