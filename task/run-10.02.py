from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new')
def new():
    return render_template('new.10.02.html')

@app.route('/users')
def users():
    return render_template('users-10.02.html')        

if __name__=='__main__':
    app.run(debug=True)  