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
- 
### Start All Containers

```plain
docker-compose up
```

Optionally, append `--detach` to run containers in the background.

_The `sketchbench-data-ingestion-tester` container might restart until the infrastructure containers (Kafka & Zookeeper) are fully running._

## Stop All Containers

```plain
docker-compose down
```

Optionally, include cleanup parameters `--rmi all --volumes --remove-orphans`.
