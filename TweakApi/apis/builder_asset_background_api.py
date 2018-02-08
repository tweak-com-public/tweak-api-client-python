# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.1
    
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


class BuilderAssetBackgroundApi(object):
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

    def builder_asset_backgrounds_folders_folder_path_get(self, folder_path, **kwargs):
        """
        Get Builder Asset Backgrounds on a folders
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.builder_asset_backgrounds_folders_folder_path_get(folder_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_path: Folder path for backgrounds (required)
        :param str filter: Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: list[CloudinaryImage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.builder_asset_backgrounds_folders_folder_path_get_with_http_info(folder_path, **kwargs)
        else:
            (data) = self.builder_asset_backgrounds_folders_folder_path_get_with_http_info(folder_path, **kwargs)
            return data

    def builder_asset_backgrounds_folders_folder_path_get_with_http_info(self, folder_path, **kwargs):
        """
        Get Builder Asset Backgrounds on a folders
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.builder_asset_backgrounds_folders_folder_path_get_with_http_info(folder_path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str folder_path: Folder path for backgrounds (required)
        :param str filter: Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: list[CloudinaryImage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_path', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method builder_asset_backgrounds_folders_folder_path_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_path' is set
        if ('folder_path' not in params) or (params['folder_path'] is None):
            raise ValueError("Missing the required parameter `folder_path` when calling `builder_asset_backgrounds_folders_folder_path_get`")


        collection_formats = {}

        resource_path = '/BuilderAsset/backgrounds/folders/{folderPath}'.replace('{format}', 'json')
        path_params = {}
        if 'folder_path' in params:
            path_params['folderPath'] = params['folder_path']

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']

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
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[CloudinaryImage]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def builder_asset_backgrounds_folders_get(self, **kwargs):
        """
        Get folders for Builder Asset Backgrounds
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.builder_asset_backgrounds_folders_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[BuilderAssetBackgroundFolder]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.builder_asset_backgrounds_folders_get_with_http_info(**kwargs)
        else:
            (data) = self.builder_asset_backgrounds_folders_get_with_http_info(**kwargs)
            return data

    def builder_asset_backgrounds_folders_get_with_http_info(self, **kwargs):
        """
        Get folders for Builder Asset Backgrounds
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.builder_asset_backgrounds_folders_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[BuilderAssetBackgroundFolder]
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
                    " to method builder_asset_backgrounds_folders_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/BuilderAsset/backgrounds/folders'.replace('{format}', 'json')
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
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[BuilderAssetBackgroundFolder]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def builder_asset_backgrounds_get(self, **kwargs):
        """
        Get all Builder Asset Backgrounds
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.builder_asset_backgrounds_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: list[CloudinaryImage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.builder_asset_backgrounds_get_with_http_info(**kwargs)
        else:
            (data) = self.builder_asset_backgrounds_get_with_http_info(**kwargs)
            return data

    def builder_asset_backgrounds_get_with_http_info(self, **kwargs):
        """
        Get all Builder Asset Backgrounds
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.builder_asset_backgrounds_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: list[CloudinaryImage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method builder_asset_backgrounds_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/BuilderAsset/backgrounds'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']

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
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[CloudinaryImage]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)
