from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    surname=db.Column(db.String(50))
    email=db.Column(db.String(50))
    details=db.Column(db.String(250))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method=='POST':
        name=request.form['user_name']
        surname=request.form['user_surname']
        email=request.form['user_email']
        details=request.form['user_detail']
        user=User(name=name, surname=surname, email=email, details=details)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    return render_template('new.10.02.html')

@app.route("/delete/<id>")
def delete(id):
    userforDelete=User.query.get(id)
    db.session.delete(userforDelete)
    db.session.commit()
    return redirect('/users')

@app.route('/detail/<id>')
def detail(id):
    userForShow=User.query.get(id)
    return render_template('detail.html',user=userForShow)

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    userForUpdate=User.query.get(id)
    if request.method=='POST':
        name=request.form['user_name']
        surname=request.form['user_surname']
        email=request.form['user_email']
        details=request.form['user_detail']
        userForUpdate.name=name
        userForUpdate.surname=surname
        userForUpdate.email=email
        userForUpdate.details=details
        db.session.commit()
        return redirect('/users')
    return render_template('update.html',user=userForUpdate)

@app.route('/users')
def users():
    allUsers=User.query.all()
    return render_template('users-10.02.html', users=allUsers)        

if __name__=='__main__':
    app.run(debug=True) 