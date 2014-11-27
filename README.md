django_tuts
===========

Django Tutorials 

This project contains two apps.
  1. myapp
  2. formtut

Install requirements in the virtualenv from the requirements.txt.
      pip install -r requirements.txt

Apps reside at following address:
  1. myapp: '127.0.0.1:8000/myapp'
  2. formstut: '127.0.0.1:8000/forms/'
  
Create a file called evn\_vars.sh and save the SECRET\_KEY and posgresql password(if using Postgresql) as follows:

      export REVIEW_SECRET_KEY='<your-secret-key>'
      export PG_PASSWORD='<your-postgresql-password>'

Initialize DJANGO\_SETTINGS\_MODULE with init\_base.sh for using sqlit3 else init\_dev.sh as following:
        
        source init_base.sh
or 

        source init_dev.sh

