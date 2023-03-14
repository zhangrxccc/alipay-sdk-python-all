#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcsmartCommonAppInfo import RcsmartCommonAppInfo
from alipay.aop.api.domain.CommercializationDeleteRuleReq import CommercializationDeleteRuleReq


class AlipayFincoreComplianceRcservsmartCustomizeruleDeleteModel(object):

    def __init__(self):
        self._app_info = None
        self._rcsmart_biz_request = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        if isinstance(value, RcsmartCommonAppInfo):
            self._app_info = value
        else:
            self._app_info = RcsmartCommonAppInfo.from_alipay_dict(value)
    @property
    def rcsmart_biz_request(self):
        return self._rcsmart_biz_request

    @rcsmart_biz_request.setter
    def rcsmart_biz_request(self, value):
        if isinstance(value, CommercializationDeleteRuleReq):
            self._rcsmart_biz_request = value
        else:
            self._rcsmart_biz_request = CommercializationDeleteRuleReq.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.rcsmart_biz_request:
            if hasattr(self.rcsmart_biz_request, 'to_alipay_dict'):
                params['rcsmart_biz_request'] = self.rcsmart_biz_request.to_alipay_dict()
            else:
                params['rcsmart_biz_request'] = self.rcsmart_biz_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcservsmartCustomizeruleDeleteModel()
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'rcsmart_biz_request' in d:
            o.rcsmart_biz_request = d['rcsmart_biz_request']
        return o


