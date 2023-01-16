# CookieCutter_Flask_API

A cookiecutter template to create an api using Flask, SQLAlchemy, Marshmallow, and APIFairy.
The finished project runs in docker with docker-compose with an nginx proxy to allow serving static files if needed.

## Start a project

1. `cookiecutter https://github.com/tcarwash/cookiecutter_flask_api`
   - Give your project a name
   - Create a database user
   - Create a database password
2. Edit the ENV file, change the secret key
3. `docker-compose build`
4. `docker-compose up` or `docker-compose up -d`

- The app directory is brought in as a volume into the web container, so any changes made there will be reflected in the container
- `flask db init`, `flask db migrate`, and `flask db upgrade` are run on start
- The initial project has placeholder models/schemas that are very likely not relevant to your project, these should be removed prior to the first run
