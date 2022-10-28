FROM python:3

COPY ./notebook/requirements.txt /app/notebook/requirements.txt
RUN pip install -r /app/notebook/requirements.txt

COPY ./libs /app/libs
COPY ./setup.py /app/setup.py
RUN pip install -e /app

WORKDIR /app

CMD jupyter lab --ip="0.0.0.0" \
                --port=8888 \
                --LabApp.token="" \
                --allow-root