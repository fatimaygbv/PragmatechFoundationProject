# main
from main import app,db
from flask import Blueprint,render_template,request,url_for,flash,redirect
from models import *

@app.route("/")
def main():
    return render_template('main/home.html')

@app.route("/2")
def main_2():
    return render_template('main/home-2.html')    

@app.route("/author")
def author():
    return render_template('main/author.html')     

@app.route("/post")
def post():
    return render_template('main/post.html')       

@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        contact=Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(contact)
        db.session.commit()
        return redirect('/contact')
    return render_template('main/contact.html')  