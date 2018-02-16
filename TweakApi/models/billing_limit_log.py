# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.10
    
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


class BillingLimitLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, value=None, operation=None, before=None, after=None, limit=None, message=None, created=None, modified=None, id=None, billing_id=None, billing=None):
        """
        BillingLimitLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'value': 'str',
            'operation': 'str',
            'before': 'BillingLimitCounter',
            'after': 'BillingLimitCounter',
            'limit': 'str',
            'message': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'billing_id': 'str',
            'billing': 'Billing'
        }

        self.attribute_map = {
            'value': 'value',
            'operation': 'operation',
            'before': 'before',
            'after': 'after',
            'limit': 'limit',
            'message': 'message',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'billing_id': 'billingId',
            'billing': 'billing'
        }

        self._value = value
        self._operation = operation
        self._before = before
        self._after = after
        self._limit = limit
        self._message = message
        self._created = created
        self._modified = modified
        self._id = id
        self._billing_id = billing_id
        self._billing = billing


    @property
    def value(self):
        """
        Gets the value of this BillingLimitLog.


        :return: The value of this BillingLimitLog.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this BillingLimitLog.


        :param value: The value of this BillingLimitLog.
        :type: str
        """

        self._value = value

    @property
    def operation(self):
        """
        Gets the operation of this BillingLimitLog.


        :return: The operation of this BillingLimitLog.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this BillingLimitLog.


        :param operation: The operation of this BillingLimitLog.
        :type: str
        """
        allowed_values = ["increase", "decrease"]
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def before(self):
        """
        Gets the before of this BillingLimitLog.


        :return: The before of this BillingLimitLog.
        :rtype: BillingLimitCounter
        """
        return self._before

    @before.setter
    def before(self, before):
        """
        Sets the before of this BillingLimitLog.


        :param before: The before of this BillingLimitLog.
        :type: BillingLimitCounter
        """

        self._before = before

    @property
    def after(self):
        """
        Gets the after of this BillingLimitLog.


        :return: The after of this BillingLimitLog.
        :rtype: BillingLimitCounter
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this BillingLimitLog.


        :param after: The after of this BillingLimitLog.
        :type: BillingLimitCounter
        """

        self._after = after

    @property
    def limit(self):
        """
        Gets the limit of this BillingLimitLog.


        :return: The limit of this BillingLimitLog.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this BillingLimitLog.


        :param limit: The limit of this BillingLimitLog.
        :type: str
        """
        allowed_values = ["teamMember", "uploader", "portal", "jpeg", "proof", "highResPdf", "storage", "stockImageLibrary", "productDbRecord", "bandwidth", "printerApi"]
        if limit not in allowed_values:
            raise ValueError(
                "Invalid value for `limit` ({0}), must be one of {1}"
                .format(limit, allowed_values)
            )

        self._limit = limit

    @property
    def message(self):
        """
        Gets the message of this BillingLimitLog.


        :return: The message of this BillingLimitLog.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BillingLimitLog.


        :param message: The message of this BillingLimitLog.
        :type: str
        """

        self._message = message

    @property
    def created(self):
        """
        Gets the created of this BillingLimitLog.


        :return: The created of this BillingLimitLog.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this BillingLimitLog.


        :param created: The created of this BillingLimitLog.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this BillingLimitLog.


        :return: The modified of this BillingLimitLog.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this BillingLimitLog.


        :param modified: The modified of this BillingLimitLog.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this BillingLimitLog.


        :return: The id of this BillingLimitLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingLimitLog.


        :param id: The id of this BillingLimitLog.
        :type: str
        """

        self._id = id

    @property
    def billing_id(self):
        """
        Gets the billing_id of this BillingLimitLog.


        :return: The billing_id of this BillingLimitLog.
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """
        Sets the billing_id of this BillingLimitLog.


        :param billing_id: The billing_id of this BillingLimitLog.
        :type: str
        """

        self._billing_id = billing_id

    @property
    def billing(self):
        """
        Gets the billing of this BillingLimitLog.


        :return: The billing of this BillingLimitLog.
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """
        Sets the billing of this BillingLimitLog.


        :param billing: The billing of this BillingLimitLog.
        :type: Billing
        """

        self._billing = billing

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
