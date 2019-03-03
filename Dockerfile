FROM python:3.6.6

RUN set -ex && pip install pip pipenv --upgrade

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN set -ex && pipenv install --system --deploy --dev
ENV PYTHONPATH=/usr/local/bin:/app

WORKDIR /app
