FROM python:3

COPY ./backend/requirements.txt /app/backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt

COPY ./libs /app/libs
COPY setup.py /app/setup.py
RUN pip install -e /app

COPY ./opt/google_auth.json /opt/google_auth.json

EXPOSE 8000

WORKDIR /app/backend

CMD uvicorn main:app --reload \
                     --host=0.0.0.0 \
                     --port=8000