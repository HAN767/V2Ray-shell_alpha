# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geoSite.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='geoSite.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rgeoSite.proto\"(\n\x0bNetworkList\x12\x19\n\x07network\x18\x01 \x03(\x0e\x32\x08.Network\"%\n\tPortRange\x12\x0c\n\x04\x46rom\x18\x01 \x01(\r\x12\n\n\x02To\x18\x02 \x01(\r\"]\n\x06\x44omain\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.Domain.Type\x12\r\n\x05value\x18\x02 \x01(\t\"(\n\x04Type\x12\t\n\x05Plain\x10\x00\x12\t\n\x05Regex\x10\x01\x12\n\n\x06\x44omain\x10\x02\"\"\n\x04\x43IDR\x12\n\n\x02ip\x18\x01 \x01(\x0c\x12\x0e\n\x06prefix\x18\x02 \x01(\r\"2\n\x05GeoIP\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12\x13\n\x04\x63idr\x18\x02 \x03(\x0b\x32\x05.CIDR\"\"\n\tGeoIPList\x12\x15\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x06.GeoIP\"8\n\x07GeoSite\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12\x17\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x07.Domain\"&\n\x0bGeoSiteList\x12\x17\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x08.GeoSite\"\xd1\x01\n\x0bRoutingRule\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x17\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x07.Domain\x12\x13\n\x04\x63idr\x18\x03 \x03(\x0b\x32\x05.CIDR\x12\x1e\n\nport_range\x18\x04 \x01(\x0b\x32\n.PortRange\x12\"\n\x0cnetwork_list\x18\x05 \x01(\x0b\x32\x0c.NetworkList\x12\x1a\n\x0bsource_cidr\x18\x06 \x03(\x0b\x32\x05.CIDR\x12\x12\n\nuser_email\x18\x07 \x03(\t\x12\x13\n\x0binbound_tag\x18\x08 \x03(\t\"\x9e\x01\n\x06\x43onfig\x12/\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32\x16.Config.DomainStrategy\x12\x1a\n\x04rule\x18\x02 \x03(\x0b\x32\x0c.RoutingRule\"G\n\x0e\x44omainStrategy\x12\x08\n\x04\x41sIs\x10\x00\x12\t\n\x05UseIp\x10\x01\x12\x10\n\x0cIpIfNonMatch\x10\x02\x12\x0e\n\nIpOnDemand\x10\x03*8\n\x07Network\x12\x0b\n\x07Unknown\x10\x00\x12\x0e\n\x06RawTCP\x10\x01\x1a\x02\x08\x01\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03UDP\x10\x03\x62\x06proto3')
)

_NETWORK = _descriptor.EnumDescriptor(
  name='Network',
  full_name='Network',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RawTCP', index=1, number=1,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\010\001')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=788,
  serialized_end=844,
)
_sym_db.RegisterEnumDescriptor(_NETWORK)

Network = enum_type_wrapper.EnumTypeWrapper(_NETWORK)
Unknown = 0
RawTCP = 1
TCP = 2
UDP = 3


_DOMAIN_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Domain.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Plain', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Regex', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Domain', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=151,
  serialized_end=191,
)
_sym_db.RegisterEnumDescriptor(_DOMAIN_TYPE)

_CONFIG_DOMAINSTRATEGY = _descriptor.EnumDescriptor(
  name='DomainStrategy',
  full_name='Config.DomainStrategy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AsIs', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UseIp', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IpIfNonMatch', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IpOnDemand', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=715,
  serialized_end=786,
)
_sym_db.RegisterEnumDescriptor(_CONFIG_DOMAINSTRATEGY)


_NETWORKLIST = _descriptor.Descriptor(
  name='NetworkList',
  full_name='NetworkList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='NetworkList.network', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=17,
  serialized_end=57,
)


_PORTRANGE = _descriptor.Descriptor(
  name='PortRange',
  full_name='PortRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='From', full_name='PortRange.From', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='To', full_name='PortRange.To', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=59,
  serialized_end=96,
)


_DOMAIN = _descriptor.Descriptor(
  name='Domain',
  full_name='Domain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Domain.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Domain.value', index=1,
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
    _DOMAIN_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=191,
)


_CIDR = _descriptor.Descriptor(
  name='CIDR',
  full_name='CIDR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='CIDR.ip', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='CIDR.prefix', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=193,
  serialized_end=227,
)


_GEOIP = _descriptor.Descriptor(
  name='GeoIP',
  full_name='GeoIP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_code', full_name='GeoIP.country_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cidr', full_name='GeoIP.cidr', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=229,
  serialized_end=279,
)


_GEOIPLIST = _descriptor.Descriptor(
  name='GeoIPList',
  full_name='GeoIPList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='GeoIPList.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=281,
  serialized_end=315,
)


_GEOSITE = _descriptor.Descriptor(
  name='GeoSite',
  full_name='GeoSite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_code', full_name='GeoSite.country_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='GeoSite.domain', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=317,
  serialized_end=373,
)


_GEOSITELIST = _descriptor.Descriptor(
  name='GeoSiteList',
  full_name='GeoSiteList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='GeoSiteList.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=375,
  serialized_end=413,
)


