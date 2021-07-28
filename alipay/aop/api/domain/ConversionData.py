#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConversionProperty import ConversionProperty


class ConversionData(object):

    def __init__(self):
        self._biz_no = None
        self._conversion_id = None
        self._conversion_time = None
        self._conversion_type = None
        self._creative_id = None
        self._group_id = None
        self._plan_id = None
        self._principal_tag = None
        self._property_list = None
        self._source = None
        self._uuid = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def conversion_time(self):
        return self._conversion_time

    @conversion_time.setter
    def conversion_time(self, value):
        self._conversion_time = value
    @property
    def conversion_type(self):
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        self._conversion_type = value
    @property
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, ConversionProperty):
                    self._property_list.append(i)
                else:
                    self._property_list.append(ConversionProperty.from_alipay_dict(i))
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.conversion_id:
            if hasattr(self.conversion_id, 'to_alipay_dict'):
                params['conversion_id'] = self.conversion_id.to_alipay_dict()
            else:
                params['conversion_id'] = self.conversion_id
        if self.conversion_time:
            if hasattr(self.conversion_time, 'to_alipay_dict'):
                params['conversion_time'] = self.conversion_time.to_alipay_dict()
            else:
                params['conversion_time'] = self.conversion_time
        if self.conversion_type:
            if hasattr(self.conversion_type, 'to_alipay_dict'):
                params['conversion_type'] = self.conversion_type.to_alipay_dict()
            else:
                params['conversion_type'] = self.conversion_type
        if self.creative_id:
            if hasattr(self.creative_id, 'to_alipay_dict'):
                params['creative_id'] = self.creative_id.to_alipay_dict()
            else:
                params['creative_id'] = self.creative_id
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.property_list:
            if isinstance(self.property_list, list):
                for i in range(0, len(self.property_list)):
                    element = self.property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_list[i] = element.to_alipay_dict()
            if hasattr(self.property_list, 'to_alipay_dict'):
                params['property_list'] = self.property_list.to_alipay_dict()
            else:
                params['property_list'] = self.property_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConversionData()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'conversion_id' in d:
            o.conversion_id = d['conversion_id']
        if 'conversion_time' in d:
            o.conversion_time = d['conversion_time']
        if 'conversion_type' in d:
            o.conversion_type = d['conversion_type']
        if 'creative_id' in d:
            o.creative_id = d['creative_id']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'property_list' in d:
            o.property_list = d['property_list']
        if 'source' in d:
            o.source = d['source']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


