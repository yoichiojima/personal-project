FROM python:3

COPY ./notebook/requirements.txt /app/notebook/requirements.txt
RUN pip install -r /app/notebook/requirements.txt

WORKDIR /app

CMD jupyter lab --ip="0.0.0.0" \
                --port=8888 \
                --LabApp.token="" \
                --allow-root