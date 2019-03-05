# Wiki Search

A UI for which help user in searching the wikipedia articles and download as a pdf with help of
[`pdfkit`](https://github.com/JazzCore/python-pdfkit) (`Wkhtmltopdf` python wrapper to convert html to pdf)


## Instructions to run locally

### Without Docker

-  **Install Dependencies**
    - To install [`pdfkit`](https://github.com/JazzCore/python-pdfkit) in the requirements we need to install [`whtmltopdf`](https://github.com/wkhtmltopdf/wkhtmltopdf) first.

        ```shell
        cd ~
        curl "https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz"
        tar Jxvf wkhtmltopdf.tar.xz
        mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf
        ```
    - Install requirements
        ```shell
        python3 -m virtualenv <environment name>
        source <environment name>/bin/activate
        pip install -r requirements.txt
        ```

- **Run Django server**
    ```shell
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver
    ```

### With Docker

- **Run docker deamon**
    ```
    docker build -t wikisearch . 
    docker run -p 8000:8000 -d wikisearch
    # http://0.0.0.0:8000/
    ```