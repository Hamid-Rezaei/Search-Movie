FROM python:3.9.19-alpine

LABEL authors="hamid"

WORKDIR /code

ENV PYTHONPATH "${PYTHONPATH}:/your/custom/path"

RUN pip install --upgrade pip

RUN pip install numpy

COPY . /code

ENTRYPOINT ["python", "cc_hw2_hello.py" ]