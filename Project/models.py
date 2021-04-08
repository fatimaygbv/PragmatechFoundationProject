from main import app,db

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    subject=db.Column(db.String(150))
    message=db.Column(db.String(250))

class Ads(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(120))