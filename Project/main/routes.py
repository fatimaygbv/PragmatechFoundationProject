# main
from main import app
from flask import Blueprint,render_template,render_template, request,url_for,flash
import models

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
        response=Responses(name=name, email=email, subject=subject, message=message)
        db.session.add(response)
        db.session.commit()
        return redirect('main/contact.html')
    return render_template('main/contact.html')  

import models    