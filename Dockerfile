FROM python:3.11.5-slim
##FROM python:latest

RUN pip install openai
##RUN pip install threading
RUN pip install werobot

WORKDIR /app
COPY chatgpt4.py .

CMD [ "python", "./chatgpt4.py"]