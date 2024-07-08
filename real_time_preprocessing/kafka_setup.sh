#!/bin/bash

# Download Kafka
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.13-2.8.0.tgz

# Extract Kafka
tar -xzf kafka_2.13-2.8.0.tgz
cd kafka_2.13-2.8.0

# Start Zookeeper (required for Kafka)
bin/zookeeper-server-start.sh config/zookeeper.properties &

# Start Kafka broker
bin/kafka-server-start.sh config/server.properties &
