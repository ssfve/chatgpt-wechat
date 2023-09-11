FROM python:3.11.5-slim
##FROM python:latest

ENV PYTHONUNBUFFERED True

RUN pip install openai
##RUN pip install threading
RUN pip install werobot
RUN pip install gunicorn

WORKDIR /app
COPY chatgpt4.py .

EXPOSE 8080
##EXPOST $PORT
CMD [ "python", "./chatgpt4.py"]