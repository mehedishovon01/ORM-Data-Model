# ORM-Data-Model-using-Django-Framework
A Python web framework task from Qtec Solution Limited. This project is running on django version 5.0 and python version 3.10.12


# Introduction
The goal of this project is to create filtering & search options. And the display the data in frontend. And then realtime filtering from checkbox using JS. After that publish into a Heroku Server.

_Note: Here, I have used a free html template for displaying and filtering the data. I have used JavaScript for realtime filtering is used in the `_sidebar.html` file because the filtering checkboxes of the template I used are placed in the sidebar._

_Also_ want to cover up this things

* Templates and Static Files
* Models and Database Interactions
* JS Integrating and Realtime Filtering
* Documentation (Commenting inside the Project)
* Deploy the Project in the Heroku Server


# Project Setup

To use this project to your own machine follow this steps

### Clone repository from github

First of all, clone this repository using this command

    git clone https://github.com/mehedishovon01/ORM-Data-Model-using-Django-Framework.git

### Create a virtualenv

Make a virtual environment to your project directory. Let's do this,

If you have already an existing python virtualenv then run this

    virtualenv venv

Or if virtualenv is not install in you machine then run this

    python -m venv venv
    
Activate the virtual environment and verify it

    . venv/bin/activate

### Install the dependencies

Most of the projects have dependency name like requirements.txt file which specifies the requirements of that project, so let’s install the requirements of it from the file.

    pip install -r requirements.txt

### Create database

We have already sqlite3 setup in our project.

So, simply apply the migrations:

    python manage.py migrate
    
Boooooom! Your project setup is done.

### Run this project

Let's run the development server:

    python manage.py runserver

That’s it! Now you’re project is already run into a development server. 

Just click this link, [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


Thanks for reading.