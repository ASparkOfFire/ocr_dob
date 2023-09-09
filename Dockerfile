FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

RUN pip install -U pip

WORKDIR /tmp
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

EXPOSE 8000
WORKDIR /app
COPY ./ /app

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]
