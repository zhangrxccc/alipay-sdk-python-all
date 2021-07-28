#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeAdvanceConsultModel(object):

    def __init__(self):
        self._agreement_no = None
        self._alipay_user_id = None
        self._consult_scene = None
        self._estimated_order_amount = None
        self._industry_product_code = None
        self._out_trade_no = None
        self._sub_merchant_id = None
        self._sub_merchant_type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def consult_scene(self):
        return self._consult_scene

    @consult_scene.setter
    def consult_scene(self, value):
        self._consult_scene = value
    @property
    def estimated_order_amount(self):
        return self._estimated_order_amount

    @estimated_order_amount.setter
    def estimated_order_amount(self, value):
        self._estimated_order_amount = value
    @property
    def industry_product_code(self):
        return self._industry_product_code

    @industry_product_code.setter
    def industry_product_code(self, value):
        self._industry_product_code = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def sub_merchant_type(self):
        return self._sub_merchant_type

    @sub_merchant_type.setter
    def sub_merchant_type(self, value):
        self._sub_merchant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.consult_scene:
            if hasattr(self.consult_scene, 'to_alipay_dict'):
                params['consult_scene'] = self.consult_scene.to_alipay_dict()
            else:
                params['consult_scene'] = self.consult_scene
        if self.estimated_order_amount:
            if hasattr(self.estimated_order_amount, 'to_alipay_dict'):
                params['estimated_order_amount'] = self.estimated_order_amount.to_alipay_dict()
            else:
                params['estimated_order_amount'] = self.estimated_order_amount
        if self.industry_product_code:
            if hasattr(self.industry_product_code, 'to_alipay_dict'):
                params['industry_product_code'] = self.industry_product_code.to_alipay_dict()
            else:
                params['industry_product_code'] = self.industry_product_code
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.sub_merchant_type:
            if hasattr(self.sub_merchant_type, 'to_alipay_dict'):
                params['sub_merchant_type'] = self.sub_merchant_type.to_alipay_dict()
            else:
                params['sub_merchant_type'] = self.sub_merchant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAdvanceConsultModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'consult_scene' in d:
            o.consult_scene = d['consult_scene']
        if 'estimated_order_amount' in d:
            o.estimated_order_amount = d['estimated_order_amount']
        if 'industry_product_code' in d:
            o.industry_product_code = d['industry_product_code']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'sub_merchant_type' in d:
            o.sub_merchant_type = d['sub_merchant_type']
        return o