_ROUTINGRULE = _descriptor.Descriptor(
  name='RoutingRule',
  full_name='RoutingRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='RoutingRule.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='RoutingRule.domain', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cidr', full_name='RoutingRule.cidr', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port_range', full_name='RoutingRule.port_range', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_list', full_name='RoutingRule.network_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_cidr', full_name='RoutingRule.source_cidr', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='RoutingRule.user_email', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbound_tag', full_name='RoutingRule.inbound_tag', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=416,
  serialized_end=625,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_strategy', full_name='Config.domain_strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='Config.rule', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIG_DOMAINSTRATEGY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=786,
)

_NETWORKLIST.fields_by_name['network'].enum_type = _NETWORK
_DOMAIN.fields_by_name['type'].enum_type = _DOMAIN_TYPE
_DOMAIN_TYPE.containing_type = _DOMAIN
_GEOIP.fields_by_name['cidr'].message_type = _CIDR
_GEOIPLIST.fields_by_name['entry'].message_type = _GEOIP
_GEOSITE.fields_by_name['domain'].message_type = _DOMAIN
_GEOSITELIST.fields_by_name['entry'].message_type = _GEOSITE
_ROUTINGRULE.fields_by_name['domain'].message_type = _DOMAIN
_ROUTINGRULE.fields_by_name['cidr'].message_type = _CIDR
_ROUTINGRULE.fields_by_name['port_range'].message_type = _PORTRANGE
_ROUTINGRULE.fields_by_name['network_list'].message_type = _NETWORKLIST
_ROUTINGRULE.fields_by_name['source_cidr'].message_type = _CIDR
_CONFIG.fields_by_name['domain_strategy'].enum_type = _CONFIG_DOMAINSTRATEGY
_CONFIG.fields_by_name['rule'].message_type = _ROUTINGRULE
_CONFIG_DOMAINSTRATEGY.containing_type = _CONFIG
DESCRIPTOR.message_types_by_name['NetworkList'] = _NETWORKLIST
DESCRIPTOR.message_types_by_name['PortRange'] = _PORTRANGE
DESCRIPTOR.message_types_by_name['Domain'] = _DOMAIN
DESCRIPTOR.message_types_by_name['CIDR'] = _CIDR
DESCRIPTOR.message_types_by_name['GeoIP'] = _GEOIP
DESCRIPTOR.message_types_by_name['GeoIPList'] = _GEOIPLIST
DESCRIPTOR.message_types_by_name['GeoSite'] = _GEOSITE
DESCRIPTOR.message_types_by_name['GeoSiteList'] = _GEOSITELIST
DESCRIPTOR.message_types_by_name['RoutingRule'] = _ROUTINGRULE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.enum_types_by_name['Network'] = _NETWORK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkList = _reflection.GeneratedProtocolMessageType('NetworkList', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKLIST,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:NetworkList)
  ))
_sym_db.RegisterMessage(NetworkList)

PortRange = _reflection.GeneratedProtocolMessageType('PortRange', (_message.Message,), dict(
  DESCRIPTOR = _PORTRANGE,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:PortRange)
  ))
_sym_db.RegisterMessage(PortRange)

Domain = _reflection.GeneratedProtocolMessageType('Domain', (_message.Message,), dict(
  DESCRIPTOR = _DOMAIN,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:Domain)
  ))
_sym_db.RegisterMessage(Domain)

CIDR = _reflection.GeneratedProtocolMessageType('CIDR', (_message.Message,), dict(
  DESCRIPTOR = _CIDR,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:CIDR)
  ))
_sym_db.RegisterMessage(CIDR)

GeoIP = _reflection.GeneratedProtocolMessageType('GeoIP', (_message.Message,), dict(
  DESCRIPTOR = _GEOIP,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:GeoIP)
  ))
_sym_db.RegisterMessage(GeoIP)

GeoIPList = _reflection.GeneratedProtocolMessageType('GeoIPList', (_message.Message,), dict(
  DESCRIPTOR = _GEOIPLIST,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:GeoIPList)
  ))
_sym_db.RegisterMessage(GeoIPList)

GeoSite = _reflection.GeneratedProtocolMessageType('GeoSite', (_message.Message,), dict(
  DESCRIPTOR = _GEOSITE,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:GeoSite)
  ))
_sym_db.RegisterMessage(GeoSite)

GeoSiteList = _reflection.GeneratedProtocolMessageType('GeoSiteList', (_message.Message,), dict(
  DESCRIPTOR = _GEOSITELIST,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:GeoSiteList)
  ))
_sym_db.RegisterMessage(GeoSiteList)

RoutingRule = _reflection.GeneratedProtocolMessageType('RoutingRule', (_message.Message,), dict(
  DESCRIPTOR = _ROUTINGRULE,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:RoutingRule)
  ))
_sym_db.RegisterMessage(RoutingRule)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'geoSite_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  ))
_sym_db.RegisterMessage(Config)


_NETWORK.values_by_name["RawTCP"].has_options = True
_NETWORK.values_by_name["RawTCP"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\010\001'))
# @@protoc_insertion_point(module_scope)
