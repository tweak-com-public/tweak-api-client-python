# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.1
    
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


class ProductSize(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, code=None, thumbnail=None, folding_type=None, folding_method=None, binding_type=None, double_sided=False, die_cut=False, unfolded_size=None, folded_size=None, pdf_size=None, pdf_page_count=1.0, pdf_dpi=300.0, print_profile=None, customer_size=None, customer_page_count=1.0, max_bleed=None, default_bleed=None, safe_area=None, unit=None, frame=0.0, shape=None, orientation=None, format=None, envelope_window=None, canvas_image_count=0.0, created=None, modified=None, id=None, pdf_color_profile_id=None, type_id=None, type=None, materials=None, size_materials=None, products=None, pdf_color_profile=None):
        """
        ProductSize - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'code': 'str',
            'thumbnail': 'CloudinaryImage',
            'folding_type': 'str',
            'folding_method': 'str',
            'binding_type': 'str',
            'double_sided': 'bool',
            'die_cut': 'bool',
            'unfolded_size': 'Dimensions',
            'folded_size': 'Dimensions',
            'pdf_size': 'Dimensions',
            'pdf_page_count': 'float',
            'pdf_dpi': 'float',
            'print_profile': 'str',
            'customer_size': 'Dimensions',
            'customer_page_count': 'float',
            'max_bleed': 'Bounds',
            'default_bleed': 'Bounds',
            'safe_area': 'Bounds',
            'unit': 'str',
            'frame': 'float',
            'shape': 'str',
            'orientation': 'str',
            'format': 'str',
            'envelope_window': 'str',
            'canvas_image_count': 'float',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'pdf_color_profile_id': 'str',
            'type_id': 'str',
            'type': 'ProductType',
            'materials': 'list[ProductMaterial]',
            'size_materials': 'list[ProductSizeMaterial]',
            'products': 'list[Product]',
            'pdf_color_profile': 'ProductPdfColorProfile'
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'thumbnail': 'thumbnail',
            'folding_type': 'foldingType',
            'folding_method': 'foldingMethod',
            'binding_type': 'bindingType',
            'double_sided': 'doubleSided',
            'die_cut': 'dieCut',
            'unfolded_size': 'unfoldedSize',
            'folded_size': 'foldedSize',
            'pdf_size': 'pdfSize',
            'pdf_page_count': 'pdfPageCount',
            'pdf_dpi': 'pdfDpi',
            'print_profile': 'printProfile',
            'customer_size': 'customerSize',
            'customer_page_count': 'customerPageCount',
            'max_bleed': 'maxBleed',
            'default_bleed': 'defaultBleed',
            'safe_area': 'safeArea',
            'unit': 'unit',
            'frame': 'frame',
            'shape': 'shape',
            'orientation': 'orientation',
            'format': 'format',
            'envelope_window': 'envelopeWindow',
            'canvas_image_count': 'canvasImageCount',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'pdf_color_profile_id': 'pdfColorProfileId',
            'type_id': 'typeId',
            'type': 'type',
            'materials': 'materials',
            'size_materials': 'sizeMaterials',
            'products': 'products',
            'pdf_color_profile': 'pdfColorProfile'
        }

        self._name = name
        self._code = code
        self._thumbnail = thumbnail
        self._folding_type = folding_type
        self._folding_method = folding_method
        self._binding_type = binding_type
        self._double_sided = double_sided
        self._die_cut = die_cut
        self._unfolded_size = unfolded_size
        self._folded_size = folded_size
        self._pdf_size = pdf_size
        self._pdf_page_count = pdf_page_count
        self._pdf_dpi = pdf_dpi
        self._print_profile = print_profile
        self._customer_size = customer_size
        self._customer_page_count = customer_page_count
        self._max_bleed = max_bleed
        self._default_bleed = default_bleed
        self._safe_area = safe_area
        self._unit = unit
        self._frame = frame
        self._shape = shape
        self._orientation = orientation
        self._format = format
        self._envelope_window = envelope_window
        self._canvas_image_count = canvas_image_count
        self._created = created
        self._modified = modified
        self._id = id
        self._pdf_color_profile_id = pdf_color_profile_id
        self._type_id = type_id
        self._type = type
        self._materials = materials
        self._size_materials = size_materials
        self._products = products
        self._pdf_color_profile = pdf_color_profile


    @property
    def name(self):
        """
        Gets the name of this ProductSize.


        :return: The name of this ProductSize.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductSize.


        :param name: The name of this ProductSize.
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """
        Gets the code of this ProductSize.


        :return: The code of this ProductSize.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ProductSize.


        :param code: The code of this ProductSize.
        :type: str
        """

        self._code = code

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this ProductSize.


        :return: The thumbnail of this ProductSize.
        :rtype: CloudinaryImage
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this ProductSize.


        :param thumbnail: The thumbnail of this ProductSize.
        :type: CloudinaryImage
        """

        self._thumbnail = thumbnail

    @property
    def folding_type(self):
        """
        Gets the folding_type of this ProductSize.


        :return: The folding_type of this ProductSize.
        :rtype: str
        """
        return self._folding_type

    @folding_type.setter
    def folding_type(self, folding_type):
        """
        Sets the folding_type of this ProductSize.


        :param folding_type: The folding_type of this ProductSize.
        :type: str
        """
        allowed_values = ["none", "accordian-left", "accordian-right", "accordion", "letter-left", "letter-right", "rollover"]
        if folding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `folding_type` ({0}), must be one of {1}"
                .format(folding_type, allowed_values)
            )

        self._folding_type = folding_type

    @property
    def folding_method(self):
        """
        Gets the folding_method of this ProductSize.


        :return: The folding_method of this ProductSize.
        :rtype: str
        """
        return self._folding_method

    @folding_method.setter
    def folding_method(self, folding_method):
        """
        Sets the folding_method of this ProductSize.


        :param folding_method: The folding_method of this ProductSize.
        :type: str
        """
        allowed_values = ["none", "fold", "crease", "prefolded"]
        if folding_method not in allowed_values:
            raise ValueError(
                "Invalid value for `folding_method` ({0}), must be one of {1}"
                .format(folding_method, allowed_values)
            )

        self._folding_method = folding_method

    @property
    def binding_type(self):
        """
        Gets the binding_type of this ProductSize.


        :return: The binding_type of this ProductSize.
        :rtype: str
        """
        return self._binding_type

    @binding_type.setter
    def binding_type(self, binding_type):
        """
        Sets the binding_type of this ProductSize.


        :param binding_type: The binding_type of this ProductSize.
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
    def double_sided(self):
        """
        Gets the double_sided of this ProductSize.


        :return: The double_sided of this ProductSize.
        :rtype: bool
        """
        return self._double_sided

    @double_sided.setter
    def double_sided(self, double_sided):
        """
        Sets the double_sided of this ProductSize.


        :param double_sided: The double_sided of this ProductSize.
        :type: bool
        """

        self._double_sided = double_sided

    @property
    def die_cut(self):
        """
        Gets the die_cut of this ProductSize.


        :return: The die_cut of this ProductSize.
        :rtype: bool
        """
        return self._die_cut

    @die_cut.setter
    def die_cut(self, die_cut):
        """
        Sets the die_cut of this ProductSize.


        :param die_cut: The die_cut of this ProductSize.
        :type: bool
        """

        self._die_cut = die_cut

    @property
    def unfolded_size(self):
        """
        Gets the unfolded_size of this ProductSize.


        :return: The unfolded_size of this ProductSize.
        :rtype: Dimensions
        """
        return self._unfolded_size

    @unfolded_size.setter
    def unfolded_size(self, unfolded_size):
        """
        Sets the unfolded_size of this ProductSize.


        :param unfolded_size: The unfolded_size of this ProductSize.
        :type: Dimensions
        """

        self._unfolded_size = unfolded_size

    @property
    def folded_size(self):
        """
        Gets the folded_size of this ProductSize.


        :return: The folded_size of this ProductSize.
        :rtype: Dimensions
        """
        return self._folded_size

    @folded_size.setter
    def folded_size(self, folded_size):
        """
        Sets the folded_size of this ProductSize.


        :param folded_size: The folded_size of this ProductSize.
        :type: Dimensions
        """

        self._folded_size = folded_size

    @property
    def pdf_size(self):
        """
        Gets the pdf_size of this ProductSize.


        :return: The pdf_size of this ProductSize.
        :rtype: Dimensions
        """
        return self._pdf_size

    @pdf_size.setter
    def pdf_size(self, pdf_size):
        """
        Sets the pdf_size of this ProductSize.


        :param pdf_size: The pdf_size of this ProductSize.
        :type: Dimensions
        """

        self._pdf_size = pdf_size

    @property
    def pdf_page_count(self):
        """
        Gets the pdf_page_count of this ProductSize.


        :return: The pdf_page_count of this ProductSize.
        :rtype: float
        """
        return self._pdf_page_count

    @pdf_page_count.setter
    def pdf_page_count(self, pdf_page_count):
        """
        Sets the pdf_page_count of this ProductSize.


        :param pdf_page_count: The pdf_page_count of this ProductSize.
        :type: float
        """

        self._pdf_page_count = pdf_page_count

    @property
    def pdf_dpi(self):
        """
        Gets the pdf_dpi of this ProductSize.


        :return: The pdf_dpi of this ProductSize.
        :rtype: float
        """
        return self._pdf_dpi

    @pdf_dpi.setter
    def pdf_dpi(self, pdf_dpi):
        """
        Sets the pdf_dpi of this ProductSize.


        :param pdf_dpi: The pdf_dpi of this ProductSize.
        :type: float
        """

        if not pdf_dpi:
            raise ValueError("Invalid value for `pdf_dpi`, must not be `None`")
        if pdf_dpi > 4800.0:
            raise ValueError("Invalid value for `pdf_dpi`, must be a value less than or equal to `4800.0`")
        if pdf_dpi < 10.0:
            raise ValueError("Invalid value for `pdf_dpi`, must be a value greater than or equal to `10.0`")

        self._pdf_dpi = pdf_dpi

    @property
    def print_profile(self):
        """
        Gets the print_profile of this ProductSize.


        :return: The print_profile of this ProductSize.
        :rtype: str
        """
        return self._print_profile

    @print_profile.setter
    def print_profile(self, print_profile):
        """
        Sets the print_profile of this ProductSize.


        :param print_profile: The print_profile of this ProductSize.
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
    def customer_size(self):
        """
        Gets the customer_size of this ProductSize.


        :return: The customer_size of this ProductSize.
        :rtype: Dimensions
        """
        return self._customer_size

    @customer_size.setter
    def customer_size(self, customer_size):
        """
        Sets the customer_size of this ProductSize.


        :param customer_size: The customer_size of this ProductSize.
        :type: Dimensions
        """

        self._customer_size = customer_size

    @property
    def customer_page_count(self):
        """
        Gets the customer_page_count of this ProductSize.


        :return: The customer_page_count of this ProductSize.
        :rtype: float
        """
        return self._customer_page_count

    @customer_page_count.setter
    def customer_page_count(self, customer_page_count):
        """
        Sets the customer_page_count of this ProductSize.


        :param customer_page_count: The customer_page_count of this ProductSize.
        :type: float
        """

        self._customer_page_count = customer_page_count

    @property
    def max_bleed(self):
        """
        Gets the max_bleed of this ProductSize.


        :return: The max_bleed of this ProductSize.
        :rtype: Bounds
        """
        return self._max_bleed

    @max_bleed.setter
    def max_bleed(self, max_bleed):
        """
        Sets the max_bleed of this ProductSize.


        :param max_bleed: The max_bleed of this ProductSize.
        :type: Bounds
        """

        self._max_bleed = max_bleed

    @property
    def default_bleed(self):
        """
        Gets the default_bleed of this ProductSize.


        :return: The default_bleed of this ProductSize.
        :rtype: Bounds
        """
        return self._default_bleed

    @default_bleed.setter
    def default_bleed(self, default_bleed):
        """
        Sets the default_bleed of this ProductSize.


        :param default_bleed: The default_bleed of this ProductSize.
        :type: Bounds
        """

        self._default_bleed = default_bleed

    @property
    def safe_area(self):
        """
        Gets the safe_area of this ProductSize.


        :return: The safe_area of this ProductSize.
        :rtype: Bounds
        """
        return self._safe_area

    @safe_area.setter
    def safe_area(self, safe_area):
        """
        Sets the safe_area of this ProductSize.


        :param safe_area: The safe_area of this ProductSize.
        :type: Bounds
        """

        self._safe_area = safe_area

    @property
    def unit(self):
        """
        Gets the unit of this ProductSize.


        :return: The unit of this ProductSize.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this ProductSize.


        :param unit: The unit of this ProductSize.
        :type: str
        """
        allowed_values = ["mm", "inch"]
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def frame(self):
        """
        Gets the frame of this ProductSize.


        :return: The frame of this ProductSize.
        :rtype: float
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """
        Sets the frame of this ProductSize.


        :param frame: The frame of this ProductSize.
        :type: float
        """

        self._frame = frame

    @property
    def shape(self):
        """
        Gets the shape of this ProductSize.


        :return: The shape of this ProductSize.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ProductSize.


        :param shape: The shape of this ProductSize.
        :type: str
        """
        allowed_values = ["rect", "square", "rect-rouded-corners", "square-rouded-corners", "oval", "circle"]
        if shape not in allowed_values:
            raise ValueError(
                "Invalid value for `shape` ({0}), must be one of {1}"
                .format(shape, allowed_values)
            )

        self._shape = shape

    @property
    def orientation(self):
        """
        Gets the orientation of this ProductSize.


        :return: The orientation of this ProductSize.
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """
        Sets the orientation of this ProductSize.


        :param orientation: The orientation of this ProductSize.
        :type: str
        """
        allowed_values = ["none", "landscape", "portrait"]
        if orientation not in allowed_values:
            raise ValueError(
                "Invalid value for `orientation` ({0}), must be one of {1}"
                .format(orientation, allowed_values)
            )

        self._orientation = orientation

    @property
    def format(self):
        """
        Gets the format of this ProductSize.


        :return: The format of this ProductSize.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this ProductSize.


        :param format: The format of this ProductSize.
        :type: str
        """
        allowed_values = ["eu", "us"]
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def envelope_window(self):
        """
        Gets the envelope_window of this ProductSize.


        :return: The envelope_window of this ProductSize.
        :rtype: str
        """
        return self._envelope_window

    @envelope_window.setter
    def envelope_window(self, envelope_window):
        """
        Sets the envelope_window of this ProductSize.


        :param envelope_window: The envelope_window of this ProductSize.
        :type: str
        """
        allowed_values = ["none", "left", "right"]
        if envelope_window not in allowed_values:
            raise ValueError(
                "Invalid value for `envelope_window` ({0}), must be one of {1}"
                .format(envelope_window, allowed_values)
            )

        self._envelope_window = envelope_window

    @property
    def canvas_image_count(self):
        """
        Gets the canvas_image_count of this ProductSize.


        :return: The canvas_image_count of this ProductSize.
        :rtype: float
        """
        return self._canvas_image_count

    @canvas_image_count.setter
    def canvas_image_count(self, canvas_image_count):
        """
        Sets the canvas_image_count of this ProductSize.


        :param canvas_image_count: The canvas_image_count of this ProductSize.
        :type: float
        """

        self._canvas_image_count = canvas_image_count

    @property
    def created(self):
        """
        Gets the created of this ProductSize.


        :return: The created of this ProductSize.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ProductSize.


        :param created: The created of this ProductSize.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this ProductSize.


        :return: The modified of this ProductSize.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this ProductSize.


        :param modified: The modified of this ProductSize.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this ProductSize.


        :return: The id of this ProductSize.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductSize.


        :param id: The id of this ProductSize.
        :type: str
        """

        self._id = id

    @property
    def pdf_color_profile_id(self):
        """
        Gets the pdf_color_profile_id of this ProductSize.


        :return: The pdf_color_profile_id of this ProductSize.
        :rtype: str
        """
        return self._pdf_color_profile_id

    @pdf_color_profile_id.setter
    def pdf_color_profile_id(self, pdf_color_profile_id):
        """
        Sets the pdf_color_profile_id of this ProductSize.


        :param pdf_color_profile_id: The pdf_color_profile_id of this ProductSize.
        :type: str
        """

        self._pdf_color_profile_id = pdf_color_profile_id

    @property
    def type_id(self):
        """
        Gets the type_id of this ProductSize.


        :return: The type_id of this ProductSize.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this ProductSize.


        :param type_id: The type_id of this ProductSize.
        :type: str
        """

        self._type_id = type_id

    @property
    def type(self):
        """
        Gets the type of this ProductSize.


        :return: The type of this ProductSize.
        :rtype: ProductType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductSize.


        :param type: The type of this ProductSize.
        :type: ProductType
        """

        self._type = type

    @property
    def materials(self):
        """
        Gets the materials of this ProductSize.


        :return: The materials of this ProductSize.
        :rtype: list[ProductMaterial]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """
        Sets the materials of this ProductSize.


        :param materials: The materials of this ProductSize.
        :type: list[ProductMaterial]
        """

        self._materials = materials

    @property
    def size_materials(self):
        """
        Gets the size_materials of this ProductSize.


        :return: The size_materials of this ProductSize.
        :rtype: list[ProductSizeMaterial]
        """
        return self._size_materials

    @size_materials.setter
    def size_materials(self, size_materials):
        """
        Sets the size_materials of this ProductSize.


        :param size_materials: The size_materials of this ProductSize.
        :type: list[ProductSizeMaterial]
        """

        self._size_materials = size_materials

    @property
    def products(self):
        """
        Gets the products of this ProductSize.


        :return: The products of this ProductSize.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this ProductSize.


        :param products: The products of this ProductSize.
        :type: list[Product]
        """

        self._products = products

    @property
    def pdf_color_profile(self):
        """
        Gets the pdf_color_profile of this ProductSize.


        :return: The pdf_color_profile of this ProductSize.
        :rtype: ProductPdfColorProfile
        """
        return self._pdf_color_profile

    @pdf_color_profile.setter
    def pdf_color_profile(self, pdf_color_profile):
        """
        Sets the pdf_color_profile of this ProductSize.


        :param pdf_color_profile: The pdf_color_profile of this ProductSize.
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
