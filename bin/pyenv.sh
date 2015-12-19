#sudo yum install python-pip
sudo yum install python-virtualenv
mkdir ./django
cd ./django
virtualenv env
source env/bin/activate
pip install -i http://mirrors.aliyuncs.com/pypi/simple django==1.4
