# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65vent.proto\x12*com.olist.su.channels.channelsintegrations\"u\n\x05\x45vent\x12\x10\n\x08trace_id\x18\x01 \x01(\t\x12\r\n\x05\x61gent\x18\x02 \x01(\t\x12(\n\x1c\x64\x65precated_internal_attempts\x18\x03 \x01(\x05\x42\x02\x18\x01\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\tB\x08Z\x06./;genb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006./;gen'
  _EVENT.fields_by_name['deprecated_internal_attempts']._options = None
  _EVENT.fields_by_name['deprecated_internal_attempts']._serialized_options = b'\030\001'
  _EVENT._serialized_start=59
  _EVENT._serialized_end=176
# @@protoc_insertion_point(module_scope)
