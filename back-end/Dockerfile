FROM python:3.7-alpine

# Set environmment variable
ENV DockerHOME=/usr/src/app

# Set working directory
WORKDIR $DockerHOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN python3 -m pip install --upgrade pip
COPY ./requirements.txt $DockerHOME/requirements.txt
RUN pip3 install -r requirements.txt

# Copy project
COPY . $DockerHOME

# Open a port
EXPOSE 8000
