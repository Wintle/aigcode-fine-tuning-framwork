#!/bin/bash
set -e
/bin/bash -c 'export GRADIO_SERVER_NAME=0.0.0.0 && export GRADIO_SERVER_PORT=7860 && llamafactory-cli webui'

