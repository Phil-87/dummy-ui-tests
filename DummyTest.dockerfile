FROM python:3.7-alpine3.10

WORKDIR /dummy-ui-tests

RUN apk update && apk add "chromium" \
    "chromium-chromedriver" \
    "git"

VOLUME ["/dev/shm"]

COPY requirements.txt ./
RUN pip install -r /dummy-ui-tests/requirements.txt

COPY . ./

ARG PATH_TO_TESTS=./features
ARG BASE_URL=""
ARG TAGS="" 

ENTRYPOINT [ "/bin/sh", "-c", "behave $PATH_TO_TESTS $TAGS $BASE_URL" ]