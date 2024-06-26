#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopScoreResultInfoDTO import ShopScoreResultInfoDTO


class AlipayDataAntsycmShopdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAntsycmShopdataQueryResponse, self).__init__()
        self._ant_poi = None
        self._city_name = None
        self._county_name = None
        self._gaode_poi = None
        self._latitude = None
        self._longitude = None
        self._province_name = None
        self._shop_address = None
        self._shop_name = None
        self._shop_score_result = None
        self._task_status = None

    @property
    def ant_poi(self):
        return self._ant_poi

    @ant_poi.setter
    def ant_poi(self, value):
        self._ant_poi = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value
    @property
    def gaode_poi(self):
        return self._gaode_poi

    @gaode_poi.setter
    def gaode_poi(self, value):
        self._gaode_poi = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_score_result(self):
        return self._shop_score_result

    @shop_score_result.setter
    def shop_score_result(self, value):
        if isinstance(value, ShopScoreResultInfoDTO):
            self._shop_score_result = value
        else:
            self._shop_score_result = ShopScoreResultInfoDTO.from_alipay_dict(value)
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAntsycmShopdataQueryResponse, self).parse_response_content(response_content)
        if 'ant_poi' in response:
            self.ant_poi = response['ant_poi']
        if 'city_name' in response:
            self.city_name = response['city_name']
        if 'county_name' in response:
            self.county_name = response['county_name']
        if 'gaode_poi' in response:
            self.gaode_poi = response['gaode_poi']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'province_name' in response:
            self.province_name = response['province_name']
        if 'shop_address' in response:
            self.shop_address = response['shop_address']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_score_result' in response:
            self.shop_score_result = response['shop_score_result']
        if 'task_status' in response:
            self.task_status = response['task_status']
