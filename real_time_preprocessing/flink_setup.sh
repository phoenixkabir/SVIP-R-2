#!/bin/bash

# Download Flink
wget https://archive.apache.org/dist/flink/flink-1.12.0/flink-1.12.0-bin-scala_2.11.tgz

# Extract Flink
tar -xzf flink-1.12.0-bin-scala_2.11.tgz
cd flink-1.12.0

# Start Flink
bin/start-cluster.sh
