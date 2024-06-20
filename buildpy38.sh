#!/bin/bash

docker build -t llamafactory-py38:$1 -f DockerfilePy38 .
docker tag llamafactory-py38:$1 ccr.ccs.tencentyun.com/aigcode/llamafactory-py38:$1 
docker tag llamafactory-py38:$1  127.0.0.1:8001/aigcode/llamafactory-py38:$1 
docker push ccr.ccs.tencentyun.com/aigcode/llamafactory-py38:$1
docker push 127.0.0.1:8001/aigcode/llamafactory-py38:$1 