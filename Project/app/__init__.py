# app

from flask import Flask,render_template,request,redirect,Blueprint
from admin.routes import admin_bp
from main.routes import main_bp

app=Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(main_bp)