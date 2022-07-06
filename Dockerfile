FROM python:3.8.9-slim-buster
WORKDIR /directoryForMyApp
ADD . /directoryForMyApp/
RUN pip install -r requirements.txt
# Copy the app file into the image working directory
COPY app.py .
# State the listening port for the container. 
# The app's code does not actually specify the port, so it would be useful to include here.
EXPOSE 5000
# Run 'python app.py' on container start-up. This is the main process.
ENTRYPOINT ["python", "app.py"]