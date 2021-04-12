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
    end = db.session.query(Blog).order_by(Blog.id.desc()).limit(2)
    return render_template('main/author.html',ennd=end)     

@app.route("/post/<int:id>",methods=['GET','POST'])
def post(id):
    blog=Blog.query.get(id)
    end = db.session.query(Blog).order_by(Blog.id.desc()).limit(2)
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        comment=request.form['comment']
        id=id
        comment_p=Comments(name=name, email=email, comment=comment,blog_id=id)
        db.session.add(comment_p)
        db.session.commit()
        return redirect(f'/post/{id}')
    return render_template('main/post.html',blog=blog,ennd=end)       

@app.route("/contact",methods=['GET','POST'])
def contact():
    endBlogs = db.session.query(Blog).order_by(Blog.id.desc()).limit(3)
    end = db.session.query(Blog).order_by(Blog.id.desc()).limit(2)
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        contact=Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(contact)
        db.session.commit()
        return redirect('/contact')
    return render_template('main/contact.html',ennd=end,a=endBlogs)