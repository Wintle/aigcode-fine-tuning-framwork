FROM aigcode/ubuntu22.04-arm64-python310-pytorch220:v1.0.0

USER root

WORKDIR /app

ENV LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/python3.10.11/lib:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/lib64/:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib/

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
RUN pip install -e .[deepspeed,metrics,bitsandbytes,qwen]
RUN pip install git+https://github.com/Wintle/aim.git


VOLUME [ "/root/.cache/huggingface/", "/app/data", "/app/output" ]

# Expose port 7860 for the LLaMA Board
EXPOSE 7860

CMD [ "./run.sh" ]
