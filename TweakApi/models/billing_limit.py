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


class BillingLimit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, team_member=None, uploader=None, portal=None, jpeg=None, proof=None, high_res_pdf=None, storage=None, stock_image_library=None, product_db_record=None, account_support=False, support_response=None, bandwidth=None, printer_api=None, id=None):
        """
        BillingLimit - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'team_member': 'BillingLimitCounter',
            'uploader': 'BillingLimitCounter',
            'portal': 'BillingLimitCounter',
            'jpeg': 'BillingLimitCounter',
            'proof': 'BillingLimitCounter',
            'high_res_pdf': 'BillingLimitCounter',
            'storage': 'BillingLimitCounter',
            'stock_image_library': 'BillingLimitCounter',
            'product_db_record': 'BillingLimitCounter',
            'account_support': 'bool',
            'support_response': 'str',
            'bandwidth': 'BillingLimitCounter',
            'printer_api': 'BillingLimitCounter',
            'id': 'str'
        }

        self.attribute_map = {
            'team_member': 'teamMember',
            'uploader': 'uploader',
            'portal': 'portal',
            'jpeg': 'jpeg',
            'proof': 'proof',
            'high_res_pdf': 'highResPdf',
            'storage': 'storage',
            'stock_image_library': 'stockImageLibrary',
            'product_db_record': 'productDbRecord',
            'account_support': 'accountSupport',
            'support_response': 'supportResponse',
            'bandwidth': 'bandwidth',
            'printer_api': 'printerApi',
            'id': 'id'
        }

        self._team_member = team_member
        self._uploader = uploader
        self._portal = portal
        self._jpeg = jpeg
        self._proof = proof
        self._high_res_pdf = high_res_pdf
        self._storage = storage
        self._stock_image_library = stock_image_library
        self._product_db_record = product_db_record
        self._account_support = account_support
        self._support_response = support_response
        self._bandwidth = bandwidth
        self._printer_api = printer_api
        self._id = id


    @property
    def team_member(self):
        """
        Gets the team_member of this BillingLimit.


        :return: The team_member of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._team_member

    @team_member.setter
    def team_member(self, team_member):
        """
        Sets the team_member of this BillingLimit.


        :param team_member: The team_member of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._team_member = team_member

    @property
    def uploader(self):
        """
        Gets the uploader of this BillingLimit.


        :return: The uploader of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._uploader

    @uploader.setter
    def uploader(self, uploader):
        """
        Sets the uploader of this BillingLimit.


        :param uploader: The uploader of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._uploader = uploader

    @property
    def portal(self):
        """
        Gets the portal of this BillingLimit.


        :return: The portal of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this BillingLimit.


        :param portal: The portal of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._portal = portal

    @property
    def jpeg(self):
        """
        Gets the jpeg of this BillingLimit.


        :return: The jpeg of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._jpeg

    @jpeg.setter
    def jpeg(self, jpeg):
        """
        Sets the jpeg of this BillingLimit.


        :param jpeg: The jpeg of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._jpeg = jpeg

    @property
    def proof(self):
        """
        Gets the proof of this BillingLimit.


        :return: The proof of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._proof

    @proof.setter
    def proof(self, proof):
        """
        Sets the proof of this BillingLimit.


        :param proof: The proof of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._proof = proof

    @property
    def high_res_pdf(self):
        """
        Gets the high_res_pdf of this BillingLimit.


        :return: The high_res_pdf of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._high_res_pdf

    @high_res_pdf.setter
    def high_res_pdf(self, high_res_pdf):
        """
        Sets the high_res_pdf of this BillingLimit.


        :param high_res_pdf: The high_res_pdf of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._high_res_pdf = high_res_pdf

    @property
    def storage(self):
        """
        Gets the storage of this BillingLimit.


        :return: The storage of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """
        Sets the storage of this BillingLimit.


        :param storage: The storage of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._storage = storage

    @property
    def stock_image_library(self):
        """
        Gets the stock_image_library of this BillingLimit.


        :return: The stock_image_library of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._stock_image_library

    @stock_image_library.setter
    def stock_image_library(self, stock_image_library):
        """
        Sets the stock_image_library of this BillingLimit.


        :param stock_image_library: The stock_image_library of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._stock_image_library = stock_image_library

    @property
    def product_db_record(self):
        """
        Gets the product_db_record of this BillingLimit.


        :return: The product_db_record of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._product_db_record

    @product_db_record.setter
    def product_db_record(self, product_db_record):
        """
        Sets the product_db_record of this BillingLimit.


        :param product_db_record: The product_db_record of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._product_db_record = product_db_record

    @property
    def account_support(self):
        """
        Gets the account_support of this BillingLimit.


        :return: The account_support of this BillingLimit.
        :rtype: bool
        """
        return self._account_support

    @account_support.setter
    def account_support(self, account_support):
        """
        Sets the account_support of this BillingLimit.


        :param account_support: The account_support of this BillingLimit.
        :type: bool
        """

        self._account_support = account_support

    @property
    def support_response(self):
        """
        Gets the support_response of this BillingLimit.


        :return: The support_response of this BillingLimit.
        :rtype: str
        """
        return self._support_response

    @support_response.setter
    def support_response(self, support_response):
        """
        Sets the support_response of this BillingLimit.


        :param support_response: The support_response of this BillingLimit.
        :type: str
        """

        self._support_response = support_response

    @property
    def bandwidth(self):
        """
        Gets the bandwidth of this BillingLimit.


        :return: The bandwidth of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """
        Sets the bandwidth of this BillingLimit.


        :param bandwidth: The bandwidth of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._bandwidth = bandwidth

    @property
    def printer_api(self):
        """
        Gets the printer_api of this BillingLimit.


        :return: The printer_api of this BillingLimit.
        :rtype: BillingLimitCounter
        """
        return self._printer_api

    @printer_api.setter
    def printer_api(self, printer_api):
        """
        Sets the printer_api of this BillingLimit.


        :param printer_api: The printer_api of this BillingLimit.
        :type: BillingLimitCounter
        """

        self._printer_api = printer_api

    @property
    def id(self):
        """
        Gets the id of this BillingLimit.


        :return: The id of this BillingLimit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingLimit.


        :param id: The id of this BillingLimit.
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
