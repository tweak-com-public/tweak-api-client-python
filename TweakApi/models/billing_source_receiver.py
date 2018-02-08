# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.0
    
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


class BillingSourceReceiver(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address=None, amount_charged=None, amount_received=None, amount_returned=None, refund_attributes_method=None, refund_attributes_status=None, id=None):
        """
        BillingSourceReceiver - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'str',
            'amount_charged': 'float',
            'amount_received': 'float',
            'amount_returned': 'float',
            'refund_attributes_method': 'str',
            'refund_attributes_status': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'amount_charged': 'amountCharged',
            'amount_received': 'amountReceived',
            'amount_returned': 'amountReturned',
            'refund_attributes_method': 'refundAttributesMethod',
            'refund_attributes_status': 'refundAttributesStatus',
            'id': 'id'
        }

        self._address = address
        self._amount_charged = amount_charged
        self._amount_received = amount_received
        self._amount_returned = amount_returned
        self._refund_attributes_method = refund_attributes_method
        self._refund_attributes_status = refund_attributes_status
        self._id = id


    @property
    def address(self):
        """
        Gets the address of this BillingSourceReceiver.


        :return: The address of this BillingSourceReceiver.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this BillingSourceReceiver.


        :param address: The address of this BillingSourceReceiver.
        :type: str
        """

        self._address = address

    @property
    def amount_charged(self):
        """
        Gets the amount_charged of this BillingSourceReceiver.


        :return: The amount_charged of this BillingSourceReceiver.
        :rtype: float
        """
        return self._amount_charged

    @amount_charged.setter
    def amount_charged(self, amount_charged):
        """
        Sets the amount_charged of this BillingSourceReceiver.


        :param amount_charged: The amount_charged of this BillingSourceReceiver.
        :type: float
        """

        self._amount_charged = amount_charged

    @property
    def amount_received(self):
        """
        Gets the amount_received of this BillingSourceReceiver.


        :return: The amount_received of this BillingSourceReceiver.
        :rtype: float
        """
        return self._amount_received

    @amount_received.setter
    def amount_received(self, amount_received):
        """
        Sets the amount_received of this BillingSourceReceiver.


        :param amount_received: The amount_received of this BillingSourceReceiver.
        :type: float
        """

        self._amount_received = amount_received

    @property
    def amount_returned(self):
        """
        Gets the amount_returned of this BillingSourceReceiver.


        :return: The amount_returned of this BillingSourceReceiver.
        :rtype: float
        """
        return self._amount_returned

    @amount_returned.setter
    def amount_returned(self, amount_returned):
        """
        Sets the amount_returned of this BillingSourceReceiver.


        :param amount_returned: The amount_returned of this BillingSourceReceiver.
        :type: float
        """

        self._amount_returned = amount_returned

    @property
    def refund_attributes_method(self):
        """
        Gets the refund_attributes_method of this BillingSourceReceiver.


        :return: The refund_attributes_method of this BillingSourceReceiver.
        :rtype: str
        """
        return self._refund_attributes_method

    @refund_attributes_method.setter
    def refund_attributes_method(self, refund_attributes_method):
        """
        Sets the refund_attributes_method of this BillingSourceReceiver.


        :param refund_attributes_method: The refund_attributes_method of this BillingSourceReceiver.
        :type: str
        """

        self._refund_attributes_method = refund_attributes_method

    @property
    def refund_attributes_status(self):
        """
        Gets the refund_attributes_status of this BillingSourceReceiver.


        :return: The refund_attributes_status of this BillingSourceReceiver.
        :rtype: str
        """
        return self._refund_attributes_status

    @refund_attributes_status.setter
    def refund_attributes_status(self, refund_attributes_status):
        """
        Sets the refund_attributes_status of this BillingSourceReceiver.


        :param refund_attributes_status: The refund_attributes_status of this BillingSourceReceiver.
        :type: str
        """

        self._refund_attributes_status = refund_attributes_status

    @property
    def id(self):
        """
        Gets the id of this BillingSourceReceiver.


        :return: The id of this BillingSourceReceiver.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingSourceReceiver.


        :param id: The id of this BillingSourceReceiver.
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
