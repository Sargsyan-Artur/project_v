--------- db ----------------
sudo apt-get update
sudo apt-get install mysql-server
mysql -u root -p
show databases;
CREATE DATABASE myproekt;
GRANT ALL PRIVILEGES ON myproekt.* TO 'user'@'%' WITH GRANT OPTION;
pip install mysqlclient
---------------GIT----
git branch
git checkout master
git status
git remote add origin https://github.com/Sargsyan-Artur/codics.git   git um  creat arac papki liky vor pti upload lini  
---------------GIT----
for checkout on branch in git: git checkoput <branch name>
for create new branch and checkout in git: git checkout -b <branch name>

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
