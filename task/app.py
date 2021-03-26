from flask import Flask,render_template,request,redirect

app=Flask(__name__)

data=[
    {
        'id':1,
        'title': 'Vilayət Eyvazov baş leytenantı rəis təyin etdi',
        'content':""" 
        Göygöl Rayon Yol Polis bölməsinə rəis təyin edilib. 
        Oxu.Az xəbər verir ki, bununla bağlı Daxili İşlər naziri, general-polkovnik Vilayət Eyvazov əmr imzalayıb.
        Əmrə əsasən, bu vəzifəyə baş leytenant Rəşad Məmişov təyin edilib.
        Qeyd edək ki, Rəşad Məmişov daha əvvəl Daşkəsən rayonu Dövlət Yol Polisinin baş inspektoru vəzifəsində çalışıb.
        """,
        'img':'../static/img/1.jpg'
    },
    {
        'id':2,
        'title': 'BMT ilə Azərbaycan arasında əməkdaşlıq sənədi imzalanıb',
        'content':"""Birləşmiş Millətlər Təşkilatı ilə Azərbaycan arasında əməkdaşlıq müqaviləsi imzalanıb.Baku TV mərasimdən videonu təqdim edir:
        """,
        'img':'../static/img/2.jpg'
    },
    {
        'id':3,
        'title': 'Qlobalistlər Ağ Evə qayıtdılar, Türkiyə necə davranacaq?',
        'content':"""İndi Türkiyənin birmənalı geosiyasi vektorundan danışmaq çətindi, ölkə NATO-nun üzvü olaraq qalır. Ancaq fərqli mövqe tutmağa və Şərqdə alternativ sivilizasiya qütbünün formalaşmasına meyllər var.
        """,
        'img':'../static/img/3.jpg'
    }
]

users=[]
id=1
@app.route('/')
def index():
    return render_template('index.html',data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', methods=['GET', 'POST'])
def user():
    global id
    if request.method=='POST':
        ad=request.form['name']
        soyad=request.form['surname']
        id+=1
        users.append({
            'id':id,
            'name':ad,
            'surname':soyad
        })
        return render_template('users.html',userlist=users)
    return render_template('users.html')

@app.route('/delete/<int:id>',methods=['GET', 'POST'])
def delete(id):
    for item in users:
        if item['id']==id:
            users.remove(item)
            return redirect('/users')
    return render_template('users.html')
if __name__=='__main__':
    app.run(debug=True)