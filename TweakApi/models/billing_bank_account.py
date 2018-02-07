# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.7-alpha.4
    
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


class BillingBankAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, object='bank_account', account=None, account_holder_name=None, account_holder_type=None, bank_name=None, country=None, currency=None, default_for_currency=False, fingerprint=None, last4=None, routing_number=None, status=None, token=None):
        """
        BillingBankAccount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'object': 'str',
            'account': 'str',
            'account_holder_name': 'str',
            'account_holder_type': 'str',
            'bank_name': 'str',
            'country': 'str',
            'currency': 'str',
            'default_for_currency': 'bool',
            'fingerprint': 'str',
            'last4': 'str',
            'routing_number': 'str',
            'status': 'str',
            'token': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'object': 'object',
            'account': 'account',
            'account_holder_name': 'accountHolderName',
            'account_holder_type': 'accountHolderType',
            'bank_name': 'bankName',
            'country': 'country',
            'currency': 'currency',
            'default_for_currency': 'defaultForCurrency',
            'fingerprint': 'fingerprint',
            'last4': 'last4',
            'routing_number': 'routingNumber',
            'status': 'status',
            'token': 'token'
        }

        self._id = id
        self._object = object
        self._account = account
        self._account_holder_name = account_holder_name
        self._account_holder_type = account_holder_type
        self._bank_name = bank_name
        self._country = country
        self._currency = currency
        self._default_for_currency = default_for_currency
        self._fingerprint = fingerprint
        self._last4 = last4
        self._routing_number = routing_number
        self._status = status
        self._token = token


    @property
    def id(self):
        """
        Gets the id of this BillingBankAccount.


        :return: The id of this BillingBankAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingBankAccount.


        :param id: The id of this BillingBankAccount.
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """
        Gets the object of this BillingBankAccount.


        :return: The object of this BillingBankAccount.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this BillingBankAccount.


        :param object: The object of this BillingBankAccount.
        :type: str
        """

        self._object = object

    @property
    def account(self):
        """
        Gets the account of this BillingBankAccount.


        :return: The account of this BillingBankAccount.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this BillingBankAccount.


        :param account: The account of this BillingBankAccount.
        :type: str
        """

        self._account = account

    @property
    def account_holder_name(self):
        """
        Gets the account_holder_name of this BillingBankAccount.


        :return: The account_holder_name of this BillingBankAccount.
        :rtype: str
        """
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, account_holder_name):
        """
        Sets the account_holder_name of this BillingBankAccount.


        :param account_holder_name: The account_holder_name of this BillingBankAccount.
        :type: str
        """

        self._account_holder_name = account_holder_name

    @property
    def account_holder_type(self):
        """
        Gets the account_holder_type of this BillingBankAccount.


        :return: The account_holder_type of this BillingBankAccount.
        :rtype: str
        """
        return self._account_holder_type

    @account_holder_type.setter
    def account_holder_type(self, account_holder_type):
        """
        Sets the account_holder_type of this BillingBankAccount.


        :param account_holder_type: The account_holder_type of this BillingBankAccount.
        :type: str
        """

        self._account_holder_type = account_holder_type

    @property
    def bank_name(self):
        """
        Gets the bank_name of this BillingBankAccount.


        :return: The bank_name of this BillingBankAccount.
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """
        Sets the bank_name of this BillingBankAccount.


        :param bank_name: The bank_name of this BillingBankAccount.
        :type: str
        """

        self._bank_name = bank_name

    @property
    def country(self):
        """
        Gets the country of this BillingBankAccount.


        :return: The country of this BillingBankAccount.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingBankAccount.


        :param country: The country of this BillingBankAccount.
        :type: str
        """

        self._country = country

    @property
    def currency(self):
        """
        Gets the currency of this BillingBankAccount.


        :return: The currency of this BillingBankAccount.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this BillingBankAccount.


        :param currency: The currency of this BillingBankAccount.
        :type: str
        """

        self._currency = currency

    @property
    def default_for_currency(self):
        """
        Gets the default_for_currency of this BillingBankAccount.


        :return: The default_for_currency of this BillingBankAccount.
        :rtype: bool
        """
        return self._default_for_currency

    @default_for_currency.setter
    def default_for_currency(self, default_for_currency):
        """
        Sets the default_for_currency of this BillingBankAccount.


        :param default_for_currency: The default_for_currency of this BillingBankAccount.
        :type: bool
        """

        self._default_for_currency = default_for_currency

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this BillingBankAccount.


        :return: The fingerprint of this BillingBankAccount.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this BillingBankAccount.


        :param fingerprint: The fingerprint of this BillingBankAccount.
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def last4(self):
        """
        Gets the last4 of this BillingBankAccount.


        :return: The last4 of this BillingBankAccount.
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """
        Sets the last4 of this BillingBankAccount.


        :param last4: The last4 of this BillingBankAccount.
        :type: str
        """

        self._last4 = last4

    @property
    def routing_number(self):
        """
        Gets the routing_number of this BillingBankAccount.


        :return: The routing_number of this BillingBankAccount.
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """
        Sets the routing_number of this BillingBankAccount.


        :param routing_number: The routing_number of this BillingBankAccount.
        :type: str
        """

        self._routing_number = routing_number

    @property
    def status(self):
        """
        Gets the status of this BillingBankAccount.


        :return: The status of this BillingBankAccount.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BillingBankAccount.


        :param status: The status of this BillingBankAccount.
        :type: str
        """

        self._status = status

    @property
    def token(self):
        """
        Gets the token of this BillingBankAccount.


        :return: The token of this BillingBankAccount.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this BillingBankAccount.


        :param token: The token of this BillingBankAccount.
        :type: str
        """

        self._token = token

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