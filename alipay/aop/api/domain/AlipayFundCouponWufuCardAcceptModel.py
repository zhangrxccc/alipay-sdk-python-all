#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponWufuCardAcceptModel(object):

    def __init__(self):
        self._card_id = None
        self._sender_user_id = None
        self._source = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def sender_user_id(self):
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, value):
        self._sender_user_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.sender_user_id:
            if hasattr(self.sender_user_id, 'to_alipay_dict'):
                params['sender_user_id'] = self.sender_user_id.to_alipay_dict()
            else:
                params['sender_user_id'] = self.sender_user_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundCouponWufuCardAcceptModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'sender_user_id' in d:
            o.sender_user_id = d['sender_user_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


