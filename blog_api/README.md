
## Installation
  - Install [Python](https://www.python.org/downloads/) and [Postgres](https://www.postgresql.org/) on your machine
  - Activate the project virtual environment with `$ pipenv shell` command
  - Install all required dependencies with `$ pip install -r requirement.txt`
  - Export the required environment variables
      ```
      $ export FLASK_ENV=development
      $ export DATABASE_URL=postgres://name:password@houst:port/blog_api_db
      $ export JWT_SECRET_KEY=hhgaghhgsdhdhdd
      ```
  - Start the app with `python run.py`


## Reference
- https://www.codementor.io/olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5

