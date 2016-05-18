Start your engines
==================

The first steps to check if everything's ready to start developing and look around in the admin section of the django project

1. `source .env-dev`
2. migrate
3. create superuser
4. start server, visit localhost:8000 and localhost:8000/admin
5. create a new user and login with that user


Hint:
Django has a management script (manage.py). It's located in the project dir. Do a

    birthdays-project/manage.py

to see the list of all available commands

The one's that help for these tasks are:

* migrate (creates or updates the database)
* createsuperuser (creates a super user, required to be able to login)
* runserver (starts the server on localhost)

Database: we use the sqlite3 for the first steps. If you want to start over, simply locate and delete the `dev.sqlite3` file. Then 'migrate' again to create a new, empty db.