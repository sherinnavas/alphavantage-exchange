# Exchange Rate project using Alphavantage Api

This is a project build in Python-Django, which gives us two endpoints
1) POST - /api/v1/qoutes - Fetches exchange rate BTC/USD from Alphavantage API and saves it to database,
2) GET - /api/v1/qoutes - fetch the latest exchange data details from the database.

Using celery the POST functionality  is executed hourly.


## Steps To Run the Project


1) Clone the repo.

2) cd into the folder

3) Create a .env file and add the required parameters referring the sample.env

4) Build docker
```bash
docker-compose build
```

5) Run the container
```bash
docker-compose up
```

6) Access the endpoint & make GET or POST request
```bash
http://localhost:8000/api/v1/qoutes
```
