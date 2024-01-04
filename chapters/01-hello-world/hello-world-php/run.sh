#!/usr/bin/env bash
docker build \
    --tag hello-world-php \
    .

docker run \
    --name hello-world-php \
    --publish 8080:80 \
    --rm \
    hello-world-php