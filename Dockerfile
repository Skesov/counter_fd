FROM python:3.9.2

# RUN apt-get update -y

# RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "server.py"]
