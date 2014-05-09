Introduction
----
This is a tutorial like the [Symfony2 tutorial](https://github.com/oveach/sf2-tutorial) to demonstrate a simple Django CRUD-like web app. The particularity is the usage of SQLAlchemy for ORM, instead of the ORM provided by Django. SQLAlchemy is a data mapper ORM like Doctrine2 in PHP or Hibernate in java and it's very powerful. So it's best comparable to my PHP tutorial.

Prepare the environment
----
First, we need some system packages to let SQLAlchemy speak with MySQL:

    sudo apt-get install libmysqlclient-dev python-dev

We will install the project in a virtual environment, the recommended way to deal with python projects. So first install these tools if you don't have it:

    sudo apt-get install python-setuptools
    sudo easy_install pip
    pip install virtualenv

Then create the virtual environment for you project like this:

    virtualenv /home/foo/django-tutorial

This creates the <code>/home/foo/django-tutorial</code> directory with some files to create an isolated python environement.
Now activate the environment and we're ready to go!

    source /home/foo/django-tutorial/bin/activate

The prompt will now display (django-tutorial) to indicate we are into the virtual environment. To quit it and go back to normal shell, just type:

    deactivate

Install the dependencies
---
Time to install the framework and libs our project will use:

    pip install django
    pip install sqlalchemy
    pip install mysql-python
    
### Create the Django project:
Follow these steps to start from scratch, otherwise the git repository contains everything needed.

    django-admin.py startproject projet_test
    
It creates a little tree with some python files in it, mainly <code>manage.py</code> which is the central point to manage the django project.
Then you need to create a django app that we name here <i>albums</i>:

    cd projet_test
    python manage.py startapp albums

### Launch the dev server:
Final step to launch our web app:

    python manage.py runserver
    
Now your web app is accessible through url: http://localhost:8000/

Congrats you're ready to code!