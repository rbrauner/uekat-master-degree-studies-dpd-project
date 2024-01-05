FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py
COPY ./src /code/src

ENV APP_ENV=prod
ENV APP_HOST=0.0.0.0
ENV APP_PORT=8000

CMD python main.py
