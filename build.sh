#!/bin/bash

docker build -t llamafactory:$1 -f Dockerfile .
docker tag llamafactory:$1 ccr.ccs.tencentyun.com/aigcode/llamafactory:$1 
docker tag llamafactory:$1  127.0.0.1:8001/aigcode/llamafactory:$1 
docker push ccr.ccs.tencentyun.com/aigcode/llamafactory:$1
docker push 127.0.0.1:8001/aigcode/llamafactory:$1 