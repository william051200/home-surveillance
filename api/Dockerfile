FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN python3 -m pip install --no-cache-dir -r ./requirements.txt

COPY ./startup.sh ./startup.sh

RUN chmod +x ./startup.sh

COPY ./src ./src

# CMD ["python3", "./src/main.py"]

CMD ["bash", "./startup.sh"]