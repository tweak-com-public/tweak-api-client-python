# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.6
    
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


class Billing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, company_name=None, company_email=None, company_vat=None, company_card=None, subscription=None, limit=None, tax_percent=0.0, stripe_customer_id=None, stripe_card_id=None, stripe_subscription_id=None, id=None, team_id=None, team=None):
        """
        Billing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'company_name': 'str',
            'company_email': 'str',
            'company_vat': 'str',
            'company_card': 'BillingCard',
            'subscription': 'BillingSubscription',
            'limit': 'BillingLimit',
            'tax_percent': 'float',
            'stripe_customer_id': 'str',
            'stripe_card_id': 'str',
            'stripe_subscription_id': 'str',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team'
        }

        self.attribute_map = {
            'company_name': 'companyName',
            'company_email': 'companyEmail',
            'company_vat': 'companyVat',
            'company_card': 'companyCard',
            'subscription': 'subscription',
            'limit': 'limit',
            'tax_percent': 'taxPercent',
            'stripe_customer_id': 'stripeCustomerId',
            'stripe_card_id': 'stripeCardId',
            'stripe_subscription_id': 'stripeSubscriptionId',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team'
        }

        self._company_name = company_name
        self._company_email = company_email
        self._company_vat = company_vat
        self._company_card = company_card
        self._subscription = subscription
        self._limit = limit
        self._tax_percent = tax_percent
        self._stripe_customer_id = stripe_customer_id
        self._stripe_card_id = stripe_card_id
        self._stripe_subscription_id = stripe_subscription_id
        self._id = id
        self._team_id = team_id
        self._team = team


    @property
    def company_name(self):
        """
        Gets the company_name of this Billing.


        :return: The company_name of this Billing.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this Billing.


        :param company_name: The company_name of this Billing.
        :type: str
        """

        self._company_name = company_name

    @property
    def company_email(self):
        """
        Gets the company_email of this Billing.


        :return: The company_email of this Billing.
        :rtype: str
        """
        return self._company_email

    @company_email.setter
    def company_email(self, company_email):
        """
        Sets the company_email of this Billing.


        :param company_email: The company_email of this Billing.
        :type: str
        """

        self._company_email = company_email

    @property
    def company_vat(self):
        """
        Gets the company_vat of this Billing.


        :return: The company_vat of this Billing.
        :rtype: str
        """
        return self._company_vat

    @company_vat.setter
    def company_vat(self, company_vat):
        """
        Sets the company_vat of this Billing.


        :param company_vat: The company_vat of this Billing.
        :type: str
        """

        self._company_vat = company_vat

    @property
    def company_card(self):
        """
        Gets the company_card of this Billing.


        :return: The company_card of this Billing.
        :rtype: BillingCard
        """
        return self._company_card

    @company_card.setter
    def company_card(self, company_card):
        """
        Sets the company_card of this Billing.


        :param company_card: The company_card of this Billing.
        :type: BillingCard
        """

        self._company_card = company_card

    @property
    def subscription(self):
        """
        Gets the subscription of this Billing.


        :return: The subscription of this Billing.
        :rtype: BillingSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this Billing.


        :param subscription: The subscription of this Billing.
        :type: BillingSubscription
        """

        self._subscription = subscription

    @property
    def limit(self):
        """
        Gets the limit of this Billing.


        :return: The limit of this Billing.
        :rtype: BillingLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this Billing.


        :param limit: The limit of this Billing.
        :type: BillingLimit
        """

        self._limit = limit

    @property
    def tax_percent(self):
        """
        Gets the tax_percent of this Billing.


        :return: The tax_percent of this Billing.
        :rtype: float
        """
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, tax_percent):
        """
        Sets the tax_percent of this Billing.


        :param tax_percent: The tax_percent of this Billing.
        :type: float
        """

        self._tax_percent = tax_percent

    @property
    def stripe_customer_id(self):
        """
        Gets the stripe_customer_id of this Billing.


        :return: The stripe_customer_id of this Billing.
        :rtype: str
        """
        return self._stripe_customer_id

    @stripe_customer_id.setter
    def stripe_customer_id(self, stripe_customer_id):
        """
        Sets the stripe_customer_id of this Billing.


        :param stripe_customer_id: The stripe_customer_id of this Billing.
        :type: str
        """

        self._stripe_customer_id = stripe_customer_id

    @property
    def stripe_card_id(self):
        """
        Gets the stripe_card_id of this Billing.


        :return: The stripe_card_id of this Billing.
        :rtype: str
        """
        return self._stripe_card_id

    @stripe_card_id.setter
    def stripe_card_id(self, stripe_card_id):
        """
        Sets the stripe_card_id of this Billing.


        :param stripe_card_id: The stripe_card_id of this Billing.
        :type: str
        """

        self._stripe_card_id = stripe_card_id

    @property
    def stripe_subscription_id(self):
        """
        Gets the stripe_subscription_id of this Billing.


        :return: The stripe_subscription_id of this Billing.
        :rtype: str
        """
        return self._stripe_subscription_id

    @stripe_subscription_id.setter
    def stripe_subscription_id(self, stripe_subscription_id):
        """
        Sets the stripe_subscription_id of this Billing.


        :param stripe_subscription_id: The stripe_subscription_id of this Billing.
        :type: str
        """

        self._stripe_subscription_id = stripe_subscription_id

    @property
    def id(self):
        """
        Gets the id of this Billing.


        :return: The id of this Billing.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Billing.


        :param id: The id of this Billing.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this Billing.


        :return: The team_id of this Billing.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Billing.


        :param team_id: The team_id of this Billing.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this Billing.


        :return: The team of this Billing.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Billing.


        :param team: The team of this Billing.
        :type: Team
        """

        self._team = team

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
