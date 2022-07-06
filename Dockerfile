FROM python:3.8.9-slim-buster
#in the container, in a different place
WORKDIR /app 
COPY . . 
RUN pip3 install -r requirements.txt
RUN python3 create.py 
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]