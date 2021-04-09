from main import db

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    subject=db.Column(db.String(150))
    message=db.Column(db.String())

class Ads(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(120))

class Comments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    subject=db.Column(db.String(150))
    message=db.Column(db.String(250))
    blogs=db.relationship('Blog',backref='comment')    

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120))
    text=db.Column(db.String(120))
    cover_img.Column(db.String(120))
    img=db.Column(db.String(120))
    date=db.Column(db.String(50))
    min_read=db.Column(db.String(50))
    comment_id=db.Column(db.Integer,db.ForeignKey('comment.id'))    