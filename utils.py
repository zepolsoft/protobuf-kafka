import logging

from channels_integrations import new_order_pb2
from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer
from confluent_kafka.serialization import MessageField, SerializationContext
from google.protobuf.json_format import MessageToDict

logger = logging.getLogger(__name__)


deserialize = ProtobufDeserializer(new_order_pb2.NewOrder(), conf={"use.deprecated.format": True})


def decode_message_from_protobuf(value, topic):
    ctx = SerializationContext(topic, MessageField.VALUE)
    msg = deserialize(value=value, ctx=ctx)
    dict_msg = MessageToDict(msg, preserving_proto_field_name=True)
    return dict_msg


def decode_message(message):
    return decode_message_from_protobuf(message.value, message.topic)
