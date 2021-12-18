# pull official base image
FROM python:3.9.6-slim-buster
# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3","main.py"]