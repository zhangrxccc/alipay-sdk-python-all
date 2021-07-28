#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppDeployResponse import MiniAppDeployResponse


class AlipayOpenMiniAppdeployByappidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAppdeployByappidQueryResponse, self).__init__()
        self._deploys = None
        self._total = None

    @property
    def deploys(self):
        return self._deploys

    @deploys.setter
    def deploys(self, value):
        if isinstance(value, list):
            self._deploys = list()
            for i in value:
                if isinstance(i, MiniAppDeployResponse):
                    self._deploys.append(i)
                else:
                    self._deploys.append(MiniAppDeployResponse.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAppdeployByappidQueryResponse, self).parse_response_content(response_content)
        if 'deploys' in response:
            self.deploys = response['deploys']
        if 'total' in response:
            self.total = response['total']
