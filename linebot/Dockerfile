FROM python:3.8-slim-bullseye

RUN apt-get update \
	&& apt-get install -y gcc-10 \		
	&& rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/gcc-10 /usr/bin/gcc

RUN pip install -U pip
RUN pip install django line-bot-sdk requests

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
