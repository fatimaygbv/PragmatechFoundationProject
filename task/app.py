from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Homepage'

@app.route('/delete/<id>')
def admin(id):
    return id

if __name__=='__main__':
    app.run(debug=True)