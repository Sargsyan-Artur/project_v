#db 
  mysql -u root -p
  show databases;
  CREATE DATABASE myproekt;
  GRANT ALL PRIVILEGES ON myproekt.* TO 'user'@'%' WITH GRANT OPTION;
  git init
   
 #GIT
   git clone https://github.com/Sargsyan-Artur/test.git copy in git
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

pip freeze
pip install -r requirements.txt