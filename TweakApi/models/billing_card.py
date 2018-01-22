# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.4
    
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


class BillingCard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cardholder_name=None, exp_month=None, exp_year=None, token=None, number=None, cvc=None, cvc_check=None, last4=None, brand=None, country=None, funding=None, type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, stripe_card_id=None, id=None):
        """
        BillingCard - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cardholder_name': 'str',
            'exp_month': 'float',
            'exp_year': 'float',
            'token': 'str',
            'number': 'str',
            'cvc': 'str',
            'cvc_check': 'str',
            'last4': 'str',
            'brand': 'str',
            'country': 'str',
            'funding': 'str',
            'type': 'str',
            'address_city': 'str',
            'address_country': 'str',
            'address_line1': 'str',
            'address_line2': 'str',
            'address_state': 'str',
            'address_zip': 'str',
            'stripe_card_id': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'cardholder_name': 'cardholderName',
            'exp_month': 'expMonth',
            'exp_year': 'expYear',
            'token': 'token',
            'number': 'number',
            'cvc': 'cvc',
            'cvc_check': 'cvcCheck',
            'last4': 'last4',
            'brand': 'brand',
            'country': 'country',
            'funding': 'funding',
            'type': 'type',
            'address_city': 'addressCity',
            'address_country': 'addressCountry',
            'address_line1': 'addressLine1',
            'address_line2': 'addressLine2',
            'address_state': 'addressState',
            'address_zip': 'addressZip',
            'stripe_card_id': 'stripeCardId',
            'id': 'id'
        }

        self._cardholder_name = cardholder_name
        self._exp_month = exp_month
        self._exp_year = exp_year
        self._token = token
        self._number = number
        self._cvc = cvc
        self._cvc_check = cvc_check
        self._last4 = last4
        self._brand = brand
        self._country = country
        self._funding = funding
        self._type = type
        self._address_city = address_city
        self._address_country = address_country
        self._address_line1 = address_line1
        self._address_line2 = address_line2
        self._address_state = address_state
        self._address_zip = address_zip
        self._stripe_card_id = stripe_card_id
        self._id = id


    @property
    def cardholder_name(self):
        """
        Gets the cardholder_name of this BillingCard.


        :return: The cardholder_name of this BillingCard.
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """
        Sets the cardholder_name of this BillingCard.


        :param cardholder_name: The cardholder_name of this BillingCard.
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def exp_month(self):
        """
        Gets the exp_month of this BillingCard.


        :return: The exp_month of this BillingCard.
        :rtype: float
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """
        Sets the exp_month of this BillingCard.


        :param exp_month: The exp_month of this BillingCard.
        :type: float
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """
        Gets the exp_year of this BillingCard.


        :return: The exp_year of this BillingCard.
        :rtype: float
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """
        Sets the exp_year of this BillingCard.


        :param exp_year: The exp_year of this BillingCard.
        :type: float
        """

        self._exp_year = exp_year

    @property
    def token(self):
        """
        Gets the token of this BillingCard.


        :return: The token of this BillingCard.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this BillingCard.


        :param token: The token of this BillingCard.
        :type: str
        """

        self._token = token

    @property
    def number(self):
        """
        Gets the number of this BillingCard.


        :return: The number of this BillingCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this BillingCard.


        :param number: The number of this BillingCard.
        :type: str
        """

        self._number = number

    @property
    def cvc(self):
        """
        Gets the cvc of this BillingCard.


        :return: The cvc of this BillingCard.
        :rtype: str
        """
        return self._cvc

    @cvc.setter
    def cvc(self, cvc):
        """
        Sets the cvc of this BillingCard.


        :param cvc: The cvc of this BillingCard.
        :type: str
        """

        self._cvc = cvc

    @property
    def cvc_check(self):
        """
        Gets the cvc_check of this BillingCard.


        :return: The cvc_check of this BillingCard.
        :rtype: str
        """
        return self._cvc_check

    @cvc_check.setter
    def cvc_check(self, cvc_check):
        """
        Sets the cvc_check of this BillingCard.


        :param cvc_check: The cvc_check of this BillingCard.
        :type: str
        """

        self._cvc_check = cvc_check

    @property
    def last4(self):
        """
        Gets the last4 of this BillingCard.


        :return: The last4 of this BillingCard.
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """
        Sets the last4 of this BillingCard.


        :param last4: The last4 of this BillingCard.
        :type: str
        """

        self._last4 = last4

    @property
    def brand(self):
        """
        Gets the brand of this BillingCard.


        :return: The brand of this BillingCard.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """
        Sets the brand of this BillingCard.


        :param brand: The brand of this BillingCard.
        :type: str
        """

        self._brand = brand

    @property
    def country(self):
        """
        Gets the country of this BillingCard.


        :return: The country of this BillingCard.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingCard.


        :param country: The country of this BillingCard.
        :type: str
        """

        self._country = country

    @property
    def funding(self):
        """
        Gets the funding of this BillingCard.


        :return: The funding of this BillingCard.
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """
        Sets the funding of this BillingCard.


        :param funding: The funding of this BillingCard.
        :type: str
        """

        self._funding = funding

    @property
    def type(self):
        """
        Gets the type of this BillingCard.


        :return: The type of this BillingCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BillingCard.


        :param type: The type of this BillingCard.
        :type: str
        """

        self._type = type

    @property
    def address_city(self):
        """
        Gets the address_city of this BillingCard.


        :return: The address_city of this BillingCard.
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """
        Sets the address_city of this BillingCard.


        :param address_city: The address_city of this BillingCard.
        :type: str
        """

        self._address_city = address_city

    @property
    def address_country(self):
        """
        Gets the address_country of this BillingCard.


        :return: The address_country of this BillingCard.
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """
        Sets the address_country of this BillingCard.


        :param address_country: The address_country of this BillingCard.
        :type: str
        """

        self._address_country = address_country

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this BillingCard.


        :return: The address_line1 of this BillingCard.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this BillingCard.


        :param address_line1: The address_line1 of this BillingCard.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this BillingCard.


        :return: The address_line2 of this BillingCard.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this BillingCard.


        :param address_line2: The address_line2 of this BillingCard.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_state(self):
        """
        Gets the address_state of this BillingCard.


        :return: The address_state of this BillingCard.
        :rtype: str
        """
        return self._address_state

    @address_state.setter
    def address_state(self, address_state):
        """
        Sets the address_state of this BillingCard.


        :param address_state: The address_state of this BillingCard.
        :type: str
        """

        self._address_state = address_state

    @property
    def address_zip(self):
        """
        Gets the address_zip of this BillingCard.


        :return: The address_zip of this BillingCard.
        :rtype: str
        """
        return self._address_zip

    @address_zip.setter
    def address_zip(self, address_zip):
        """
        Sets the address_zip of this BillingCard.


        :param address_zip: The address_zip of this BillingCard.
        :type: str
        """

        self._address_zip = address_zip

    @property
    def stripe_card_id(self):
        """
        Gets the stripe_card_id of this BillingCard.


        :return: The stripe_card_id of this BillingCard.
        :rtype: str
        """
        return self._stripe_card_id

    @stripe_card_id.setter
    def stripe_card_id(self, stripe_card_id):
        """
        Sets the stripe_card_id of this BillingCard.


        :param stripe_card_id: The stripe_card_id of this BillingCard.
        :type: str
        """

        self._stripe_card_id = stripe_card_id

    @property
    def id(self):
        """
        Gets the id of this BillingCard.


        :return: The id of this BillingCard.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingCard.


        :param id: The id of this BillingCard.
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
