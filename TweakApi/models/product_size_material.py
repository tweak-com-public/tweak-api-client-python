# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-beta.0
    
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


class ProductSizeMaterial(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, legacy_code=None, description=None, thumbnail=None, status=None, binding_type=None, default_bleed=None, print_profile=None, created=None, modified=None, id=None, material_id=None, team_id=None, pdf_color_profile_id=None, size_id=None, size=None, material=None, team=None, pdf_color_profile=None):
        """
        ProductSizeMaterial - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'legacy_code': 'str',
            'description': 'str',
            'thumbnail': 'CloudinaryImage',
            'status': 'str',
            'binding_type': 'str',
            'default_bleed': 'Bounds',
            'print_profile': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'material_id': 'str',
            'team_id': 'str',
            'pdf_color_profile_id': 'str',
            'size_id': 'str',
            'size': 'ProductSize',
            'material': 'ProductMaterial',
            'team': 'Team',
            'pdf_color_profile': 'ProductPdfColorProfile'
        }

        self.attribute_map = {
            'code': 'code',
            'legacy_code': 'legacyCode',
            'description': 'description',
            'thumbnail': 'thumbnail',
            'status': 'status',
            'binding_type': 'bindingType',
            'default_bleed': 'defaultBleed',
            'print_profile': 'printProfile',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'material_id': 'materialId',
            'team_id': 'teamId',
            'pdf_color_profile_id': 'pdfColorProfileId',
            'size_id': 'sizeId',
            'size': 'size',
            'material': 'material',
            'team': 'team',
            'pdf_color_profile': 'pdfColorProfile'
        }

        self._code = code
        self._legacy_code = legacy_code
        self._description = description
        self._thumbnail = thumbnail
        self._status = status
        self._binding_type = binding_type
        self._default_bleed = default_bleed
        self._print_profile = print_profile
        self._created = created
        self._modified = modified
        self._id = id
        self._material_id = material_id
        self._team_id = team_id
        self._pdf_color_profile_id = pdf_color_profile_id
        self._size_id = size_id
        self._size = size
        self._material = material
        self._team = team
        self._pdf_color_profile = pdf_color_profile


    @property
    def code(self):
        """
        Gets the code of this ProductSizeMaterial.


        :return: The code of this ProductSizeMaterial.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ProductSizeMaterial.


        :param code: The code of this ProductSizeMaterial.
        :type: str
        """

        self._code = code

    @property
    def legacy_code(self):
        """
        Gets the legacy_code of this ProductSizeMaterial.


        :return: The legacy_code of this ProductSizeMaterial.
        :rtype: str
        """
        return self._legacy_code

    @legacy_code.setter
    def legacy_code(self, legacy_code):
        """
        Sets the legacy_code of this ProductSizeMaterial.


        :param legacy_code: The legacy_code of this ProductSizeMaterial.
        :type: str
        """

        self._legacy_code = legacy_code

    @property
    def description(self):
        """
        Gets the description of this ProductSizeMaterial.


        :return: The description of this ProductSizeMaterial.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProductSizeMaterial.


        :param description: The description of this ProductSizeMaterial.
        :type: str
        """

        self._description = description

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this ProductSizeMaterial.


        :return: The thumbnail of this ProductSizeMaterial.
        :rtype: CloudinaryImage
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this ProductSizeMaterial.


        :param thumbnail: The thumbnail of this ProductSizeMaterial.
        :type: CloudinaryImage
        """

        self._thumbnail = thumbnail

    @property
    def status(self):
        """
        Gets the status of this ProductSizeMaterial.


        :return: The status of this ProductSizeMaterial.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProductSizeMaterial.


        :param status: The status of this ProductSizeMaterial.
        :type: str
        """
        allowed_values = ["public", "private"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def binding_type(self):
        """
        Gets the binding_type of this ProductSizeMaterial.


        :return: The binding_type of this ProductSizeMaterial.
        :rtype: str
        """
        return self._binding_type

    @binding_type.setter
    def binding_type(self, binding_type):
        """
        Sets the binding_type of this ProductSizeMaterial.


        :param binding_type: The binding_type of this ProductSizeMaterial.
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
        Gets the default_bleed of this ProductSizeMaterial.


        :return: The default_bleed of this ProductSizeMaterial.
        :rtype: Bounds
        """
        return self._default_bleed

    @default_bleed.setter
    def default_bleed(self, default_bleed):
        """
        Sets the default_bleed of this ProductSizeMaterial.


        :param default_bleed: The default_bleed of this ProductSizeMaterial.
        :type: Bounds
        """

        self._default_bleed = default_bleed

    @property
    def print_profile(self):
        """
        Gets the print_profile of this ProductSizeMaterial.


        :return: The print_profile of this ProductSizeMaterial.
        :rtype: str
        """
        return self._print_profile

    @print_profile.setter
    def print_profile(self, print_profile):
        """
        Sets the print_profile of this ProductSizeMaterial.


        :param print_profile: The print_profile of this ProductSizeMaterial.
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
        Gets the created of this ProductSizeMaterial.


        :return: The created of this ProductSizeMaterial.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ProductSizeMaterial.


        :param created: The created of this ProductSizeMaterial.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this ProductSizeMaterial.


        :return: The modified of this ProductSizeMaterial.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this ProductSizeMaterial.


        :param modified: The modified of this ProductSizeMaterial.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this ProductSizeMaterial.


        :return: The id of this ProductSizeMaterial.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductSizeMaterial.


        :param id: The id of this ProductSizeMaterial.
        :type: str
        """

        self._id = id

    @property
    def material_id(self):
        """
        Gets the material_id of this ProductSizeMaterial.


        :return: The material_id of this ProductSizeMaterial.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        """
        Sets the material_id of this ProductSizeMaterial.


        :param material_id: The material_id of this ProductSizeMaterial.
        :type: str
        """

        self._material_id = material_id

    @property
    def team_id(self):
        """
        Gets the team_id of this ProductSizeMaterial.


        :return: The team_id of this ProductSizeMaterial.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this ProductSizeMaterial.


        :param team_id: The team_id of this ProductSizeMaterial.
        :type: str
        """

        self._team_id = team_id

    @property
    def pdf_color_profile_id(self):
        """
        Gets the pdf_color_profile_id of this ProductSizeMaterial.


        :return: The pdf_color_profile_id of this ProductSizeMaterial.
        :rtype: str
        """
        return self._pdf_color_profile_id

    @pdf_color_profile_id.setter
    def pdf_color_profile_id(self, pdf_color_profile_id):
        """
        Sets the pdf_color_profile_id of this ProductSizeMaterial.


        :param pdf_color_profile_id: The pdf_color_profile_id of this ProductSizeMaterial.
        :type: str
        """

        self._pdf_color_profile_id = pdf_color_profile_id

    @property
    def size_id(self):
        """
        Gets the size_id of this ProductSizeMaterial.


        :return: The size_id of this ProductSizeMaterial.
        :rtype: str
        """
        return self._size_id

    @size_id.setter
    def size_id(self, size_id):
        """
        Sets the size_id of this ProductSizeMaterial.


        :param size_id: The size_id of this ProductSizeMaterial.
        :type: str
        """

        self._size_id = size_id

    @property
    def size(self):
        """
        Gets the size of this ProductSizeMaterial.


        :return: The size of this ProductSizeMaterial.
        :rtype: ProductSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ProductSizeMaterial.


        :param size: The size of this ProductSizeMaterial.
        :type: ProductSize
        """

        self._size = size

    @property
    def material(self):
        """
        Gets the material of this ProductSizeMaterial.


        :return: The material of this ProductSizeMaterial.
        :rtype: ProductMaterial
        """
        return self._material

    @material.setter
    def material(self, material):
        """
        Sets the material of this ProductSizeMaterial.


        :param material: The material of this ProductSizeMaterial.
        :type: ProductMaterial
        """

        self._material = material

    @property
    def team(self):
        """
        Gets the team of this ProductSizeMaterial.


        :return: The team of this ProductSizeMaterial.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this ProductSizeMaterial.


        :param team: The team of this ProductSizeMaterial.
        :type: Team
        """

        self._team = team

    @property
    def pdf_color_profile(self):
        """
        Gets the pdf_color_profile of this ProductSizeMaterial.


        :return: The pdf_color_profile of this ProductSizeMaterial.
        :rtype: ProductPdfColorProfile
        """
        return self._pdf_color_profile

    @pdf_color_profile.setter
    def pdf_color_profile(self, pdf_color_profile):
        """
        Sets the pdf_color_profile of this ProductSizeMaterial.


        :param pdf_color_profile: The pdf_color_profile of this ProductSizeMaterial.
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
