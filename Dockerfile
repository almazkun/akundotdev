# We Use an official Python runtime as a parent image
FROM python:3.8
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /<dir-in-container>
# Set the working directory to /music_service
WORKDIR /<dir-in-container>
# Copy the current directory contents into the container at /music_service
ADD . /<dir-in-container>/
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn <Django-project_name>.wsgi:application — bind 0.0.0.0:8000 — workers 3