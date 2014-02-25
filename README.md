django-cms-boilerplate
======================
## Installation
- Set up a new [virtualenv](http://www.virtualenv.org/en/latest/)
- Create a new [django-project](https://docs.djangoproject.com/en/1.6/ref/django-admin/#django-admin-startproject)
- Replace the new project directory with this django-cms-boilerplate project
- Activate your virtualenv to make sure you install the requirements only in this virtualenv
- Change the current working directory to the new django-cms-boilerplate directory
- Run "pip install -r requirements.txt" to install all requirements for this project in the fresh new virtualenv
- Run "pythonX.X manage.py syncdb" and create the new superuser when prompted
- Run "pythonX.X manage.py migrate" to migrate the database
- Display your site in a browser, login and create new pages in the django-cms
