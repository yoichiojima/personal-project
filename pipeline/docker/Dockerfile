FROM python:3

COPY ./opt/google_auth.json /opt/google_auth.json

COPY libs /app/libs
COPY setup.py /app/setup.py
RUN pip install --upgrade pip
RUN pip install -e /app

COPY pipeline/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app/pipeline

CMD luigid