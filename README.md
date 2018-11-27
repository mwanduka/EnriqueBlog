# EnriqueBlog

## Link to deployed site


## Setup and installations
Prerequisites
Python3.6
Postgres
virtualenv
Pip


## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- Heroku
- Postgresql
-Flask framework

## Running and installing the app
Clone the Repo and checkout into the project folder.
git clone
Create and activate the virtual environment
python3.6 -m virtualenv virtual
source virtual/bin/activate
Setting up environment variables

Create the Database
In a new terminal, open the postgresql shell with psql.

CREATE DATABASE EnriqueBlog;

Make and run migrations
python3.6 manage.py makemigrations && python3.6 manage.py migrate

Run the app
./start.sh
Open localhost:5000

## Known bugs
none yet

## Support and contact details
Contact mwandukastephen20@gmail.com for further help/support

## License
MIT

Copyright (c)2018 Mwanduka Stephen
