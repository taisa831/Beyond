## 

```
## clone
git clone git@bitbucket.org:taisa007/beyond.git
cd beyond

## virtualenv
virtualenv env
source env/bin/activate
pip install -r requirement.txt

## mysql
SET PASSWORD FOR root@localhost=PASSWORD('password');
create schema beyond;

## migrate
python manage.py migrate

## mysql data import
mysql -uroot -p beyond < docs/beyond_2015-05-31.sql

```