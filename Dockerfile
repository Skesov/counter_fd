FROM python:3.9.2

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "server.py"]
