# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mspconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mspconfig.proto',
  package='msp',
  syntax='proto3',
  serialized_pb=_b('\n\x0fmspconfig.proto\x12\x03msp\")\n\tMSPConfig\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\x0c\"\x81\x03\n\x0f\x46\x61\x62ricMSPConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nroot_certs\x18\x02 \x03(\x0c\x12\x1a\n\x12intermediate_certs\x18\x03 \x03(\x0c\x12\x0e\n\x06\x61\x64mins\x18\x04 \x03(\x0c\x12\x17\n\x0frevocation_list\x18\x05 \x03(\x0c\x12\x32\n\x10signing_identity\x18\x06 \x01(\x0b\x32\x18.msp.SigningIdentityInfo\x12@\n\x1forganizational_unit_identifiers\x18\x07 \x03(\x0b\x32\x17.msp.FabricOUIdentifier\x12.\n\rcrypto_config\x18\x08 \x01(\x0b\x32\x17.msp.FabricCryptoConfig\x12\x16\n\x0etls_root_certs\x18\t \x03(\x0c\x12\x1e\n\x16tls_intermediate_certs\x18\n \x03(\x0c\x12)\n\rFabricNodeOUs\x18\x0b \x01(\x0b\x32\x12.msp.FabricNodeOUs\"^\n\x12\x46\x61\x62ricCryptoConfig\x12\x1d\n\x15signature_hash_family\x18\x01 \x01(\t\x12)\n!identity_identifier_hash_function\x18\x02 \x01(\t\"X\n\x0fIdemixMSPConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03IPk\x18\x02 \x01(\x0c\x12*\n\x06signer\x18\x03 \x01(\x0b\x32\x1a.msp.IdemixMSPSignerConfig\"k\n\x15IdemixMSPSignerConfig\x12\x0c\n\x04\x43red\x18\x01 \x01(\x0c\x12\n\n\x02Sk\x18\x02 \x01(\x0c\x12&\n\x1eorganizational_unit_identifier\x18\x03 \x01(\t\x12\x10\n\x08is_admin\x18\x04 \x01(\x08\"R\n\x13SigningIdentityInfo\x12\x15\n\rpublic_signer\x18\x01 \x01(\x0c\x12$\n\x0eprivate_signer\x18\x02 \x01(\x0b\x32\x0c.msp.KeyInfo\"7\n\x07KeyInfo\x12\x16\n\x0ekey_identifier\x18\x01 \x01(\t\x12\x14\n\x0ckey_material\x18\x02 \x01(\x0c\"Q\n\x12\x46\x61\x62ricOUIdentifier\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12&\n\x1eorganizational_unit_identifier\x18\x02 \x01(\t\"\xbd\x01\n\rFabricNodeOUs\x12\x0e\n\x06\x45nable\x18\x01 \x01(\x08\x12\x33\n\x12\x63lientOUIdentifier\x18\x02 \x01(\x0b\x32\x17.msp.FabricOUIdentifier\x12\x31\n\x10peerOUIdentifier\x18\x03 \x01(\x0b\x32\x17.msp.FabricOUIdentifier\x12\x34\n\x13ordererOUIdentifier\x18\x04 \x01(\x0b\x32\x17.msp.FabricOUIdentifierB*Z(github.com/hyperledger/fabric/protos/mspb\x06proto3')
)




_MSPCONFIG = _descriptor.Descriptor(
  name='MSPConfig',
  full_name='msp.MSPConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='msp.MSPConfig.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='msp.MSPConfig.config', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=65,
)


