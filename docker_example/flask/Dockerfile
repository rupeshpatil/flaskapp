FROM python:3

# Set working directory to app
WORKDIR /app

# copy current directory contents into the container at /app
ADD . /app

RUN pip install -r requirement.txt 

# run command to start uWSGI

CMD ["uwsgi", "app.ini"]