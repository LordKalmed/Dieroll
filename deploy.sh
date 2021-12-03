#!/bin/bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip

pip3 install -r test_requirements.txt

docker system prune -a -f
docker-compose build
docker-compose up -d
sleep 10
docker-compose ps
docker-compose logs nginx
docker-compose logs service1
docker-compose logs service2
docker-compose logs service3
docker-compose logs service4
docker-compose push 
docker-compose down --rmi all



cd ansible
ansible-playbook -i inventory.yaml playbook.yaml

