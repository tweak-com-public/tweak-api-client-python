# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.13
    
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


class BillingSubscription(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, coupon=None, tax_percent=None, trial_period_days=None, subscribed_plans=None, discount=None, status=None, cancel_at_period_end=None, created=None, start=None, ended_at=None, trial_end=None, trial_start=None, current_period_end=None, current_period_start=None, canceled_at=None):
        """
        BillingSubscription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'coupon': 'str',
            'tax_percent': 'float',
            'trial_period_days': 'float',
            'subscribed_plans': 'list[BillingSubscriptionItem]',
            'discount': 'float',
            'status': 'str',
            'cancel_at_period_end': 'bool',
            'created': 'datetime',
            'start': 'datetime',
            'ended_at': 'datetime',
            'trial_end': 'datetime',
            'trial_start': 'datetime',
            'current_period_end': 'datetime',
            'current_period_start': 'datetime',
            'canceled_at': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'coupon': 'coupon',
            'tax_percent': 'taxPercent',
            'trial_period_days': 'trialPeriodDays',
            'subscribed_plans': 'subscribedPlans',
            'discount': 'discount',
            'status': 'status',
            'cancel_at_period_end': 'cancelAtPeriodEnd',
            'created': 'created',
            'start': 'start',
            'ended_at': 'endedAt',
            'trial_end': 'trialEnd',
            'trial_start': 'trialStart',
            'current_period_end': 'currentPeriodEnd',
            'current_period_start': 'currentPeriodStart',
            'canceled_at': 'canceledAt'
        }

        self._id = id
        self._coupon = coupon
        self._tax_percent = tax_percent
        self._trial_period_days = trial_period_days
        self._subscribed_plans = subscribed_plans
        self._discount = discount
        self._status = status
        self._cancel_at_period_end = cancel_at_period_end
        self._created = created
        self._start = start
        self._ended_at = ended_at
        self._trial_end = trial_end
        self._trial_start = trial_start
        self._current_period_end = current_period_end
        self._current_period_start = current_period_start
        self._canceled_at = canceled_at


    @property
    def id(self):
        """
        Gets the id of this BillingSubscription.


        :return: The id of this BillingSubscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingSubscription.


        :param id: The id of this BillingSubscription.
        :type: str
        """

        self._id = id

    @property
    def coupon(self):
        """
        Gets the coupon of this BillingSubscription.


        :return: The coupon of this BillingSubscription.
        :rtype: str
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """
        Sets the coupon of this BillingSubscription.


        :param coupon: The coupon of this BillingSubscription.
        :type: str
        """

        self._coupon = coupon

    @property
    def tax_percent(self):
        """
        Gets the tax_percent of this BillingSubscription.


        :return: The tax_percent of this BillingSubscription.
        :rtype: float
        """
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, tax_percent):
        """
        Sets the tax_percent of this BillingSubscription.


        :param tax_percent: The tax_percent of this BillingSubscription.
        :type: float
        """

        self._tax_percent = tax_percent

    @property
    def trial_period_days(self):
        """
        Gets the trial_period_days of this BillingSubscription.


        :return: The trial_period_days of this BillingSubscription.
        :rtype: float
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """
        Sets the trial_period_days of this BillingSubscription.


        :param trial_period_days: The trial_period_days of this BillingSubscription.
        :type: float
        """

        self._trial_period_days = trial_period_days

    @property
    def subscribed_plans(self):
        """
        Gets the subscribed_plans of this BillingSubscription.


        :return: The subscribed_plans of this BillingSubscription.
        :rtype: list[BillingSubscriptionItem]
        """
        return self._subscribed_plans

    @subscribed_plans.setter
    def subscribed_plans(self, subscribed_plans):
        """
        Sets the subscribed_plans of this BillingSubscription.


        :param subscribed_plans: The subscribed_plans of this BillingSubscription.
        :type: list[BillingSubscriptionItem]
        """

        self._subscribed_plans = subscribed_plans

    @property
    def discount(self):
        """
        Gets the discount of this BillingSubscription.


        :return: The discount of this BillingSubscription.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """
        Sets the discount of this BillingSubscription.


        :param discount: The discount of this BillingSubscription.
        :type: float
        """

        self._discount = discount

    @property
    def status(self):
        """
        Gets the status of this BillingSubscription.


        :return: The status of this BillingSubscription.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BillingSubscription.


        :param status: The status of this BillingSubscription.
        :type: str
        """

        self._status = status

    @property
    def cancel_at_period_end(self):
        """
        Gets the cancel_at_period_end of this BillingSubscription.


        :return: The cancel_at_period_end of this BillingSubscription.
        :rtype: bool
        """
        return self._cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, cancel_at_period_end):
        """
        Sets the cancel_at_period_end of this BillingSubscription.


        :param cancel_at_period_end: The cancel_at_period_end of this BillingSubscription.
        :type: bool
        """

        self._cancel_at_period_end = cancel_at_period_end

    @property
    def created(self):
        """
        Gets the created of this BillingSubscription.


        :return: The created of this BillingSubscription.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this BillingSubscription.


        :param created: The created of this BillingSubscription.
        :type: datetime
        """

        self._created = created

    @property
    def start(self):
        """
        Gets the start of this BillingSubscription.


        :return: The start of this BillingSubscription.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this BillingSubscription.


        :param start: The start of this BillingSubscription.
        :type: datetime
        """

        self._start = start

    @property
    def ended_at(self):
        """
        Gets the ended_at of this BillingSubscription.


        :return: The ended_at of this BillingSubscription.
        :rtype: datetime
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """
        Sets the ended_at of this BillingSubscription.


        :param ended_at: The ended_at of this BillingSubscription.
        :type: datetime
        """

        self._ended_at = ended_at

    @property
    def trial_end(self):
        """
        Gets the trial_end of this BillingSubscription.


        :return: The trial_end of this BillingSubscription.
        :rtype: datetime
        """
        return self._trial_end

    @trial_end.setter
    def trial_end(self, trial_end):
        """
        Sets the trial_end of this BillingSubscription.


        :param trial_end: The trial_end of this BillingSubscription.
        :type: datetime
        """

        self._trial_end = trial_end

    @property
    def trial_start(self):
        """
        Gets the trial_start of this BillingSubscription.


        :return: The trial_start of this BillingSubscription.
        :rtype: datetime
        """
        return self._trial_start

    @trial_start.setter
    def trial_start(self, trial_start):
        """
        Sets the trial_start of this BillingSubscription.


        :param trial_start: The trial_start of this BillingSubscription.
        :type: datetime
        """

        self._trial_start = trial_start

    @property
    def current_period_end(self):
        """
        Gets the current_period_end of this BillingSubscription.


        :return: The current_period_end of this BillingSubscription.
        :rtype: datetime
        """
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, current_period_end):
        """
        Sets the current_period_end of this BillingSubscription.


        :param current_period_end: The current_period_end of this BillingSubscription.
        :type: datetime
        """

        self._current_period_end = current_period_end

    @property
    def current_period_start(self):
        """
        Gets the current_period_start of this BillingSubscription.


        :return: The current_period_start of this BillingSubscription.
        :rtype: datetime
        """
        return self._current_period_start

    @current_period_start.setter
    def current_period_start(self, current_period_start):
        """
        Sets the current_period_start of this BillingSubscription.


        :param current_period_start: The current_period_start of this BillingSubscription.
        :type: datetime
        """

        self._current_period_start = current_period_start

    @property
    def canceled_at(self):
        """
        Gets the canceled_at of this BillingSubscription.


        :return: The canceled_at of this BillingSubscription.
        :rtype: datetime
        """
        return self._canceled_at

    @canceled_at.setter
    def canceled_at(self, canceled_at):
        """
        Sets the canceled_at of this BillingSubscription.


        :param canceled_at: The canceled_at of this BillingSubscription.
        :type: datetime
        """

        self._canceled_at = canceled_at

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
