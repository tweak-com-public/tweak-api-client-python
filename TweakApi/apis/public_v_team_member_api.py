# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.0
    
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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PublicVTeamMemberApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v1_team_members_login_post(self, id, portal_id, **kwargs):
        """
        Change portal
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_team_members_login_post(id, portal_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: TeamMember id (required)
        :param str portal_id: Portal id (required)
        :return: TeamMemberAccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_team_members_login_post_with_http_info(id, portal_id, **kwargs)
        else:
            (data) = self.v1_team_members_login_post_with_http_info(id, portal_id, **kwargs)
            return data

    def v1_team_members_login_post_with_http_info(self, id, portal_id, **kwargs):
        """
        Change portal
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_team_members_login_post_with_http_info(id, portal_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: TeamMember id (required)
        :param str portal_id: Portal id (required)
        :return: TeamMemberAccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'portal_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_team_members_login_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_team_members_login_post`")
        # verify the required parameter 'portal_id' is set
        if ('portal_id' not in params) or (params['portal_id'] is None):
            raise ValueError("Missing the required parameter `portal_id` when calling `v1_team_members_login_post`")


        collection_formats = {}

        resource_path = '/v1/TeamMembers/login'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'portal_id' in params:
            path_params['portalId'] = params['portal_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])

        # Authentication setting
        auth_settings = ['access_token', 'teamKey']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TeamMemberAccessToken',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def v1_team_members_logout_post(self, **kwargs):
        """
        Logout a TeamMember
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_team_members_logout_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_team_members_logout_post_with_http_info(**kwargs)
        else:
            (data) = self.v1_team_members_logout_post_with_http_info(**kwargs)
            return data

    def v1_team_members_logout_post_with_http_info(self, **kwargs):
        """
        Logout a TeamMember
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_team_members_logout_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_team_members_logout_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v1/TeamMembers/logout'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])

        # Authentication setting
        auth_settings = ['access_token', 'teamKey']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def v1_team_members_post(self, data, **kwargs):
        """
        Create a Member
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_team_members_post(data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PublicV1TeamMember data: Data to create Member (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_team_members_post_with_http_info(data, **kwargs)
        else:
            (data) = self.v1_team_members_post_with_http_info(data, **kwargs)
            return data

    def v1_team_members_post_with_http_info(self, data, **kwargs):
        """
        Create a Member
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_team_members_post_with_http_info(data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PublicV1TeamMember data: Data to create Member (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_team_members_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `v1_team_members_post`")


        collection_formats = {}

        resource_path = '/v1/TeamMembers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])

        # Authentication setting
        auth_settings = ['access_token', 'teamKey']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)
