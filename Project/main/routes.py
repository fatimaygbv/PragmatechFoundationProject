# main
from main import app,db
from models import *
from flask import Blueprint,render_template,request,url_for,flash,redirect

@app.route("/")
def main():
    blog = Blog.query.all()
    endBlogs = db.session.query(Blog).order_by(Blog.id.desc()).limit(3)
    end = db.session.query(Blog).order_by(Blog.id.desc()).limit(2)
    return render_template('main/home.html',blog=blog,endBlogs=endBlogs,ennd=end)    

@app.route("/author")
def author():
    return render_template('main/author.html')     

@app.route("/post/<int:id>")
def post(id):
    blog=Blog.query.get(id)
    return render_template('main/post.html',blog=blog)       

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