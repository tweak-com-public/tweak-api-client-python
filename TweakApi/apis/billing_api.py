# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-beta.0
    
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


class BillingApi(object):
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

    def billings_change_stream_get(self, **kwargs):
        """
        Create a change stream.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_change_stream_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str options: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billings_change_stream_get_with_http_info(**kwargs)
        else:
            (data) = self.billings_change_stream_get_with_http_info(**kwargs)
            return data

    def billings_change_stream_get_with_http_info(self, **kwargs):
        """
        Create a change stream.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_change_stream_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str options: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['options']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_change_stream_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/Billings/change-stream'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'options' in params:
            query_params['options'] = params['options']

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
                                            response_type='file',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def billings_change_stream_post(self, **kwargs):
        """
        Create a change stream.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_change_stream_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str options: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billings_change_stream_post_with_http_info(**kwargs)
        else:
            (data) = self.billings_change_stream_post_with_http_info(**kwargs)
            return data

    def billings_change_stream_post_with_http_info(self, **kwargs):
        """
        Create a change stream.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_change_stream_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str options: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['options']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_change_stream_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/Billings/change-stream'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'options' in params:
            form_params.append(('options', params['options']))

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

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='file',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def billings_countries_get(self, **kwargs):
        """
        List available countries
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_countries_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billings_countries_get_with_http_info(**kwargs)
        else:
            (data) = self.billings_countries_get_with_http_info(**kwargs)
            return data

    def billings_countries_get_with_http_info(self, **kwargs):
        """
        List available countries
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_countries_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[str]
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
                    " to method billings_countries_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/Billings/countries'.replace('{format}', 'json')
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
                                            response_type='list[str]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def billings_id_put(self, id, **kwargs):
        """
        Replace attributes for a model instance and persist it into the data source.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Model id (required)
        :param Billing data: Model instance data
        :return: Billing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billings_id_put_with_http_info(id, **kwargs)
        else:
            (data) = self.billings_id_put_with_http_info(id, **kwargs)
            return data

    def billings_id_put_with_http_info(self, id, **kwargs):
        """
        Replace attributes for a model instance and persist it into the data source.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_id_put_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Model id (required)
        :param Billing data: Model instance data
        :return: Billing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `billings_id_put`")


        collection_formats = {}

        resource_path = '/Billings/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Billing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def billings_id_replace_post(self, id, **kwargs):
        """
        Replace attributes for a model instance and persist it into the data source.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_id_replace_post(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Model id (required)
        :param Billing data: Model instance data
        :return: Billing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billings_id_replace_post_with_http_info(id, **kwargs)
        else:
            (data) = self.billings_id_replace_post_with_http_info(id, **kwargs)
            return data

    def billings_id_replace_post_with_http_info(self, id, **kwargs):
        """
        Replace attributes for a model instance and persist it into the data source.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_id_replace_post_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Model id (required)
        :param Billing data: Model instance data
        :return: Billing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_id_replace_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `billings_id_replace_post`")


        collection_formats = {}

        resource_path = '/Billings/{id}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Billing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def billings_tax_evidence_country_vat_get(self, country, vat, **kwargs):
        """
        Get Tax Evidence by country and VAT
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_tax_evidence_country_vat_get(country, vat, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country:  (required)
        :param str vat:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billings_tax_evidence_country_vat_get_with_http_info(country, vat, **kwargs)
        else:
            (data) = self.billings_tax_evidence_country_vat_get_with_http_info(country, vat, **kwargs)
            return data

    def billings_tax_evidence_country_vat_get_with_http_info(self, country, vat, **kwargs):
        """
        Get Tax Evidence by country and VAT
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billings_tax_evidence_country_vat_get_with_http_info(country, vat, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country:  (required)
        :param str vat:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country', 'vat']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billings_tax_evidence_country_vat_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country' is set
        if ('country' not in params) or (params['country'] is None):
            raise ValueError("Missing the required parameter `country` when calling `billings_tax_evidence_country_vat_get`")
        # verify the required parameter 'vat' is set
        if ('vat' not in params) or (params['vat'] is None):
            raise ValueError("Missing the required parameter `vat` when calling `billings_tax_evidence_country_vat_get`")


        collection_formats = {}

        resource_path = '/Billings/taxEvidence/{country}/{vat}'.replace('{format}', 'json')
        path_params = {}
        if 'country' in params:
            path_params['country'] = params['country']
        if 'vat' in params:
            path_params['vat'] = params['vat']

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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)
