#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HotelGuests import HotelGuests


class HotelRoomInfo(object):

    def __init__(self):
        self._guests = None
        self._room_number = None
        self._room_type = None

    @property
    def guests(self):
        return self._guests

    @guests.setter
    def guests(self, value):
        if isinstance(value, list):
            self._guests = list()
            for i in value:
                if isinstance(i, HotelGuests):
                    self._guests.append(i)
                else:
                    self._guests.append(HotelGuests.from_alipay_dict(i))
    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.guests:
            if isinstance(self.guests, list):
                for i in range(0, len(self.guests)):
                    element = self.guests[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.guests[i] = element.to_alipay_dict()
            if hasattr(self.guests, 'to_alipay_dict'):
                params['guests'] = self.guests.to_alipay_dict()
            else:
                params['guests'] = self.guests
        if self.room_number:
            if hasattr(self.room_number, 'to_alipay_dict'):
                params['room_number'] = self.room_number.to_alipay_dict()
            else:
                params['room_number'] = self.room_number
        if self.room_type:
            if hasattr(self.room_type, 'to_alipay_dict'):
                params['room_type'] = self.room_type.to_alipay_dict()
            else:
                params['room_type'] = self.room_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelRoomInfo()
        if 'guests' in d:
            o.guests = d['guests']
        if 'room_number' in d:
            o.room_number = d['room_number']
        if 'room_type' in d:
            o.room_type = d['room_type']
        return o


