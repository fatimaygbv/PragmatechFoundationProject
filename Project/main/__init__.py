# main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import os


app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/data.db'
app.config['UPLOAD_PATH']='admin/static/upload'
db=SQLAlchemy(app)
migrate=Migrate(app,db,render_as_batch=True)
manager=Manager(app)
manager.add_command('db',MigrateCommand)

import models
from main.routes import *
import admin