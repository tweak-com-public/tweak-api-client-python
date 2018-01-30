# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-beta.1
    
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


class TemplatePermissionSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, high_res_pdf=False, proof_pdf=False, jpegs=False, social_sharing=False, can_edit=False, need_admin_approval=False, id=None, template_id=None, template=None):
        """
        TemplatePermissionSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'high_res_pdf': 'bool',
            'proof_pdf': 'bool',
            'jpegs': 'bool',
            'social_sharing': 'bool',
            'can_edit': 'bool',
            'need_admin_approval': 'bool',
            'id': 'str',
            'template_id': 'str',
            'template': 'Template'
        }

        self.attribute_map = {
            'high_res_pdf': 'highResPdf',
            'proof_pdf': 'proofPdf',
            'jpegs': 'jpegs',
            'social_sharing': 'socialSharing',
            'can_edit': 'canEdit',
            'need_admin_approval': 'needAdminApproval',
            'id': 'id',
            'template_id': 'templateId',
            'template': 'template'
        }

        self._high_res_pdf = high_res_pdf
        self._proof_pdf = proof_pdf
        self._jpegs = jpegs
        self._social_sharing = social_sharing
        self._can_edit = can_edit
        self._need_admin_approval = need_admin_approval
        self._id = id
        self._template_id = template_id
        self._template = template


    @property
    def high_res_pdf(self):
        """
        Gets the high_res_pdf of this TemplatePermissionSet.


        :return: The high_res_pdf of this TemplatePermissionSet.
        :rtype: bool
        """
        return self._high_res_pdf

    @high_res_pdf.setter
    def high_res_pdf(self, high_res_pdf):
        """
        Sets the high_res_pdf of this TemplatePermissionSet.


        :param high_res_pdf: The high_res_pdf of this TemplatePermissionSet.
        :type: bool
        """

        self._high_res_pdf = high_res_pdf

    @property
    def proof_pdf(self):
        """
        Gets the proof_pdf of this TemplatePermissionSet.


        :return: The proof_pdf of this TemplatePermissionSet.
        :rtype: bool
        """
        return self._proof_pdf

    @proof_pdf.setter
    def proof_pdf(self, proof_pdf):
        """
        Sets the proof_pdf of this TemplatePermissionSet.


        :param proof_pdf: The proof_pdf of this TemplatePermissionSet.
        :type: bool
        """

        self._proof_pdf = proof_pdf

    @property
    def jpegs(self):
        """
        Gets the jpegs of this TemplatePermissionSet.


        :return: The jpegs of this TemplatePermissionSet.
        :rtype: bool
        """
        return self._jpegs

    @jpegs.setter
    def jpegs(self, jpegs):
        """
        Sets the jpegs of this TemplatePermissionSet.


        :param jpegs: The jpegs of this TemplatePermissionSet.
        :type: bool
        """

        self._jpegs = jpegs

    @property
    def social_sharing(self):
        """
        Gets the social_sharing of this TemplatePermissionSet.


        :return: The social_sharing of this TemplatePermissionSet.
        :rtype: bool
        """
        return self._social_sharing

    @social_sharing.setter
    def social_sharing(self, social_sharing):
        """
        Sets the social_sharing of this TemplatePermissionSet.


        :param social_sharing: The social_sharing of this TemplatePermissionSet.
        :type: bool
        """

        self._social_sharing = social_sharing

    @property
    def can_edit(self):
        """
        Gets the can_edit of this TemplatePermissionSet.


        :return: The can_edit of this TemplatePermissionSet.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """
        Sets the can_edit of this TemplatePermissionSet.


        :param can_edit: The can_edit of this TemplatePermissionSet.
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def need_admin_approval(self):
        """
        Gets the need_admin_approval of this TemplatePermissionSet.


        :return: The need_admin_approval of this TemplatePermissionSet.
        :rtype: bool
        """
        return self._need_admin_approval

    @need_admin_approval.setter
    def need_admin_approval(self, need_admin_approval):
        """
        Sets the need_admin_approval of this TemplatePermissionSet.


        :param need_admin_approval: The need_admin_approval of this TemplatePermissionSet.
        :type: bool
        """

        self._need_admin_approval = need_admin_approval

    @property
    def id(self):
        """
        Gets the id of this TemplatePermissionSet.


        :return: The id of this TemplatePermissionSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TemplatePermissionSet.


        :param id: The id of this TemplatePermissionSet.
        :type: str
        """

        self._id = id

    @property
    def template_id(self):
        """
        Gets the template_id of this TemplatePermissionSet.


        :return: The template_id of this TemplatePermissionSet.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this TemplatePermissionSet.


        :param template_id: The template_id of this TemplatePermissionSet.
        :type: str
        """

        self._template_id = template_id

    @property
    def template(self):
        """
        Gets the template of this TemplatePermissionSet.


        :return: The template of this TemplatePermissionSet.
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this TemplatePermissionSet.


        :param template: The template of this TemplatePermissionSet.
        :type: Template
        """

        self._template = template

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
