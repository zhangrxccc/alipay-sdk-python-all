#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseUsercenterBaseinfoQueryModel(object):

    def __init__(self):
        self._authorization = None
        self._passport_id = None

    @property
    def authorization(self):
        return self._authorization

    @authorization.setter
    def authorization(self, value):
        self._authorization = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization:
            if hasattr(self.authorization, 'to_alipay_dict'):
                params['authorization'] = self.authorization.to_alipay_dict()
            else:
                params['authorization'] = self.authorization
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseUsercenterBaseinfoQueryModel()
        if 'authorization' in d:
            o.authorization = d['authorization']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        return o


