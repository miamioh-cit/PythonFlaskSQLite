FROM python:3.9-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3 \
    build-essential\
    nfs-common

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["flask", "--app", "hello_app.webapp", "--debug", "run"]



