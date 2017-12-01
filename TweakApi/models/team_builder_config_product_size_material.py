# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.11
    
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


class TeamBuilderConfigProductSizeMaterial(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, binding_type=None, default_bleed=None, print_profile=None, created=None, modified=None, id=None, product_size_material_id=None, pdf_color_profile_id=None, builder_config_id=None, builder_config=None, product_size_material=None, pdf_color_profile=None):
        """
        TeamBuilderConfigProductSizeMaterial - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'binding_type': 'str',
            'default_bleed': 'Bounds',
            'print_profile': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'product_size_material_id': 'str',
            'pdf_color_profile_id': 'str',
            'builder_config_id': 'str',
            'builder_config': 'TeamBuilderConfig',
            'product_size_material': 'ProductSizeMaterial',
            'pdf_color_profile': 'ProductPdfColorProfile'
        }

        self.attribute_map = {
            'binding_type': 'bindingType',
            'default_bleed': 'defaultBleed',
            'print_profile': 'printProfile',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'product_size_material_id': 'productSizeMaterialId',
            'pdf_color_profile_id': 'pdfColorProfileId',
            'builder_config_id': 'builderConfigId',
            'builder_config': 'builderConfig',
            'product_size_material': 'productSizeMaterial',
            'pdf_color_profile': 'pdfColorProfile'
        }

        self._binding_type = binding_type
        self._default_bleed = default_bleed
        self._print_profile = print_profile
        self._created = created
        self._modified = modified
        self._id = id
        self._product_size_material_id = product_size_material_id
        self._pdf_color_profile_id = pdf_color_profile_id
        self._builder_config_id = builder_config_id
        self._builder_config = builder_config
        self._product_size_material = product_size_material
        self._pdf_color_profile = pdf_color_profile


    @property
    def binding_type(self):
        """
        Gets the binding_type of this TeamBuilderConfigProductSizeMaterial.


        :return: The binding_type of this TeamBuilderConfigProductSizeMaterial.
        :rtype: str
        """
        return self._binding_type

    @binding_type.setter
    def binding_type(self, binding_type):
        """
        Sets the binding_type of this TeamBuilderConfigProductSizeMaterial.


        :param binding_type: The binding_type of this TeamBuilderConfigProductSizeMaterial.
        :type: str
        """
        allowed_values = ["none", "saddle-stitched", "perfect", "section-sewn", "wiro", "cased-in-wiro", "pamphlet-stitched", "coptic", "japanese", "screw-post"]
        if binding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `binding_type` ({0}), must be one of {1}"
                .format(binding_type, allowed_values)
            )

        self._binding_type = binding_type

    @property
    def default_bleed(self):
        """
        Gets the default_bleed of this TeamBuilderConfigProductSizeMaterial.


        :return: The default_bleed of this TeamBuilderConfigProductSizeMaterial.
        :rtype: Bounds
        """
        return self._default_bleed

    @default_bleed.setter
    def default_bleed(self, default_bleed):
        """
        Sets the default_bleed of this TeamBuilderConfigProductSizeMaterial.


        :param default_bleed: The default_bleed of this TeamBuilderConfigProductSizeMaterial.
        :type: Bounds
        """

        self._default_bleed = default_bleed

    @property
    def print_profile(self):
        """
        Gets the print_profile of this TeamBuilderConfigProductSizeMaterial.


        :return: The print_profile of this TeamBuilderConfigProductSizeMaterial.
        :rtype: str
        """
        return self._print_profile

    @print_profile.setter
    def print_profile(self, print_profile):
        """
        Sets the print_profile of this TeamBuilderConfigProductSizeMaterial.


        :param print_profile: The print_profile of this TeamBuilderConfigProductSizeMaterial.
        :type: str
        """
        allowed_values = ["PDFX1A", "PDFX3A"]
        if print_profile not in allowed_values:
            raise ValueError(
                "Invalid value for `print_profile` ({0}), must be one of {1}"
                .format(print_profile, allowed_values)
            )

        self._print_profile = print_profile

    @property
    def created(self):
        """
        Gets the created of this TeamBuilderConfigProductSizeMaterial.


        :return: The created of this TeamBuilderConfigProductSizeMaterial.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TeamBuilderConfigProductSizeMaterial.


        :param created: The created of this TeamBuilderConfigProductSizeMaterial.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this TeamBuilderConfigProductSizeMaterial.


        :return: The modified of this TeamBuilderConfigProductSizeMaterial.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this TeamBuilderConfigProductSizeMaterial.


        :param modified: The modified of this TeamBuilderConfigProductSizeMaterial.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this TeamBuilderConfigProductSizeMaterial.


        :return: The id of this TeamBuilderConfigProductSizeMaterial.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamBuilderConfigProductSizeMaterial.


        :param id: The id of this TeamBuilderConfigProductSizeMaterial.
        :type: str
        """

        self._id = id

    @property
    def product_size_material_id(self):
        """
        Gets the product_size_material_id of this TeamBuilderConfigProductSizeMaterial.


        :return: The product_size_material_id of this TeamBuilderConfigProductSizeMaterial.
        :rtype: str
        """
        return self._product_size_material_id

    @product_size_material_id.setter
    def product_size_material_id(self, product_size_material_id):
        """
        Sets the product_size_material_id of this TeamBuilderConfigProductSizeMaterial.


        :param product_size_material_id: The product_size_material_id of this TeamBuilderConfigProductSizeMaterial.
        :type: str
        """

        self._product_size_material_id = product_size_material_id

    @property
    def pdf_color_profile_id(self):
        """
        Gets the pdf_color_profile_id of this TeamBuilderConfigProductSizeMaterial.


        :return: The pdf_color_profile_id of this TeamBuilderConfigProductSizeMaterial.
        :rtype: str
        """
        return self._pdf_color_profile_id

    @pdf_color_profile_id.setter
    def pdf_color_profile_id(self, pdf_color_profile_id):
        """
        Sets the pdf_color_profile_id of this TeamBuilderConfigProductSizeMaterial.


        :param pdf_color_profile_id: The pdf_color_profile_id of this TeamBuilderConfigProductSizeMaterial.
        :type: str
        """

        self._pdf_color_profile_id = pdf_color_profile_id

    @property
    def builder_config_id(self):
        """
        Gets the builder_config_id of this TeamBuilderConfigProductSizeMaterial.


        :return: The builder_config_id of this TeamBuilderConfigProductSizeMaterial.
        :rtype: str
        """
        return self._builder_config_id

    @builder_config_id.setter
    def builder_config_id(self, builder_config_id):
        """
        Sets the builder_config_id of this TeamBuilderConfigProductSizeMaterial.


        :param builder_config_id: The builder_config_id of this TeamBuilderConfigProductSizeMaterial.
        :type: str
        """

        self._builder_config_id = builder_config_id

    @property
    def builder_config(self):
        """
        Gets the builder_config of this TeamBuilderConfigProductSizeMaterial.


        :return: The builder_config of this TeamBuilderConfigProductSizeMaterial.
        :rtype: TeamBuilderConfig
        """
        return self._builder_config

    @builder_config.setter
    def builder_config(self, builder_config):
        """
        Sets the builder_config of this TeamBuilderConfigProductSizeMaterial.


        :param builder_config: The builder_config of this TeamBuilderConfigProductSizeMaterial.
        :type: TeamBuilderConfig
        """

        self._builder_config = builder_config

    @property
    def product_size_material(self):
        """
        Gets the product_size_material of this TeamBuilderConfigProductSizeMaterial.


        :return: The product_size_material of this TeamBuilderConfigProductSizeMaterial.
        :rtype: ProductSizeMaterial
        """
        return self._product_size_material

    @product_size_material.setter
    def product_size_material(self, product_size_material):
        """
        Sets the product_size_material of this TeamBuilderConfigProductSizeMaterial.


        :param product_size_material: The product_size_material of this TeamBuilderConfigProductSizeMaterial.
        :type: ProductSizeMaterial
        """

        self._product_size_material = product_size_material

    @property
    def pdf_color_profile(self):
        """
        Gets the pdf_color_profile of this TeamBuilderConfigProductSizeMaterial.


        :return: The pdf_color_profile of this TeamBuilderConfigProductSizeMaterial.
        :rtype: ProductPdfColorProfile
        """
        return self._pdf_color_profile

    @pdf_color_profile.setter
    def pdf_color_profile(self, pdf_color_profile):
        """
        Sets the pdf_color_profile of this TeamBuilderConfigProductSizeMaterial.


        :param pdf_color_profile: The pdf_color_profile of this TeamBuilderConfigProductSizeMaterial.
        :type: ProductPdfColorProfile
        """

        self._pdf_color_profile = pdf_color_profile

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
