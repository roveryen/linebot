# About
This is my python execrise with django framework and linebot sdk library.
With this execrice, I learned some knowledge that like:

1. Build the docker image for pre-installing django and linebot-sdk.
2. Utilize the linebot to react with people in LINE group.


# Prerequisite

1. build a basic image for pre-install django and linebot-sdk

   `docker build linebot -t python:linebot`

2. bring up docker

   `docker-compose up -d`

# fill the values from LINE developers to settings.py

   `cp project/main/settings.sample.py project/main/settings.py`


```python
LINE_CHANNEL_ACCESS_TOKEN = ''

LINE_CHANNEL_SECRET = ''
```

# Run

1. go into docker container

   `docker exec -it linebot bash`

3. start service

   `cd /project && python manage.py runserver`


   
