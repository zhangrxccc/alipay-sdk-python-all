#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsUserpermissionIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsUserpermissionIdentifyResponse, self).__init__()
        self._permit = None

    @property
    def permit(self):
        return self._permit

    @permit.setter
    def permit(self, value):
        self._permit = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsUserpermissionIdentifyResponse, self).parse_response_content(response_content)
        if 'permit' in response:
            self.permit = response['permit']
