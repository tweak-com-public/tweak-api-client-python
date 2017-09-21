# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.1-beta.1
    
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


class BillingInvoiceLine(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, amount=None, currency=None, customer=None, date=None, description=None, discountable=None, invoice=None, period=None, plan=None, proration=None, quantity=None, subscription=None, subscription_item=None):
        """
        BillingInvoiceLine - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'amount': 'float',
            'currency': 'str',
            'customer': 'str',
            'date': 'datetime',
            'description': 'str',
            'discountable': 'bool',
            'invoice': 'str',
            'period': 'object',
            'plan': 'BillingPlan',
            'proration': 'bool',
            'quantity': 'float',
            'subscription': 'str',
            'subscription_item': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'amount': 'amount',
            'currency': 'currency',
            'customer': 'customer',
            'date': 'date',
            'description': 'description',
            'discountable': 'discountable',
            'invoice': 'invoice',
            'period': 'period',
            'plan': 'plan',
            'proration': 'proration',
            'quantity': 'quantity',
            'subscription': 'subscription',
            'subscription_item': 'subscriptionItem'
        }

        self._id = id
        self._amount = amount
        self._currency = currency
        self._customer = customer
        self._date = date
        self._description = description
        self._discountable = discountable
        self._invoice = invoice
        self._period = period
        self._plan = plan
        self._proration = proration
        self._quantity = quantity
        self._subscription = subscription
        self._subscription_item = subscription_item


    @property
    def id(self):
        """
        Gets the id of this BillingInvoiceLine.


        :return: The id of this BillingInvoiceLine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingInvoiceLine.


        :param id: The id of this BillingInvoiceLine.
        :type: str
        """

        self._id = id

    @property
    def amount(self):
        """
        Gets the amount of this BillingInvoiceLine.


        :return: The amount of this BillingInvoiceLine.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this BillingInvoiceLine.


        :param amount: The amount of this BillingInvoiceLine.
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """
        Gets the currency of this BillingInvoiceLine.


        :return: The currency of this BillingInvoiceLine.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this BillingInvoiceLine.


        :param currency: The currency of this BillingInvoiceLine.
        :type: str
        """

        self._currency = currency

    @property
    def customer(self):
        """
        Gets the customer of this BillingInvoiceLine.


        :return: The customer of this BillingInvoiceLine.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this BillingInvoiceLine.


        :param customer: The customer of this BillingInvoiceLine.
        :type: str
        """

        self._customer = customer

    @property
    def date(self):
        """
        Gets the date of this BillingInvoiceLine.


        :return: The date of this BillingInvoiceLine.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this BillingInvoiceLine.


        :param date: The date of this BillingInvoiceLine.
        :type: datetime
        """

        self._date = date

    @property
    def description(self):
        """
        Gets the description of this BillingInvoiceLine.


        :return: The description of this BillingInvoiceLine.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BillingInvoiceLine.


        :param description: The description of this BillingInvoiceLine.
        :type: str
        """

        self._description = description

    @property
    def discountable(self):
        """
        Gets the discountable of this BillingInvoiceLine.


        :return: The discountable of this BillingInvoiceLine.
        :rtype: bool
        """
        return self._discountable

    @discountable.setter
    def discountable(self, discountable):
        """
        Sets the discountable of this BillingInvoiceLine.


        :param discountable: The discountable of this BillingInvoiceLine.
        :type: bool
        """

        self._discountable = discountable

    @property
    def invoice(self):
        """
        Gets the invoice of this BillingInvoiceLine.


        :return: The invoice of this BillingInvoiceLine.
        :rtype: str
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """
        Sets the invoice of this BillingInvoiceLine.


        :param invoice: The invoice of this BillingInvoiceLine.
        :type: str
        """

        self._invoice = invoice

    @property
    def period(self):
        """
        Gets the period of this BillingInvoiceLine.


        :return: The period of this BillingInvoiceLine.
        :rtype: object
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this BillingInvoiceLine.


        :param period: The period of this BillingInvoiceLine.
        :type: object
        """

        self._period = period

    @property
    def plan(self):
        """
        Gets the plan of this BillingInvoiceLine.


        :return: The plan of this BillingInvoiceLine.
        :rtype: BillingPlan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """
        Sets the plan of this BillingInvoiceLine.


        :param plan: The plan of this BillingInvoiceLine.
        :type: BillingPlan
        """

        self._plan = plan

    @property
    def proration(self):
        """
        Gets the proration of this BillingInvoiceLine.


        :return: The proration of this BillingInvoiceLine.
        :rtype: bool
        """
        return self._proration

    @proration.setter
    def proration(self, proration):
        """
        Sets the proration of this BillingInvoiceLine.


        :param proration: The proration of this BillingInvoiceLine.
        :type: bool
        """

        self._proration = proration

    @property
    def quantity(self):
        """
        Gets the quantity of this BillingInvoiceLine.


        :return: The quantity of this BillingInvoiceLine.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this BillingInvoiceLine.


        :param quantity: The quantity of this BillingInvoiceLine.
        :type: float
        """

        self._quantity = quantity

    @property
    def subscription(self):
        """
        Gets the subscription of this BillingInvoiceLine.


        :return: The subscription of this BillingInvoiceLine.
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this BillingInvoiceLine.


        :param subscription: The subscription of this BillingInvoiceLine.
        :type: str
        """

        self._subscription = subscription

    @property
    def subscription_item(self):
        """
        Gets the subscription_item of this BillingInvoiceLine.


        :return: The subscription_item of this BillingInvoiceLine.
        :rtype: str
        """
        return self._subscription_item

    @subscription_item.setter
    def subscription_item(self, subscription_item):
        """
        Sets the subscription_item of this BillingInvoiceLine.


        :param subscription_item: The subscription_item of this BillingInvoiceLine.
        :type: str
        """

        self._subscription_item = subscription_item

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
