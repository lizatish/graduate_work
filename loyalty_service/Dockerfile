FROM python:3.10

WORKDIR /opt

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . /opt/app/

ENV PYTHONPATH "${PYTHONPATH}:/opt/app/src/"

EXPOSE 6666
ENTRYPOINT gunicorn app.src.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:6666 --timeout 90