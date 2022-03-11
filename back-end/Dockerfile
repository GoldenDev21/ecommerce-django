FROM python:3.7-alpine

# Set environmment variable
ENV DockerHOME=/home/app/webapp

# Set working directory
WORKDIR $DockerHOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt $DockerHOME/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . $DockerHOME

# Open a port
EXPOSE 8000
