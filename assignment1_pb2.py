# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assignment1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61ssignment1.proto\x12\x0b\x61ssignment1\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"/\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x05\"3\n\x05Liste\x12*\n\x04word\x18\x01 \x03(\x0b\x32\x1c.assignment1.MessageResponse2\x83\x01\n\x13\x46requencyCalculator\x12\x37\n\tCalculate\x12\x14.assignment1.Message\x1a\x12.assignment1.Liste\"\x00\x12\x33\n\x07\x43ombine\x12\x12.assignment1.Liste\x1a\x12.assignment1.Liste\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'assignment1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MESSAGE']._serialized_start=34
  _globals['_MESSAGE']._serialized_end=60
  _globals['_MESSAGERESPONSE']._serialized_start=62
  _globals['_MESSAGERESPONSE']._serialized_end=109
  _globals['_LISTE']._serialized_start=111
  _globals['_LISTE']._serialized_end=162
  _globals['_FREQUENCYCALCULATOR']._serialized_start=165
  _globals['_FREQUENCYCALCULATOR']._serialized_end=296
# @@protoc_insertion_point(module_scope)
