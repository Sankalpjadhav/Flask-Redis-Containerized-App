# Use an official Python runtime as pa parent image

FROM python:3.8-slim

# Set the working firectory to /app

WORKDIR /app

# Copy the current firectory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container

EXPOSE 80

# Define environment variable

ENV NAME World

# Run app.py whent he container launches

CMD ["python3", "app.py"]
