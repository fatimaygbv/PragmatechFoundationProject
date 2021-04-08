# main
from flask import Flask
from admin import admin_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
# from flask_script import Manager

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/data.db'
app.config['UPLOAD_PATH']='admin/static/uploads'
db=SQLAlchemy(app)
migrate=Migrate(app,db,render_as_batch=True)

app.register_blueprint(admin_bp)
from main.routes import *
import admin