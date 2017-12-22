# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-alpha.9
    
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


class BillingInvoice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, amount_due=None, attempt_count=None, attempted=None, charged=None, closed=None, currency=None, customer=None, date=None, description=None, ending_balance=None, forgiven=None, lines=None, next_payment_attempt=None, paid=None, period_end=None, period_start=None, number=None, recipt_number=None, starting_balance=None, statement_descriptor=None, subscription=None, subscription_proration_date=None, subtotal=None, tax=None, total=None):
        """
        BillingInvoice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'amount_due': 'float',
            'attempt_count': 'float',
            'attempted': 'bool',
            'charged': 'bool',
            'closed': 'bool',
            'currency': 'str',
            'customer': 'str',
            'date': 'datetime',
            'description': 'str',
            'ending_balance': 'float',
            'forgiven': 'bool',
            'lines': 'list[BillingInvoiceLine]',
            'next_payment_attempt': 'datetime',
            'paid': 'bool',
            'period_end': 'datetime',
            'period_start': 'datetime',
            'number': 'str',
            'recipt_number': 'str',
            'starting_balance': 'float',
            'statement_descriptor': 'str',
            'subscription': 'str',
            'subscription_proration_date': 'float',
            'subtotal': 'float',
            'tax': 'float',
            'total': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'amount_due': 'amountDue',
            'attempt_count': 'attemptCount',
            'attempted': 'attempted',
            'charged': 'charged',
            'closed': 'closed',
            'currency': 'currency',
            'customer': 'customer',
            'date': 'date',
            'description': 'description',
            'ending_balance': 'endingBalance',
            'forgiven': 'forgiven',
            'lines': 'lines',
            'next_payment_attempt': 'nextPaymentAttempt',
            'paid': 'paid',
            'period_end': 'periodEnd',
            'period_start': 'periodStart',
            'number': 'number',
            'recipt_number': 'reciptNumber',
            'starting_balance': 'startingBalance',
            'statement_descriptor': 'statementDescriptor',
            'subscription': 'subscription',
            'subscription_proration_date': 'subscriptionProrationDate',
            'subtotal': 'subtotal',
            'tax': 'tax',
            'total': 'total'
        }

        self._id = id
        self._amount_due = amount_due
        self._attempt_count = attempt_count
        self._attempted = attempted
        self._charged = charged
        self._closed = closed
        self._currency = currency
        self._customer = customer
        self._date = date
        self._description = description
        self._ending_balance = ending_balance
        self._forgiven = forgiven
        self._lines = lines
        self._next_payment_attempt = next_payment_attempt
        self._paid = paid
        self._period_end = period_end
        self._period_start = period_start
        self._number = number
        self._recipt_number = recipt_number
        self._starting_balance = starting_balance
        self._statement_descriptor = statement_descriptor
        self._subscription = subscription
        self._subscription_proration_date = subscription_proration_date
        self._subtotal = subtotal
        self._tax = tax
        self._total = total


    @property
    def id(self):
        """
        Gets the id of this BillingInvoice.


        :return: The id of this BillingInvoice.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingInvoice.


        :param id: The id of this BillingInvoice.
        :type: str
        """

        self._id = id

    @property
    def amount_due(self):
        """
        Gets the amount_due of this BillingInvoice.


        :return: The amount_due of this BillingInvoice.
        :rtype: float
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """
        Sets the amount_due of this BillingInvoice.


        :param amount_due: The amount_due of this BillingInvoice.
        :type: float
        """

        self._amount_due = amount_due

    @property
    def attempt_count(self):
        """
        Gets the attempt_count of this BillingInvoice.


        :return: The attempt_count of this BillingInvoice.
        :rtype: float
        """
        return self._attempt_count

    @attempt_count.setter
    def attempt_count(self, attempt_count):
        """
        Sets the attempt_count of this BillingInvoice.


        :param attempt_count: The attempt_count of this BillingInvoice.
        :type: float
        """

        self._attempt_count = attempt_count

    @property
    def attempted(self):
        """
        Gets the attempted of this BillingInvoice.


        :return: The attempted of this BillingInvoice.
        :rtype: bool
        """
        return self._attempted

    @attempted.setter
    def attempted(self, attempted):
        """
        Sets the attempted of this BillingInvoice.


        :param attempted: The attempted of this BillingInvoice.
        :type: bool
        """

        self._attempted = attempted

    @property
    def charged(self):
        """
        Gets the charged of this BillingInvoice.


        :return: The charged of this BillingInvoice.
        :rtype: bool
        """
        return self._charged

    @charged.setter
    def charged(self, charged):
        """
        Sets the charged of this BillingInvoice.


        :param charged: The charged of this BillingInvoice.
        :type: bool
        """

        self._charged = charged

    @property
    def closed(self):
        """
        Gets the closed of this BillingInvoice.


        :return: The closed of this BillingInvoice.
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """
        Sets the closed of this BillingInvoice.


        :param closed: The closed of this BillingInvoice.
        :type: bool
        """

        self._closed = closed

    @property
    def currency(self):
        """
        Gets the currency of this BillingInvoice.


        :return: The currency of this BillingInvoice.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this BillingInvoice.


        :param currency: The currency of this BillingInvoice.
        :type: str
        """

        self._currency = currency

    @property
    def customer(self):
        """
        Gets the customer of this BillingInvoice.


        :return: The customer of this BillingInvoice.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this BillingInvoice.


        :param customer: The customer of this BillingInvoice.
        :type: str
        """

        self._customer = customer

    @property
    def date(self):
        """
        Gets the date of this BillingInvoice.


        :return: The date of this BillingInvoice.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this BillingInvoice.


        :param date: The date of this BillingInvoice.
        :type: datetime
        """

        self._date = date

    @property
    def description(self):
        """
        Gets the description of this BillingInvoice.


        :return: The description of this BillingInvoice.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BillingInvoice.


        :param description: The description of this BillingInvoice.
        :type: str
        """

        self._description = description

    @property
    def ending_balance(self):
        """
        Gets the ending_balance of this BillingInvoice.


        :return: The ending_balance of this BillingInvoice.
        :rtype: float
        """
        return self._ending_balance

    @ending_balance.setter
    def ending_balance(self, ending_balance):
        """
        Sets the ending_balance of this BillingInvoice.


        :param ending_balance: The ending_balance of this BillingInvoice.
        :type: float
        """

        self._ending_balance = ending_balance

    @property
    def forgiven(self):
        """
        Gets the forgiven of this BillingInvoice.


        :return: The forgiven of this BillingInvoice.
        :rtype: bool
        """
        return self._forgiven

    @forgiven.setter
    def forgiven(self, forgiven):
        """
        Sets the forgiven of this BillingInvoice.


        :param forgiven: The forgiven of this BillingInvoice.
        :type: bool
        """

        self._forgiven = forgiven

    @property
    def lines(self):
        """
        Gets the lines of this BillingInvoice.


        :return: The lines of this BillingInvoice.
        :rtype: list[BillingInvoiceLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this BillingInvoice.


        :param lines: The lines of this BillingInvoice.
        :type: list[BillingInvoiceLine]
        """

        self._lines = lines

    @property
    def next_payment_attempt(self):
        """
        Gets the next_payment_attempt of this BillingInvoice.


        :return: The next_payment_attempt of this BillingInvoice.
        :rtype: datetime
        """
        return self._next_payment_attempt

    @next_payment_attempt.setter
    def next_payment_attempt(self, next_payment_attempt):
        """
        Sets the next_payment_attempt of this BillingInvoice.


        :param next_payment_attempt: The next_payment_attempt of this BillingInvoice.
        :type: datetime
        """

        self._next_payment_attempt = next_payment_attempt

    @property
    def paid(self):
        """
        Gets the paid of this BillingInvoice.


        :return: The paid of this BillingInvoice.
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """
        Sets the paid of this BillingInvoice.


        :param paid: The paid of this BillingInvoice.
        :type: bool
        """

        self._paid = paid

    @property
    def period_end(self):
        """
        Gets the period_end of this BillingInvoice.


        :return: The period_end of this BillingInvoice.
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """
        Sets the period_end of this BillingInvoice.


        :param period_end: The period_end of this BillingInvoice.
        :type: datetime
        """

        self._period_end = period_end

    @property
    def period_start(self):
        """
        Gets the period_start of this BillingInvoice.


        :return: The period_start of this BillingInvoice.
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """
        Sets the period_start of this BillingInvoice.


        :param period_start: The period_start of this BillingInvoice.
        :type: datetime
        """

        self._period_start = period_start

    @property
    def number(self):
        """
        Gets the number of this BillingInvoice.


        :return: The number of this BillingInvoice.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this BillingInvoice.


        :param number: The number of this BillingInvoice.
        :type: str
        """

        self._number = number

    @property
    def recipt_number(self):
        """
        Gets the recipt_number of this BillingInvoice.


        :return: The recipt_number of this BillingInvoice.
        :rtype: str
        """
        return self._recipt_number

    @recipt_number.setter
    def recipt_number(self, recipt_number):
        """
        Sets the recipt_number of this BillingInvoice.


        :param recipt_number: The recipt_number of this BillingInvoice.
        :type: str
        """

        self._recipt_number = recipt_number

    @property
    def starting_balance(self):
        """
        Gets the starting_balance of this BillingInvoice.


        :return: The starting_balance of this BillingInvoice.
        :rtype: float
        """
        return self._starting_balance

    @starting_balance.setter
    def starting_balance(self, starting_balance):
        """
        Sets the starting_balance of this BillingInvoice.


        :param starting_balance: The starting_balance of this BillingInvoice.
        :type: float
        """

        self._starting_balance = starting_balance

    @property
    def statement_descriptor(self):
        """
        Gets the statement_descriptor of this BillingInvoice.


        :return: The statement_descriptor of this BillingInvoice.
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """
        Sets the statement_descriptor of this BillingInvoice.


        :param statement_descriptor: The statement_descriptor of this BillingInvoice.
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def subscription(self):
        """
        Gets the subscription of this BillingInvoice.


        :return: The subscription of this BillingInvoice.
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this BillingInvoice.


        :param subscription: The subscription of this BillingInvoice.
        :type: str
        """

        self._subscription = subscription

    @property
    def subscription_proration_date(self):
        """
        Gets the subscription_proration_date of this BillingInvoice.


        :return: The subscription_proration_date of this BillingInvoice.
        :rtype: float
        """
        return self._subscription_proration_date

    @subscription_proration_date.setter
    def subscription_proration_date(self, subscription_proration_date):
        """
        Sets the subscription_proration_date of this BillingInvoice.


        :param subscription_proration_date: The subscription_proration_date of this BillingInvoice.
        :type: float
        """

        self._subscription_proration_date = subscription_proration_date

    @property
    def subtotal(self):
        """
        Gets the subtotal of this BillingInvoice.


        :return: The subtotal of this BillingInvoice.
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """
        Sets the subtotal of this BillingInvoice.


        :param subtotal: The subtotal of this BillingInvoice.
        :type: float
        """

        self._subtotal = subtotal

    @property
    def tax(self):
        """
        Gets the tax of this BillingInvoice.


        :return: The tax of this BillingInvoice.
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this BillingInvoice.


        :param tax: The tax of this BillingInvoice.
        :type: float
        """

        self._tax = tax

    @property
    def total(self):
        """
        Gets the total of this BillingInvoice.


        :return: The total of this BillingInvoice.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this BillingInvoice.


        :param total: The total of this BillingInvoice.
        :type: float
        """

        self._total = total

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
