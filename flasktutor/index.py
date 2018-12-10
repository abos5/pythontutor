# all the imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import MySQLdb


SQLALCHEMY_DATABASE_URI = 'mysql://root:3a7d30f2de@db.host/abostutor'
USERNAME = 'abos5'
PASSWORD = 'awesome'
DEBUG = True

# configuration
app = Flask(__name__)

app.config.from_object(__name__)
g = {
    'db': None
}


def connect_db():
    return g.db


# create our little application :)


@app.before_request
def before_request():
    g['db'] = SQLAlchemy(app)
    pass


@app.teardown_request
def teardown_request(exception):
    db = g['db']
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()

#eof
