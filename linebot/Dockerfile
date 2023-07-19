FROM python:latest

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \		
	&& rm -rf /var/lib/apt/lists/*


RUN pip install django
RUN pip install line-bot-sdk
RUN pip install requests

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
