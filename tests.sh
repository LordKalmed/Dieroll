sudo apt install python3
sudo apt install python3-pip

pip install -r test_requirements.txt 
pip3 install flask flask-testing pytest pytest-cov requests

cd service1
pytest --cov=app --cov-report term-missing --cov-report html:cov_service1_html
cd ..
cd service2
pytest --cov=app --cov-report term-missing --cov-report html:cov_service2_html
cd ..
cd service3
pytest --cov=app --cov-report term-missing --cov-report html:cov_service3_html
cd ..
cd service4
pytest --cov=app --cov-report term-missing --cov-report html:cov_service4_html
