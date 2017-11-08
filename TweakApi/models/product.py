# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.12
    
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


class Product(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description='', thumbnail=None, object=None, idml=None, language=None, created=None, modified=None, id=None, size_id=None, size=None, tags=None):
        """
        Product - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'thumbnail': 'object',
            'object': 'object',
            'idml': 'object',
            'language': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'size_id': 'str',
            'size': 'ProductSize',
            'tags': 'list[Tag]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'thumbnail': 'thumbnail',
            'object': 'object',
            'idml': 'idml',
            'language': 'language',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'size_id': 'sizeId',
            'size': 'size',
            'tags': 'tags'
        }

        self._name = name
        self._description = description
        self._thumbnail = thumbnail
        self._object = object
        self._idml = idml
        self._language = language
        self._created = created
        self._modified = modified
        self._id = id
        self._size_id = size_id
        self._size = size
        self._tags = tags


    @property
    def name(self):
        """
        Gets the name of this Product.


        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Product.


        :param name: The name of this Product.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Product.


        :return: The description of this Product.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Product.


        :param description: The description of this Product.
        :type: str
        """

        self._description = description

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this Product.


        :return: The thumbnail of this Product.
        :rtype: object
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this Product.


        :param thumbnail: The thumbnail of this Product.
        :type: object
        """

        self._thumbnail = thumbnail

    @property
    def object(self):
        """
        Gets the object of this Product.


        :return: The object of this Product.
        :rtype: object
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this Product.


        :param object: The object of this Product.
        :type: object
        """

        self._object = object

    @property
    def idml(self):
        """
        Gets the idml of this Product.


        :return: The idml of this Product.
        :rtype: object
        """
        return self._idml

    @idml.setter
    def idml(self, idml):
        """
        Sets the idml of this Product.


        :param idml: The idml of this Product.
        :type: object
        """

        self._idml = idml

    @property
    def language(self):
        """
        Gets the language of this Product.


        :return: The language of this Product.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Product.


        :param language: The language of this Product.
        :type: str
        """
        allowed_values = ["sq_AL", "sq", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SD", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "ar", "be_BY", "be", "bg_BG", "bg", "ca_ES", "ca", "zh_CN", "zh_HK", "zh_SG", "zh_TW", "zh", "hr_HR", "hr", "cs_CZ", "cs", "da_DK", "da", "nl_BE", "nl_NL", "nl", "en_AU", "en_CA", "en_IN", "en_IE", "en_MT", "en_NZ", "en_PH", "en_SG", "en_ZA", "en_GB", "en_US", "en", "et_EE", "et", "fi_FI", "fi", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_CH", "fr", "de_AT", "de_DE", "de_LU", "de_CH", "de", "el_CY", "el_GR", "el", "iw_IL", "iw", "hi_IN", "hu_HU", "hu", "is_IS", "is", "in_ID", "in", "ga_IE", "ga", "it_IT", "it_CH", "it", "ja_JP", "ja_JP_JP", "ja", "ko_KR", "ko", "lv_LV", "lv", "lt_LT", "lt", "mk_MK", "mk", "ms_MY", "ms", "mt_MT", "mt", "no_NO", "no_NO_NY", "no", "pl_PL", "pl", "pt_BR", "pt_PT", "pt", "ro_RO", "ro", "ru_RU", "ru", "sr_BA", "sr_ME", "sr_CS", "sr_RS", "sr", "sk_SK", "sk", "sl_SI", "sl", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY", "es_PE", "es_PR", "es_ES", "es_US", "es_UY", "es_VE", "es", "sv_SE", "sv", "th_TH", "th_TH_TH", "th", "tr_TR", "tr", "uk_UA", "uk", "vi_VN", "vi"]
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def created(self):
        """
        Gets the created of this Product.


        :return: The created of this Product.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Product.


        :param created: The created of this Product.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Product.


        :return: The modified of this Product.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Product.


        :param modified: The modified of this Product.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Product.


        :return: The id of this Product.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Product.


        :param id: The id of this Product.
        :type: str
        """

        self._id = id

    @property
    def size_id(self):
        """
        Gets the size_id of this Product.


        :return: The size_id of this Product.
        :rtype: str
        """
        return self._size_id

    @size_id.setter
    def size_id(self, size_id):
        """
        Sets the size_id of this Product.


        :param size_id: The size_id of this Product.
        :type: str
        """

        self._size_id = size_id

    @property
    def size(self):
        """
        Gets the size of this Product.


        :return: The size of this Product.
        :rtype: ProductSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Product.


        :param size: The size of this Product.
        :type: ProductSize
        """

        self._size = size

    @property
    def tags(self):
        """
        Gets the tags of this Product.


        :return: The tags of this Product.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Product.


        :param tags: The tags of this Product.
        :type: list[Tag]
        """

        self._tags = tags

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