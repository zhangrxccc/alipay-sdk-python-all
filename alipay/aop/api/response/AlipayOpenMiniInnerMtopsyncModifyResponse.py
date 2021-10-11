#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerMtopsyncModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerMtopsyncModifyResponse, self).__init__()
        self._code = None
        self._msg = None
        self._sub_code = None
        self._sub_msg = None
        self._type = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_msg(self):
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, value):
        self._sub_msg = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerMtopsyncModifyResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
        if 'type' in response:
            self.type = response['type']
