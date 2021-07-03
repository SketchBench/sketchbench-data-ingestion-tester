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
   "SketchBenchBoolean": false,
   "SketchBenchInteger": 4680,
   "SketchBenchLong": 17381163767201438000,
   "SketchBenchFloat": -0.6736831,
   "SketchBenchDouble": -0.71966375026374,
   "SketchBenchString": "incentivize 24/7 ROI",
   "SketchBenchBooleanMap": {
      "SketchBenchBooleanOne": true,
      "SketchBenchBooleanTwo": false
   },
   "SketchBenchIntegerMap": {
      "SketchBenchIntegerOne": 959,
      "SketchBenchIntegerTwo": 3871
   },
   "SketchBenchLongMap": {
      "SketchBenchLongOne": 12405357220187828000,
      "SketchBenchLongTwo": 16599164916512221000
   },
   "SketchBenchFloatMap": {
      "SketchBenchFloatOne": -0.6615189,
      "SketchBenchFloatTwo": 0.4545328
   },
   "SketchBenchDoubleMap": {
      "SketchBenchDoubleOne": 0.595727791717468,
      "SketchBenchDoubleTwo": -0.470706766232865
   },
   "SketchBenchStringMap": {
      "SketchBenchStringOne": "evolve seamless convergence",
      "SketchBenchStringTwo": "Sharable client-server Graphic Interface"
   },
   "SketchBenchBooleanMapMap": {
      "SketchBenchBooleanMapOne": {
         "SketchBenchBooleanOne": true,
         "SketchBenchBooleanTwo": true
      },
      "SketchBenchBooleanMapTwo": {
         "SketchBenchBooleanOne": true,
         "SketchBenchBooleanTwo": true
      }
   },
   "SketchBenchIntegerMapMap": {
      "SketchBenchIntegerMapOne": {
         "SketchBenchIntegerOne": 3002,
         "SketchBenchIntegerTwo": 2474
      },
      "SketchBenchIntegerMapTwo": {
         "SketchBenchIntegerOne": 7719,
         "SketchBenchIntegerTwo": 124
      }
   },
   "SketchBenchLongMapMap": {
      "SketchBenchLongMapOne": {
         "SketchBenchLongOne": 9753260017885856000,
         "SketchBenchLongTwo": 16734300098606176000
      },
      "SketchBenchLongMapTwo": {
         "SketchBenchLongOne": 13311185963017191000,
         "SketchBenchLongTwo": 13012292389728508000
      }
   },
   "SketchBenchFloatMapMap": {
      "SketchBenchFloatMapOne": {
         "SketchBenchFloatOne": 0.3517626,
         "SketchBenchFloatTwo": -0.5237855
      },
      "SketchBenchFloatMapTwo": {
         "SketchBenchFloatOne": 0.1630309,
         "SketchBenchFloatTwo": 0.4890072
      }
   },
   "SketchBenchDoubleMapMap": {
      "SketchBenchDoubleMapOne": {
         "SketchBenchDoubleOne": -0.52442321009014,
         "SketchBenchDoubleTwo": -0.368535996960704
      },
      "SketchBenchDoubleMapTwo": {
         "SketchBenchDoubleOne": -0.314387669891155,
         "SketchBenchDoubleTwo": -0.66959359075869
      }
   },
   "SketchBenchStringMapMap": {
      "SketchBenchStringMapOne": {
         "SketchBenchStringOne": "generate B2C action-items",
         "SketchBenchStringTwo": "Grass-roots hybrid migration"
      },
      "SketchBenchStringMapTwo": {
         "SketchBenchStringOne": "synthesize one-to-one eyeballs",
         "SketchBenchStringTwo": "Proactive didactic middleware"
      }
   },
   "SketchBenchBooleanList": [
      false,
      true
   ],
   "SketchBenchIntegerList": [
      4673,
      8126
   ],
   "SketchBenchLongList": [
      17795363561565530000,
      17010220832115091000
   ],
   "SketchBenchFloatList": [
      -0.133418,
      0.6225013
   ],
   "SketchBenchDoubleList": [
      0.729906939516728,
      -0.331646744564121
   ],
   "SketchBenchStringList": [
      "leverage synergistic networks",
      "Function-based 4thgeneration instruction set"
   ],
   "SketchBenchBooleanMapList": {
      "SketchBenchBooleanListOne": [
         true,
         true
      ],
      "SketchBenchBooleanListTwo": [
         false,
         true
      ]
   },
   "SketchBenchIntegerMapList": {
      "SketchBenchIntegerListOne": [
         3652,
         1258
      ],
      "SketchBenchIntegerListTwo": [
         2341,
         1204
      ]
   },
   "SketchBenchLongMapList": {
      "SketchBenchLongListOne": [
         10821444901808830000,
         16680769582394352000
      ],
      "SketchBenchLongListTwo": [
         12451900065695437000,
         14809527274602793000
      ]
   },
   "SketchBenchFloatMapList": {
      "SketchBenchFloatListOne": [
         -0.7972251,
         -0.535875
      ],
      "SketchBenchFloatListTwo": [
         -0.3798413,
         0.8174764
      ]
   },
   "SketchBenchDoubleMapList": {
      "SketchBenchDoubleListOne": [
         0.851025432527654,
         0.426357379131281
      ],
      "SketchBenchDoubleListTwo": [
         0.998496492495993,
         0.843068760260131
      ]
   },
   "SketchBenchStringMapList": {
      "SketchBenchStringListOne": [
         "generate plug-and-play ROI",
         "Total secondary core"
      ],
      "SketchBenchStringListTwo": [
         "enhance scalable convergence",
         "Re-engineered systematic methodology"
      ]
   }
}
```
