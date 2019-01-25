# app-crawler

This crawler is written by Python3.

## Introduction

A crawler which is designed to crawl frequently downloaded apk packages from the mainstream Android application markets in China.

## Dependency

```
beautifulsoup4          4.7.1
certifi                 2018.11.29
chardet                 3.0.4
idna                    2.8
pymongo                 3.7.2
requests                2.21.0
soupsieve               1.7.2
urllib3                 1.24.1
```

## Development and Deployment

- Python3 and pip3 needed
- MongoDB needed
- Download the virtual environment configuration globally
    ```bash
    $ pip3 install virtualenv
    ```
- Download this repository to your own device
    ```bash
    $ git clone git@github.com:wurahara/app-crawler.git
    $ cd app-crawler
    ```
- Create a python virtualenv in the project directory
    ```bash
    $ virtualenv venv
    ```
- Active the virtualenv and install dependencies
    ```bash
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```
- Start MongoDB service
    ```bash
    $ mongod --config /usr/local/etc/mongod.conf
    ```
- Start the crawler
    ```bash
    $ python3 index.py
    ```
- Deactivate the virtualenv
    ```bash
    $ deactivate
    ```
## Description

This repository is part of the Android App Privacy Protection Project, whose aim is to protect the privacy of mobile phones and prevent confidential information from leaking under confidential environments. In order to evaluate the safety factor of mainstream Android applications, it is necessary to conduct a security assessment towards a widest range of applications on application markets. Thus, an automated method is needed to get the apks on the mainstream Android markets. This script is designed to get the apk download links and persist them for further operations.

## License

This repository is released under [MIT](https://github.com/wurahara/app-crawler/blob/master/LICENSE) licence.
Copyright © [Rui Song](https://github.com/wurahara).
