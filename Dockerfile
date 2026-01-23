FROM python:3.9.1-slim-buster

WORKDIR /app

ADD ..

RUN pip install -r requirements.txt

CMD ["python", "app.py"]