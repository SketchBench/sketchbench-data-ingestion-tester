# SketchBench Data Ingestion Tester

> Based on [Aiven's Kafka Python Fake Data Producer](https://github.com/aiven/kafka-python-fake-data-producer).

The Data Ingestion Tester for SketchBench produces test data using the Python [`Faker`](https://github.com/joke2k/faker) library and ingests it into Kafka.
The generated message payload covers all supported data types in [Bullet's schema](https://bullet-db.github.io/backend/dsl/#schema).

## Usage

```plain
$ poetry run sketchbench-data-ingestion-tester --help
Usage: sketchbench-data-ingestion-tester [OPTIONS]

  Connect to Kafka and produce fake data for a topic.

Options:
  -s, --server TEXT               Kafka bootstrap servers that the producer
                                  should contact to.  [default:
                                  localhost:9092]
  -t, --topic TEXT                Kafka topic where the messages will be
                                  published.  [default: sketchbench-test]
  -n, --number-messages INTEGER   Number of messages to produce (0 for
                                  unlimited).  [default: 0]
  -w, --max-waiting-time FLOAT    Max waiting time in seconds between messages
                                  (0 for none).  [default: 0.1]
  -p, --security-protocol [PLAINTEXT|SSL|SASL_PLAINTEXT|SASL_SSL]
                                  Protocol used to communicate with brokers.
                                  [default: PLAINTEXT]
  --ssl-cafile PATH               Filename of ca file to use in certificate
                                  verification.
  --ssl-certfile PATH             Filename of file in pem format containing
                                  the client certificate.
  --ssl-keyfile PATH              Filename containing the client private key.
  --sasl-mechanism [PLAIN|GSSAPI|OAUTHBEARER|SCRAM-SHA-256|SCRAM-SHA-512]
                                  Authentication mechanism when
                                  security_protocol is configured.
  --sasl-plain-username TEXT      Username for sasl PLAIN and SCRAM
                                  authentication.
  --sasl-kerberos-service-name TEXT
                                  Service name to include in GSSAPI sasl
                                  mechanism handshake.  [default: kafka]
  --sasl-kerberos-domain-name TEXT
                                  Kerberos domain name to use in GSSAPI sasl
                                  mechanism handshake.
  --help                          Show this message and exit.
```

## Example

This repo also contains a [`docker-compose.yml`](https://github.com/SketchBench/sketchbench-data-ingestion-tester/blob/main/docker-compose.yml).
It builds the Docker image and starts the `sketchbench-data-ingestion-tester` together with:

- `kafka` ([`docker.io/bitnami/kafka`](https://hub.docker.com/r/bitnami/kafka))
- `zookeeper` for Kafka ([`docker.io/bitnami/zookeeper`](https://hub.docker.com/r/bitnami/zookeeper))
- `kafdrop` for Kafka monitoring/debugging ([`obsidiandynamics/kafdrop`](https://hub.docker.com/r/obsidiandynamics/kafdrop))

### Start All Containers

```plain
docker-compose up
```

Optionally, append `--detach` to run containers in the background.

_The `sketchbench-data-ingestion-tester` container might restart until the infrastructure containers (Kafka & Zookeeper) are fully running._

### Stop All Containers

```plain
docker-compose down
```

Optionally, include cleanup parameters `--rmi all --volumes --remove-orphans`.

## Example Message Payload

```json
{
   "SketchBenchMessageID": 8,
   "SketchBenchBoolean": true,
   "SketchBenchInteger": 3583,
   "SketchBenchLong": 9223372036854776000,
   "SketchBenchFloat": 0.4968928,
   "SketchBenchDouble": -0.116756782941063,
   "SketchBenchString": "mesh granular bandwidth",
   "SketchBenchBooleanMap": {
      "SketchBenchBooleanOne": true,
      "SketchBenchBooleanTwo": false
   },
   "SketchBenchIntegerMap": {
      "SketchBenchIntegerOne": 7361,
      "SketchBenchIntegerTwo": 3750
   },
   "SketchBenchLongMap": {
      "SketchBenchLongOne": 9223372036854776000,
      "SketchBenchLongTwo": 9223372036854776000
   },
   "SketchBenchFloatMap": {
      "SketchBenchFloatOne": 0.6091936,
      "SketchBenchFloatTwo": -0.9311707
   },
   "SketchBenchDoubleMap": {
      "SketchBenchDoubleOne": -0.149212534103102,
      "SketchBenchDoubleTwo": 0.986187516992927
   },
   "SketchBenchStringMap": {
      "SketchBenchStringOne": "drive world-class architectures",
      "SketchBenchStringTwo": "Optimized even-keeled open architecture"
   },
   "SketchBenchBooleanMapMap": {
      "SketchBenchBooleanMapOne": {
         "SketchBenchBooleanOne": false,
         "SketchBenchBooleanTwo": true
      },
      "SketchBenchBooleanMapTwo": {
         "SketchBenchBooleanOne": false,
         "SketchBenchBooleanTwo": true
      }
   },
   "SketchBenchIntegerMapMap": {
      "SketchBenchIntegerMapOne": {
         "SketchBenchIntegerOne": 8494,
         "SketchBenchIntegerTwo": 5350
      },
      "SketchBenchIntegerMapTwo": {
         "SketchBenchIntegerOne": 5889,
         "SketchBenchIntegerTwo": 3983
      }
   },
   "SketchBenchLongMapMap": {
      "SketchBenchLongMapOne": {
         "SketchBenchLongOne": 9223372036854776000,
         "SketchBenchLongTwo": 9223372036854776000
      },
      "SketchBenchLongMapTwo": {
         "SketchBenchLongOne": 9223372036854776000,
         "SketchBenchLongTwo": 9223372036854776000
      }
   },
   "SketchBenchFloatMapMap": {
      "SketchBenchFloatMapOne": {
         "SketchBenchFloatOne": -0.4420025,
         "SketchBenchFloatTwo": 0.438981
      },
      "SketchBenchFloatMapTwo": {
         "SketchBenchFloatOne": -0.4475535,
         "SketchBenchFloatTwo": -0.9763844
      }
   },
   "SketchBenchDoubleMapMap": {
      "SketchBenchDoubleMapOne": {
         "SketchBenchDoubleOne": -0.495523881349819,
         "SketchBenchDoubleTwo": 0.190281932097149
      },
      "SketchBenchDoubleMapTwo": {
         "SketchBenchDoubleOne": 0.786427699364296,
         "SketchBenchDoubleTwo": -0.558253388273458
      }
   },
   "SketchBenchStringMapMap": {
      "SketchBenchStringMapOne": {
         "SketchBenchStringOne": "target customized schemas",
         "SketchBenchStringTwo": "Ameliorated clear-thinking focus group"
      },
      "SketchBenchStringMapTwo": {
         "SketchBenchStringOne": "incubate web-enabled action-items",
         "SketchBenchStringTwo": "Pre-emptive responsive neural-net"
      }
   },
   "SketchBenchBooleanList": [
      false,
      true
   ],
   "SketchBenchIntegerList": [
      6181,
      354
   ],
   "SketchBenchLongList": [
      9223372036854776000,
      9223372036854776000
   ],
   "SketchBenchFloatList": [
      -0.1424044,
      0.9347839
   ],
   "SketchBenchDoubleList": [
      -0.326835817910416,
      -0.533978554495603
   ],
   "SketchBenchStringList": [
      "envisioneer collaborative users",
      "Ergonomic national superstructure"
   ],
   "SketchBenchBooleanMapList": [
      {
         "SketchBenchBooleanOne": true,
         "SketchBenchBooleanTwo": false
      },
      {
         "SketchBenchBooleanOne": false,
         "SketchBenchBooleanTwo": false
      }
   ],
   "SketchBenchIntegerMapList": [
      {
         "SketchBenchIntegerOne": 1385,
         "SketchBenchIntegerTwo": 8705
      },
      {
         "SketchBenchIntegerOne": 1292,
         "SketchBenchIntegerTwo": 3537
      }
   ],
   "SketchBenchLongMapList": [
      {
         "SketchBenchLongOne": 9223372036854776000,
         "SketchBenchLongTwo": 9223372036854776000
      },
      {
         "SketchBenchLongOne": 9223372036854776000,
         "SketchBenchLongTwo": 9223372036854776000
      }
   ],
   "SketchBenchFloatMapList": [
      {
         "SketchBenchFloatOne": -0.787982,
         "SketchBenchFloatTwo": -0.9212975
      },
      {
         "SketchBenchFloatOne": -0.1016218,
         "SketchBenchFloatTwo": -0.9815003
      }
   ],
   "SketchBenchDoubleMapList": [
      {
         "SketchBenchDoubleOne": 0.83640428357851,
         "SketchBenchDoubleTwo": 0.99176170162883
      },
      {
         "SketchBenchDoubleOne": 0.45293697921741,
         "SketchBenchDoubleTwo": 0.629348839198145
      }
   ],
   "SketchBenchStringMapList": [
      {
         "SketchBenchStringOne": "incubate 24/7 interfaces",
         "SketchBenchStringTwo": "Customizable 4thgeneration database"
      },
      {
         "SketchBenchStringOne": "embrace rich experiences",
         "SketchBenchStringTwo": "Triple-buffered asymmetric workforce"
      }
   ]
}
```
