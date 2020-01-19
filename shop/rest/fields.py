# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from rest_framework import serializers


class OrderedDictField(serializers.Field):
    """
    Serializer field which transparently bypasses the internal representation of an OrderedDict.
    """
    def to_representation(self, obj):
        return OrderedDict(obj)

    def to_internal_value(self, data):
        return OrderedDict(data)


class JSONSerializerField(serializers.Field):
    """
    Serializer field which transparently bypasses its object instead of serializing/deserializing.
    """
    def __init__(self, **kwargs):
        # CRn adds treatments for encoder to solve bug using postgres
        encoder = kwargs.pop('encoder', None)
        super(JSONSerializerField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data
