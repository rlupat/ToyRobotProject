FROM python:3.8.2
LABEL maintainer="Richard Lupat"

WORKDIR /toyrobot
COPY . .

# Install latest packages
RUN pip3 install -r requirements.txt
RUN pip3 install .

ENTRYPOINT ["toyrobot"]