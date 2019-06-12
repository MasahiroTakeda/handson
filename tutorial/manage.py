from __future__ import print_function
from flask_script import Manager
from flaskr import app, db
#from flask_sqlalchemy import SQLAlchemy

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()

    #flask.ext.script 