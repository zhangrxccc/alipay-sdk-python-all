#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromotePageData import PromotePageData


class AlipayDataDataserviceAdPromotepageDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdPromotepageDownloadResponse, self).__init__()
        self._conversion_id = None
        self._list = None
        self._page_no = None
        self._page_size = None
        self._total = None

    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, PromotePageData):
                    self._list.append(i)
                else:
                    self._list.append(PromotePageData.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdPromotepageDownloadResponse, self).parse_response_content(response_content)
        if 'conversion_id' in response:
            self.conversion_id = response['conversion_id']
        if 'list' in response:
            self.list = response['list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
