#!/bin/bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip




docker-compose up -d
sleep 15
docker-compose ps
docker-compose logs nginx
docker-compose logs service1
docker-compose logs service2
docker-compose logs service3
docker-compose logs service4
docker-compose down --rmi all

docker system prune -a -y
