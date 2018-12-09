FROM arm32v7/python:3.7.1-slim

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /code
COPY . /code

CMD ["gunicorn", "run:app"]