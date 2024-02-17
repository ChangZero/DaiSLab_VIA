FROM python:3.10.6
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y
ENV TZ Asia/Seoul
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8888
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]