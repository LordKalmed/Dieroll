#!/bin/bash

cd service1
pytest --cov=app 
cd service2
pytest --cov=app 
cd service3
pytest --cov=app 
cd service4
pytest --cov=app 

cd

docker-compose up -d
docker-compose ps
docker-compose logs nginx
docker-compose logs service1
docker-compose logs service2
docker-compose logs service3
docker-compose logs service4
docker-compose down --rmi all