"""Data ingestion test for SketchBench for all support Bullet schema types."""

import itertools
import os
import random
import time
from pathlib import Path
from typing import Any, Dict, Sequence, Tuple

import click
import click_pathlib
import orjson
from faker import Faker  # type: ignore
from kafka import KafkaProducer  # type: ignore
from loguru import logger

fake = Faker()


def _long() -> int:
    min_exponent: int = 63
    max_exponent: int = 63
    return fake.random_int(min=2**min_exponent, max=2**max_exponent)


def _float() -> float:
    digits: int = 7
    return fake.pyfloat(left_digits=0, right_digits=digits)


def _double() -> float:
    digits: int = 15
    return fake.pyfloat(left_digits=0, right_digits=digits)


def create_message(message_id: int) -> Tuple[str, Dict[str, Any]]:
    """Create a message for Kafka testing all supported types in Bullet.

    The message payload contains fake data using the Faker library. The payload
    covers all supported schema types in Bullet. More info:
    https://bullet-db.github.io/backend/dsl/#schema

    A random country name is used as key to allow partitioning in Kafka.

    Args:
        message_id: An integer to be added as ID in the message payload.

    Returns:
        A tuple consisting of the message key and message payload.
    """
    return fake.country(), {
        'SketchBenchMessageID': message_id,
        'SketchBenchBoolean': fake.boolean(),
        'SketchBenchInteger': fake.random_int(),
        'SketchBenchLong': _long(),
        'SketchBenchFloat': _float(),
        'SketchBenchDouble': _double(),
        'SketchBenchString': fake.bs(),
        'SketchBenchBooleanMap': {
            'SketchBenchBooleanOne': fake.boolean(),
            'SketchBenchBooleanTwo': fake.boolean(),
        },
        'SketchBenchIntegerMap': {
            'SketchBenchIntegerOne': fake.random_int(),
            'SketchBenchIntegerTwo': fake.random_int(),
        },
        'SketchBenchLongMap': {
            'SketchBenchLongOne': _long(),
            'SketchBenchLongTwo': _long(),
        },
        'SketchBenchFloatMap': {
            'SketchBenchFloatOne': _float(),
            'SketchBenchFloatTwo': _float(),
        },
        'SketchBenchDoubleMap': {
            'SketchBenchDoubleOne': _double(),
            'SketchBenchDoubleTwo': _double(),
        },
        'SketchBenchStringMap': {
            'SketchBenchStringOne': fake.bs(),
            'SketchBenchStringTwo': fake.catch_phrase(),
        },
        'SketchBenchBooleanMapMap': {
            'SketchBenchBooleanMapOne': {
                'SketchBenchBooleanOne': fake.boolean(),
                'SketchBenchBooleanTwo': fake.boolean(),
            },
            'SketchBenchBooleanMapTwo': {
                'SketchBenchBooleanOne': fake.boolean(),
                'SketchBenchBooleanTwo': fake.boolean(),
            },
        },
        'SketchBenchIntegerMapMap': {
            'SketchBenchIntegerMapOne': {
                'SketchBenchIntegerOne': fake.random_int(),
                'SketchBenchIntegerTwo': fake.random_int(),
            },
            'SketchBenchIntegerMapTwo': {
                'SketchBenchIntegerOne': fake.random_int(),
                'SketchBenchIntegerTwo': fake.random_int(),
            },
        },
        'SketchBenchLongMapMap': {
            'SketchBenchLongMapOne': {
                'SketchBenchLongOne': _long(),
                'SketchBenchLongTwo': _long(),
            },
            'SketchBenchLongMapTwo': {
                'SketchBenchLongOne': _long(),
                'SketchBenchLongTwo': _long(),
            },
        },
        'SketchBenchFloatMapMap': {
            'SketchBenchFloatMapOne': {
                'SketchBenchFloatOne': _float(),
                'SketchBenchFloatTwo': _float(),
            },
            'SketchBenchFloatMapTwo': {
                'SketchBenchFloatOne': _float(),
                'SketchBenchFloatTwo': _float(),
            },
        },
        'SketchBenchDoubleMapMap': {
            'SketchBenchDoubleMapOne': {
                'SketchBenchDoubleOne': _double(),
                'SketchBenchDoubleTwo': _double(),
            },
            'SketchBenchDoubleMapTwo': {
                'SketchBenchDoubleOne': _double(),
                'SketchBenchDoubleTwo': _double(),
            },
        },
        'SketchBenchStringMapMap': {
            'SketchBenchStringMapOne': {
                'SketchBenchStringOne': fake.bs(),
                'SketchBenchStringTwo': fake.catch_phrase(),
            },
            'SketchBenchStringMapTwo': {
                'SketchBenchStringOne': fake.bs(),
                'SketchBenchStringTwo': fake.catch_phrase(),
            },
        },
        'SketchBenchBooleanList': [fake.boolean(), fake.boolean()],
        'SketchBenchIntegerList': [fake.random_int(), fake.random_int()],
        'SketchBenchLongList': [_long(), _long()],
        'SketchBenchFloatList': [_float(), _float()],
        'SketchBenchDoubleList': [_double(), _double()],
        'SketchBenchStringList': [fake.bs(), fake.catch_phrase()],
        'SketchBenchBooleanMapList': {
            'SketchBenchBooleanListOne': [fake.boolean(), fake.boolean()],
            'SketchBenchBooleanListTwo': [fake.boolean(), fake.boolean()],
        },
        'SketchBenchIntegerMapList': {
            'SketchBenchIntegerListOne': [
                fake.random_int(),
                fake.random_int(),
            ],
            'SketchBenchIntegerListTwo': [
                fake.random_int(),
                fake.random_int(),
            ],
        },
        'SketchBenchLongMapList': {
            'SketchBenchLongListOne': [_long(), _long()],
            'SketchBenchLongListTwo': [_long(), _long()],
        },
        'SketchBenchFloatMapList': {
            'SketchBenchFloatListOne': [_float(), _float()],
            'SketchBenchFloatListTwo': [_float(), _float()],
        },
        'SketchBenchDoubleMapList': {
            'SketchBenchDoubleListOne': [_double(), _double()],
            'SketchBenchDoubleListTwo': [_double(), _double()],
        },
        'SketchBenchStringMapList': {
            'SketchBenchStringListOne': [fake.bs(), fake.catch_phrase()],
            'SketchBenchStringListTwo': [fake.bs(), fake.catch_phrase()],
        },
    }