_FABRICMSPCONFIG = _descriptor.Descriptor(
  name='FabricMSPConfig',
  full_name='msp.FabricMSPConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='msp.FabricMSPConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_certs', full_name='msp.FabricMSPConfig.root_certs', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intermediate_certs', full_name='msp.FabricMSPConfig.intermediate_certs', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admins', full_name='msp.FabricMSPConfig.admins', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revocation_list', full_name='msp.FabricMSPConfig.revocation_list', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signing_identity', full_name='msp.FabricMSPConfig.signing_identity', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifiers', full_name='msp.FabricMSPConfig.organizational_unit_identifiers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crypto_config', full_name='msp.FabricMSPConfig.crypto_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_root_certs', full_name='msp.FabricMSPConfig.tls_root_certs', index=8,
      number=9, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_intermediate_certs', full_name='msp.FabricMSPConfig.tls_intermediate_certs', index=9,
      number=10, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FabricNodeOUs', full_name='msp.FabricMSPConfig.FabricNodeOUs', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=453,
)


_FABRICCRYPTOCONFIG = _descriptor.Descriptor(
  name='FabricCryptoConfig',
  full_name='msp.FabricCryptoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_hash_family', full_name='msp.FabricCryptoConfig.signature_hash_family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity_identifier_hash_function', full_name='msp.FabricCryptoConfig.identity_identifier_hash_function', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=549,
)


_IDEMIXMSPCONFIG = _descriptor.Descriptor(
  name='IdemixMSPConfig',
  full_name='msp.IdemixMSPConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='msp.IdemixMSPConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IPk', full_name='msp.IdemixMSPConfig.IPk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signer', full_name='msp.IdemixMSPConfig.signer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=639,
)


_IDEMIXMSPSIGNERCONFIG = _descriptor.Descriptor(
  name='IdemixMSPSignerConfig',
  full_name='msp.IdemixMSPSignerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Cred', full_name='msp.IdemixMSPSignerConfig.Cred', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Sk', full_name='msp.IdemixMSPSignerConfig.Sk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifier', full_name='msp.IdemixMSPSignerConfig.organizational_unit_identifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_admin', full_name='msp.IdemixMSPSignerConfig.is_admin', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=748,
)


_SIGNINGIDENTITYINFO = _descriptor.Descriptor(
  name='SigningIdentityInfo',
  full_name='msp.SigningIdentityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_signer', full_name='msp.SigningIdentityInfo.public_signer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_signer', full_name='msp.SigningIdentityInfo.private_signer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=750,
  serialized_end=832,
)


_KEYINFO = _descriptor.Descriptor(
  name='KeyInfo',
  full_name='msp.KeyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_identifier', full_name='msp.KeyInfo.key_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_material', full_name='msp.KeyInfo.key_material', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=889,
)


_FABRICOUIDENTIFIER = _descriptor.Descriptor(
  name='FabricOUIdentifier',
  full_name='msp.FabricOUIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificate', full_name='msp.FabricOUIdentifier.certificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifier', full_name='msp.FabricOUIdentifier.organizational_unit_identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=891,
  serialized_end=972,
)


_FABRICNODEOUS = _descriptor.Descriptor(
  name='FabricNodeOUs',
  full_name='msp.FabricNodeOUs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Enable', full_name='msp.FabricNodeOUs.Enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientOUIdentifier', full_name='msp.FabricNodeOUs.clientOUIdentifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peerOUIdentifier', full_name='msp.FabricNodeOUs.peerOUIdentifier', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ordererOUIdentifier', full_name='msp.FabricNodeOUs.ordererOUIdentifier', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=975,
  serialized_end=1164,
)

