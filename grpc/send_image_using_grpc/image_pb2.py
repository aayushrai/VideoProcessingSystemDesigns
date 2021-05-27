# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bimage.proto\";\n\x08\x42\x36\x34Image\x12\x10\n\x08\x62\x36\x34image\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\"\x1a\n\x08UserInfo\x12\x0e\n\x06\x66\x61\x63\x65id\x18\x01 \x01(\t29\n\x12ImagePreprocessing\x12#\n\tfacerecog\x12\t.B64Image\x1a\t.UserInfo\"\x00\x62\x06proto3'
)




_B64IMAGE = _descriptor.Descriptor(
  name='B64Image',
  full_name='B64Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='b64image', full_name='B64Image.b64image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='B64Image.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='B64Image.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=74,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceid', full_name='UserInfo.faceid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['B64Image'] = _B64IMAGE
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

B64Image = _reflection.GeneratedProtocolMessageType('B64Image', (_message.Message,), {
  'DESCRIPTOR' : _B64IMAGE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:B64Image)
  })
_sym_db.RegisterMessage(B64Image)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)



_IMAGEPREPROCESSING = _descriptor.ServiceDescriptor(
  name='ImagePreprocessing',
  full_name='ImagePreprocessing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=104,
  serialized_end=161,
  methods=[
  _descriptor.MethodDescriptor(
    name='facerecog',
    full_name='ImagePreprocessing.facerecog',
    index=0,
    containing_service=None,
    input_type=_B64IMAGE,
    output_type=_USERINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGEPREPROCESSING)

DESCRIPTOR.services_by_name['ImagePreprocessing'] = _IMAGEPREPROCESSING

# @@protoc_insertion_point(module_scope)
