# Pull base image
FROM python:3.7-slim

# File Author / Maintainer
MAINTAINER Adriaan Knapen <hi@aknapen.nl>

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt
RUN pip install gunicorn

# Collect our static media.
RUN python /code/manage.py collectstatic --noinput

# Install dependencies
RUN pip install -r /code/requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]