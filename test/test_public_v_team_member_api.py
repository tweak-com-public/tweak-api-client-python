# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.7-beta.1
    
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

from __future__ import absolute_import

import os
import sys
import unittest

import TweakApi
from TweakApi.rest import ApiException
from TweakApi.apis.public_v_team_member_api import PublicVTeamMemberApi


class TestPublicVTeamMemberApi(unittest.TestCase):
    """ PublicVTeamMemberApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.public_v_team_member_api.PublicVTeamMemberApi()

    def tearDown(self):
        pass

    def test_v1_team_members_login_post(self):
        """
        Test case for v1_team_members_login_post

        Change portal
        """
        pass

    def test_v1_team_members_logout_post(self):
        """
        Test case for v1_team_members_logout_post

        Logout a TeamMember
        """
        pass

    def test_v1_team_members_post(self):
        """
        Test case for v1_team_members_post

        Create a Member
        """
        pass


if __name__ == '__main__':
    unittest.main()
