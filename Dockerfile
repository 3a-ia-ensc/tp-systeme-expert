FROM python:3.7-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY src /app/src
COPY www /app/www
COPY app.py /app/app.py

EXPOSE 5000
WORKDIR /app/
CMD ["flask", "run", "--host=0.0.0.0"]
