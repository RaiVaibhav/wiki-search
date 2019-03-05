FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common vim && add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

RUN apt-get install -y curl libxrender1 libfontconfig libxtst6 xz-utils
RUN curl "https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz"
RUN tar Jxvf wkhtmltopdf.tar.xz
RUN mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf
RUN mkdir -p /app

WORKDIR /app
ADD . /app

RUN python3.6 -m pip install -r requirements.txt
RUN python3.6 manage.py makemigrations && python3.6 manage.py migrate
EXPOSE 8000
CMD ["python3.6", "manage.py", "runserver", "0.0.0.0:8000"]