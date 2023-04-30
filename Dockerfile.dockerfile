FROM python:3.8-alpine

WORKDIR /flask
COPY . /flask

RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python" , "app.py"]