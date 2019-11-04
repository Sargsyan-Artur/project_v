--------- db ----------------
sudo apt-get update
sudo apt-get install mysql-server
mysql -u root -p
show databases;
CREATE DATABASE myproekt;
GRANT ALL PRIVILEGES ON myproekt.* TO 'user'@'%' WITH GRANT OPTION;
pip install mysqlclient


---------------GIT-----------------
git init
git clone https://github.com/Sargsyan-Artur/test.git #copy in git
cd clone project
git add .
git status
git commit -m "Add views.py"
git push
git pull -------- download change code


you change code
git add .
git status
git commit -m "Add change file"
git push

-------BLACK------------
pip install black
black ./
pip freeze > requirements.txt

----venv---------
virtualenv venv
source venv/bin/activate
pip install django
pip install python
sudo apt-get upgrade python3


django-admin.py startproject project_name .
