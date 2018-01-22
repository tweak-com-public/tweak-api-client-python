# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.2
    
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


class BillingPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, amount=None, currency=None, interval=None, interval_count=None, statement_descriptor=None, statement_description=None, trial_period_days=None, type=None, limit=None, created=None):
        """
        BillingPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'amount': 'float',
            'currency': 'str',
            'interval': 'str',
            'interval_count': 'float',
            'statement_descriptor': 'str',
            'statement_description': 'str',
            'trial_period_days': 'float',
            'type': 'str',
            'limit': 'BillingLimit',
            'created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'amount': 'amount',
            'currency': 'currency',
            'interval': 'interval',
            'interval_count': 'intervalCount',
            'statement_descriptor': 'statementDescriptor',
            'statement_description': 'statementDescription',
            'trial_period_days': 'trialPeriodDays',
            'type': 'type',
            'limit': 'limit',
            'created': 'created'
        }

        self._id = id
        self._name = name
        self._amount = amount
        self._currency = currency
        self._interval = interval
        self._interval_count = interval_count
        self._statement_descriptor = statement_descriptor
        self._statement_description = statement_description
        self._trial_period_days = trial_period_days
        self._type = type
        self._limit = limit
        self._created = created


    @property
    def id(self):
        """
        Gets the id of this BillingPlan.


        :return: The id of this BillingPlan.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingPlan.


        :param id: The id of this BillingPlan.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BillingPlan.


        :return: The name of this BillingPlan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BillingPlan.


        :param name: The name of this BillingPlan.
        :type: str
        """

        self._name = name

    @property
    def amount(self):
        """
        Gets the amount of this BillingPlan.


        :return: The amount of this BillingPlan.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this BillingPlan.


        :param amount: The amount of this BillingPlan.
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """
        Gets the currency of this BillingPlan.


        :return: The currency of this BillingPlan.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this BillingPlan.


        :param currency: The currency of this BillingPlan.
        :type: str
        """

        self._currency = currency

    @property
    def interval(self):
        """
        Gets the interval of this BillingPlan.


        :return: The interval of this BillingPlan.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this BillingPlan.


        :param interval: The interval of this BillingPlan.
        :type: str
        """

        self._interval = interval

    @property
    def interval_count(self):
        """
        Gets the interval_count of this BillingPlan.


        :return: The interval_count of this BillingPlan.
        :rtype: float
        """
        return self._interval_count

    @interval_count.setter
    def interval_count(self, interval_count):
        """
        Sets the interval_count of this BillingPlan.


        :param interval_count: The interval_count of this BillingPlan.
        :type: float
        """

        self._interval_count = interval_count

    @property
    def statement_descriptor(self):
        """
        Gets the statement_descriptor of this BillingPlan.


        :return: The statement_descriptor of this BillingPlan.
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """
        Sets the statement_descriptor of this BillingPlan.


        :param statement_descriptor: The statement_descriptor of this BillingPlan.
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def statement_description(self):
        """
        Gets the statement_description of this BillingPlan.


        :return: The statement_description of this BillingPlan.
        :rtype: str
        """
        return self._statement_description

    @statement_description.setter
    def statement_description(self, statement_description):
        """
        Sets the statement_description of this BillingPlan.


        :param statement_description: The statement_description of this BillingPlan.
        :type: str
        """

        self._statement_description = statement_description

    @property
    def trial_period_days(self):
        """
        Gets the trial_period_days of this BillingPlan.


        :return: The trial_period_days of this BillingPlan.
        :rtype: float
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """
        Sets the trial_period_days of this BillingPlan.


        :param trial_period_days: The trial_period_days of this BillingPlan.
        :type: float
        """

        self._trial_period_days = trial_period_days

    @property
    def type(self):
        """
        Gets the type of this BillingPlan.


        :return: The type of this BillingPlan.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BillingPlan.


        :param type: The type of this BillingPlan.
        :type: str
        """
        allowed_values = ["plan", "additional"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def limit(self):
        """
        Gets the limit of this BillingPlan.


        :return: The limit of this BillingPlan.
        :rtype: BillingLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this BillingPlan.


        :param limit: The limit of this BillingPlan.
        :type: BillingLimit
        """

        self._limit = limit

    @property
    def created(self):
        """
        Gets the created of this BillingPlan.


        :return: The created of this BillingPlan.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this BillingPlan.


        :param created: The created of this BillingPlan.
        :type: datetime
        """

        self._created = created

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
