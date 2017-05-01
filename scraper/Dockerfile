FROM python:2.7-alpine
ADD . /scraper
WORKDIR /scraper
RUN pip install -r requirements.txt
CMD ["python", "newnym.py"]