@click.command()
@click.option(
    '-s',
    '--server',
    'bootstrap_servers',
    type=click.STRING,
    multiple=True,
    help='Kafka bootstrap servers that the producer should contact to.',
    default=['localhost:9092'],
    show_default=True,
)
@click.option(
    '-t',
    '--topic',
    'topic',
    type=click.STRING,
    help='Kafka topic where the messages will be published.',
    default='sketchbench-test',
    show_default=True,
)
@click.option(
    '-n',
    '--number-messages',
    'number_messages',
    type=click.INT,
    help='Number of messages to produce (0 for unlimited).',
    default=0,
    show_default=True,
)
@click.option(
    '-w',
    '--max-waiting-time',
    'max_waiting_time',
    type=click.FLOAT,
    help='Max waiting time in seconds between messages (0 for none).',
    default=0.1,
    show_default=True,
)
@click.option(
    '-p',
    '--security-protocol',
    'security_protocol',
    type=click.Choice(
        ['PLAINTEXT', 'SSL', 'SASL_PLAINTEXT', 'SASL_SSL'],
        case_sensitive=False,
    ),
    help='Protocol used to communicate with brokers.',
    default='PLAINTEXT',
    show_default=True,
)
@click.option(
    '--ssl-cafile',
    'ssl_cafile',
    type=click_pathlib.Path(exists=True),
    help='Filename of ca file to use in certificate verification.',
)
@click.option(
    '--ssl-certfile',
    'ssl_certfile',
    type=click_pathlib.Path(exists=True),
    help='Filename of file in pem format containing the client certificate.',
)
@click.option(
    '--ssl-keyfile',
    'ssl_keyfile',
    type=click_pathlib.Path(exists=True),
    help='Filename containing the client private key.',
)
@click.option(
    '--sasl-mechanism',
    'sasl_mechanism',
    type=click.Choice(
        ['PLAIN', 'GSSAPI', 'OAUTHBEARER', 'SCRAM-SHA-256', 'SCRAM-SHA-512'],
        case_sensitive=False,
    ),
    help='Authentication mechanism when security_protocol is configured.',
)
@click.option(
    '--sasl-plain-username',
    'sasl_plain_username',
    type=click.STRING,
    help='Username for sasl PLAIN and SCRAM authentication.',
)
@click.option(
    '--sasl-kerberos-service-name',
    'sasl_kerberos_service_name',
    type=click.STRING,
    help='Service name to include in GSSAPI sasl mechanism handshake.',
    default='kafka',
    show_default=True,
)
@click.option(
    '--sasl-kerberos-domain-name',
    'sasl_kerberos_domain_name',
    type=click.STRING,
    help='Kerberos domain name to use in GSSAPI sasl mechanism handshake.',
)
def cli(  # noqa: WPS211,WPS216
    bootstrap_servers: Sequence[str],
    topic: str,
    number_messages: float,
    max_waiting_time: float,
    security_protocol: str,
    ssl_cafile: Path,
    ssl_certfile: Path,
    ssl_keyfile: Path,
    sasl_mechanism: str,
    sasl_plain_username: str,
    sasl_kerberos_service_name: str,
    sasl_kerberos_domain_name: str,
) -> None:
    """Connect to Kafka and produce fake data for a topic."""
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        security_protocol=security_protocol,
        ssl_cafile=str(ssl_cafile),
        ssl_certfile=str(ssl_certfile),
        ssl_keyfile=str(ssl_keyfile),
        ssl_password=os.getenv('SSL_PASSWORD'),
        sasl_mechanism=sasl_mechanism,
        sasl_plain_username=sasl_plain_username,
        sasl_plain_password=os.getenv('SASL_PASSWORD'),
        sasl_kerberos_service_name=sasl_kerberos_service_name,
        sasl_kerberos_domain_name=sasl_kerberos_domain_name,
        value_serializer=lambda payload: orjson.dumps(payload),
        key_serializer=lambda msg_key: msg_key.encode(),
    )
    for message_id in itertools.count():
        if number_messages > 0 and message_id == number_messages:
            break
        key, message = create_message(message_id)
        logger.info('Sending: {0}', message)
        producer.send(
            topic=topic,
            key=key,
            value=message,
        )
        sleep_time = random.uniform(0, max_waiting_time * 10) / 10
        logger.info('Sleeping for {0}s', sleep_time)
        time.sleep(sleep_time)
        # Force flushing of all messages
        if (message_id % 10) == 0:
            producer.flush()
    producer.flush()


if __name__ == '__main__':
    cli()
