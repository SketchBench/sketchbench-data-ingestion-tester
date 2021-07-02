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

This repo also contains a [`docker-compose.yaml`](https://github.com/SketchBench/sketchbench-data-ingestion-tester/blob/main/docker-compose.yaml).
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
   "SketchBenchMessageID": 31,
   "SketchBenchBoolean": true,
   "SketchBenchInteger": 141,
   "SketchBenchLong": 9223372036854776000,
   "SketchBenchFloat": -0.8539659,
   "SketchBenchDouble": -0.529517953770302,
   "SketchBenchString": "extend magnetic e-markets",
   "SketchBenchBooleanMap": {
      "SketchBenchBooleanOne": false,
      "SketchBenchBooleanTwo": true
   },
   "SketchBenchIntegerMap": {
      "SketchBenchIntegerOne": 1501,
      "SketchBenchIntegerTwo": 9221
   },
   "SketchBenchLongMap": {
      "SketchBenchLongOne": 9223372036854776000,
      "SketchBenchLongTwo": 9223372036854776000
   },
   "SketchBenchFloatMap": {
      "SketchBenchFloatOne": -0.4021153,
      "SketchBenchFloatTwo": 0.9187859
   },
   "SketchBenchDoubleMap": {
      "SketchBenchDoubleOne": 0.315264548785299,
      "SketchBenchDoubleTwo": -0.762407252391137
   },
   "SketchBenchStringMap": {
      "SketchBenchStringOne": "e-enable enterprise models",
      "SketchBenchStringTwo": "Public-key impactful help-desk"
   },
   "SketchBenchBooleanMapMap": {
      "SketchBenchBooleanMapOne": {
         "SketchBenchBooleanOne": true,
         "SketchBenchBooleanTwo": true
      },
      "SketchBenchBooleanMapTwo": {
         "SketchBenchBooleanOne": false,
         "SketchBenchBooleanTwo": true
      }
   },
   "SketchBenchIntegerMapMap": {
      "SketchBenchIntegerMapOne": {
         "SketchBenchIntegerOne": 1633,
         "SketchBenchIntegerTwo": 3074
      },
      "SketchBenchIntegerMapTwo": {
         "SketchBenchIntegerOne": 9616,
         "SketchBenchIntegerTwo": 8785
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
         "SketchBenchFloatOne": -0.2370886,
         "SketchBenchFloatTwo": 0.88226
      },
      "SketchBenchFloatMapTwo": {
         "SketchBenchFloatOne": -0.533147,
         "SketchBenchFloatTwo": -0.7366217
      }
   },
   "SketchBenchDoubleMapMap": {
      "SketchBenchDoubleMapOne": {
         "SketchBenchDoubleOne": 0.650313884339732,
         "SketchBenchDoubleTwo": 0.949253289610448
      },
      "SketchBenchDoubleMapTwo": {
         "SketchBenchDoubleOne": -0.15282554628291,
         "SketchBenchDoubleTwo": -0.970043616249494
      }
   },
   "SketchBenchStringMapMap": {
      "SketchBenchStringMapOne": {
         "SketchBenchStringOne": "streamline cross-platform niches",
         "SketchBenchStringTwo": "Implemented attitude-oriented strategy"
      },
      "SketchBenchStringMapTwo": {
         "SketchBenchStringOne": "re-contextualize killer paradigms",
         "SketchBenchStringTwo": "Realigned secondary function"
      }
   },
   "SketchBenchBooleanList": [
      false,
      true
   ],
   "SketchBenchIntegerList": [
      7671,
      318
   ],
   "SketchBenchLongList": [
      9223372036854776000,
      9223372036854776000
   ],
   "SketchBenchFloatList": [
      0.3468411,
      -0.274181
   ],
   "SketchBenchDoubleList": [
      -0.593023836607392,
      0.10903266469462
   ],
   "SketchBenchStringList": [
      "enable one-to-one interfaces",
      "Function-based dynamic help-desk"
   ],
   "SketchBenchBooleanMapList": {
      "SketchBenchBooleanListOne": [
         false,
         true
      ],
      "SketchBenchBooleanListTwo": [
         true,
         false
      ]
   },
   "SketchBenchIntegerMapList": {
      "SketchBenchIntegerListOne": [
         6142,
         9188
      ],
      "SketchBenchIntegerListTwo": [
         569,
         4465
      ]
   },
   "SketchBenchLongMapList": {
      "SketchBenchLongListOne": [
         9223372036854776000,
         9223372036854776000
      ],
      "SketchBenchLongListTwo": [
         9223372036854776000,
         9223372036854776000
      ]
   },
   "SketchBenchFloatMapList": {
      "SketchBenchFloatListOne": [
         -0.6408545,
         0.9645153
      ],
      "SketchBenchFloatListTwo": [
         0.7020063,
         -0.6172132
      ]
   },
   "SketchBenchDoubleMapList": {
      "SketchBenchDoubleListOne": [
         0.586855576316007,
         0.611186873781055
      ],
      "SketchBenchDoubleListTwo": [
         -0.243311157263657,
         -0.40322259324684
      ]
   },
   "SketchBenchStringMapList": {
      "SketchBenchStringListOne": [
         "generate web-enabled schemas",
         "Robust dynamic extranet"
      ],
      "SketchBenchStringListTwo": [
         "incubate dot-com e-markets",
         "Intuitive solution-oriented core"
      ]
   }
}
```
