# Youtube Search App

The project has 2 main components i.e first fetching the data from youtube and storing it in database and second exposing api's to get the data from DB.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Database

SQlite Database is used as it is easy to create and use. A single table "Video" is defined
in the Database. The table consists of necessary details of a video like title, description etc.

## Views

There are 3 routes defined.

1. Base url to check if server is up and Running
2. To get the data from DB in paginated form.
3. Search API to search in DB.

## Installation

Clone Repository

```bash
   git clone https://github.com/sushant66/youtube_search_app.git
```

Project setup

```bash
    cd youtube_search_app
```

Setting up virtual environment and activating it

```bash
    python -m venv env
```

For Linux

```bash
    source env/bin/activate
```

For windows

```
    .\env\Scripts\activate
```

Installing dependencies

```bash
    pip install -r requirements.txt
```

Running the server

```bash
    python app.py
```

## Available routes

For server check

```bash
    http:\\localhost:5000
```

For getting data stored in DB

Default route to get page 1 data

```bash
    http:\\localhost:5000\videos
```

To get data from particular page (replace page_no with 1,2..)

```bash
    http:\\localhost:5000\videos\page\{page_no}
```

## Steps for dockerizing (Only for linux)

Build Image

```bash
    sudo docker build --tag youtube-search-app .
```

Run docker container in detached mode and expose port

```bash
    docker run -d -p 5000:5000 youtube-search-app
```

To stop the container use below command

```bash
    sudo docker stop <container_id>
```
