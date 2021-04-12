from main import db
from datetime import datetime

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    subject=db.Column(db.String(150))
    message=db.Column(db.Text)

class Ads(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    url=db.Column(db.String(150))
    img=db.Column(db.String(120))


class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120))
    text=db.Column(db.String(120))
    img=db.Column(db.String(120))
    date=db.Column(db.DateTime,default=datetime.now())
    min_read=db.Column(db.String(50))
    comment=db.relationship('Comments',backref='blog',lazy=True) 

class Comments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    comment=db.Column(db.Text)
    blog_id=db.Column(db.Integer,db.ForeignKey('blog.id'))  