FROM jupyter/datascience-notebook
RUN set -ex && pip install --upgrade pip
COPY requirements.txt requirements.txt
COPY scripts /app/scripts
RUN set -ex && pip install -r requirements.txt
ENV PYTHONPATH=/usr/local/bin:/app
ENV PYTHON_VERSION=3.6.4
WORKDIR /app
