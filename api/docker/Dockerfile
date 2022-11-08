FROM python:3

COPY ./api/requirements.txt /app/api/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/api/requirements.txt

EXPOSE 8000

WORKDIR /app/api

CMD uvicorn main:app --reload \
                     --host=0.0.0.0 \
                     --port=8000