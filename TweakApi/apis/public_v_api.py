# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.7-beta.3
    
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


class PublicVApi(object):
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

    def v1_base_locale_country_code_get(self, country_code, **kwargs):
        """
        Get locale from Country Code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_base_locale_country_code_get(country_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code: Country code (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_base_locale_country_code_get_with_http_info(country_code, **kwargs)
        else:
            (data) = self.v1_base_locale_country_code_get_with_http_info(country_code, **kwargs)
            return data

    def v1_base_locale_country_code_get_with_http_info(self, country_code, **kwargs):
        """
        Get locale from Country Code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_base_locale_country_code_get_with_http_info(country_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code: Country code (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_base_locale_country_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params) or (params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `v1_base_locale_country_code_get`")


        collection_formats = {}

        resource_path = '/v1/Base/locale/country/code'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'country_code' in params:
            query_params['countryCode'] = params['country_code']

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

        return self.api_client.call_api(resource_path, 'GET',
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

    def v1_base_locale_country_name_get(self, country_name, **kwargs):
        """
        Get locale from Country Name
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_base_locale_country_name_get(country_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_name: Country name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_base_locale_country_name_get_with_http_info(country_name, **kwargs)
        else:
            (data) = self.v1_base_locale_country_name_get_with_http_info(country_name, **kwargs)
            return data

    def v1_base_locale_country_name_get_with_http_info(self, country_name, **kwargs):
        """
        Get locale from Country Name
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_base_locale_country_name_get_with_http_info(country_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_name: Country name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_base_locale_country_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_name' is set
        if ('country_name' not in params) or (params['country_name'] is None):
            raise ValueError("Missing the required parameter `country_name` when calling `v1_base_locale_country_name_get`")


        collection_formats = {}

        resource_path = '/v1/Base/locale/country/name'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'country_name' in params:
            query_params['countryName'] = params['country_name']

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

        return self.api_client.call_api(resource_path, 'GET',
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

    def v1_base_locale_get(self, **kwargs):
        """
        Get locale from client IP
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_base_locale_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_base_locale_get_with_http_info(**kwargs)
        else:
            (data) = self.v1_base_locale_get_with_http_info(**kwargs)
            return data

    def v1_base_locale_get_with_http_info(self, **kwargs):
        """
        Get locale from client IP
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_base_locale_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: object
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
                    " to method v1_base_locale_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v1/Base/locale'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET',
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