_FABRICMSPCONFIG.fields_by_name['signing_identity'].message_type = _SIGNINGIDENTITYINFO
_FABRICMSPCONFIG.fields_by_name['organizational_unit_identifiers'].message_type = _FABRICOUIDENTIFIER
_FABRICMSPCONFIG.fields_by_name['crypto_config'].message_type = _FABRICCRYPTOCONFIG
_FABRICMSPCONFIG.fields_by_name['FabricNodeOUs'].message_type = _FABRICNODEOUS
_IDEMIXMSPCONFIG.fields_by_name['signer'].message_type = _IDEMIXMSPSIGNERCONFIG
_SIGNINGIDENTITYINFO.fields_by_name['private_signer'].message_type = _KEYINFO
_FABRICNODEOUS.fields_by_name['clientOUIdentifier'].message_type = _FABRICOUIDENTIFIER
_FABRICNODEOUS.fields_by_name['peerOUIdentifier'].message_type = _FABRICOUIDENTIFIER
_FABRICNODEOUS.fields_by_name['ordererOUIdentifier'].message_type = _FABRICOUIDENTIFIER
DESCRIPTOR.message_types_by_name['MSPConfig'] = _MSPCONFIG
DESCRIPTOR.message_types_by_name['FabricMSPConfig'] = _FABRICMSPCONFIG
DESCRIPTOR.message_types_by_name['FabricCryptoConfig'] = _FABRICCRYPTOCONFIG
DESCRIPTOR.message_types_by_name['IdemixMSPConfig'] = _IDEMIXMSPCONFIG
DESCRIPTOR.message_types_by_name['IdemixMSPSignerConfig'] = _IDEMIXMSPSIGNERCONFIG
DESCRIPTOR.message_types_by_name['SigningIdentityInfo'] = _SIGNINGIDENTITYINFO
DESCRIPTOR.message_types_by_name['KeyInfo'] = _KEYINFO
DESCRIPTOR.message_types_by_name['FabricOUIdentifier'] = _FABRICOUIDENTIFIER
DESCRIPTOR.message_types_by_name['FabricNodeOUs'] = _FABRICNODEOUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MSPConfig = _reflection.GeneratedProtocolMessageType('MSPConfig', (_message.Message,), dict(
  DESCRIPTOR = _MSPCONFIG,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.MSPConfig)
  ))
_sym_db.RegisterMessage(MSPConfig)

FabricMSPConfig = _reflection.GeneratedProtocolMessageType('FabricMSPConfig', (_message.Message,), dict(
  DESCRIPTOR = _FABRICMSPCONFIG,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricMSPConfig)
  ))
_sym_db.RegisterMessage(FabricMSPConfig)

FabricCryptoConfig = _reflection.GeneratedProtocolMessageType('FabricCryptoConfig', (_message.Message,), dict(
  DESCRIPTOR = _FABRICCRYPTOCONFIG,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricCryptoConfig)
  ))
_sym_db.RegisterMessage(FabricCryptoConfig)

IdemixMSPConfig = _reflection.GeneratedProtocolMessageType('IdemixMSPConfig', (_message.Message,), dict(
  DESCRIPTOR = _IDEMIXMSPCONFIG,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.IdemixMSPConfig)
  ))
_sym_db.RegisterMessage(IdemixMSPConfig)

IdemixMSPSignerConfig = _reflection.GeneratedProtocolMessageType('IdemixMSPSignerConfig', (_message.Message,), dict(
  DESCRIPTOR = _IDEMIXMSPSIGNERCONFIG,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.IdemixMSPSignerConfig)
  ))
_sym_db.RegisterMessage(IdemixMSPSignerConfig)

SigningIdentityInfo = _reflection.GeneratedProtocolMessageType('SigningIdentityInfo', (_message.Message,), dict(
  DESCRIPTOR = _SIGNINGIDENTITYINFO,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.SigningIdentityInfo)
  ))
_sym_db.RegisterMessage(SigningIdentityInfo)

KeyInfo = _reflection.GeneratedProtocolMessageType('KeyInfo', (_message.Message,), dict(
  DESCRIPTOR = _KEYINFO,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.KeyInfo)
  ))
_sym_db.RegisterMessage(KeyInfo)

FabricOUIdentifier = _reflection.GeneratedProtocolMessageType('FabricOUIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _FABRICOUIDENTIFIER,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricOUIdentifier)
  ))
_sym_db.RegisterMessage(FabricOUIdentifier)

FabricNodeOUs = _reflection.GeneratedProtocolMessageType('FabricNodeOUs', (_message.Message,), dict(
  DESCRIPTOR = _FABRICNODEOUS,
  __module__ = 'mspconfig_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricNodeOUs)
  ))
_sym_db.RegisterMessage(FabricNodeOUs)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z(github.com/hyperledger/fabric/protos/msp'))
# @@protoc_insertion_point(module_scope)
