from main import app,db

class Contact(db.Model):
    __tablename__='Contact_Form'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    subject=db.Column(db.String(150))
    message=db.Column(db.String(120))