#!/usr/bin/env bash
docker build \
    --tag hello-world-python \
    .

docker run \
    --name hello-world-python \
    --publish 8080:8080 \
    --rm \
    hello-world-python