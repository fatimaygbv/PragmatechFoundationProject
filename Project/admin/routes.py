# admin
from main import *
from werkzeug.utils import secure_filename
import os

admin_bp=Blueprint('admin',__name__,template_folder='templates',static_folder='static',url_prefix='/admin')


@admin_bp.route("/")
def admin_blogs():
    blogs=Blog.query.all()
    return render_template('admin/blogs.html',blogs=blogs)    

@admin_bp.route("/new-blog",methods=['GET','POST'])
def admin_new_blog():
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        filePath=f"/{app.config['UPLOAD_PATH']}/{filename}"
        post=Blog(
            title=request.form['title'],
            text=request.form['text'],
            img=filePath,
            min_read=request.form['min_read'])
        db.session.add(post)
        db.session.commit()
        return redirect ('/admin')
    return render_template('admin/new_blog.html') 

@admin_bp.route("/comments")
def admin_comments():
    comments=Comments.query.all()
    return render_template('admin/comments.html',comments=comments)     

@admin_bp.route("/commentdelete/<id>")    
def commentDelete(id):
    db.session.delete(Comments.query.get(id))
    db.session.commit()
    return redirect ('/admin/comments')

@admin_bp.route("/contact-form")
def admin_contact_form():
    contact=Contact.query.all()
    return render_template('admin/contact-form.html',contact=contact)  

@admin_bp.route("/delete/<id>")
def delete(id):
    responseforDelete=Contact.query.get(id)
    db.session.delete(responseforDelete)
    db.session.commit()
    return redirect('/admin/contact-form')    

@admin_bp.route("/blogdelete/<id>")
def blogDelete(id):
    blogDelete=Blog.query.get(id)
    db.session.delete(blogDelete)
    db.session.commit()
    return redirect('/admin')  

@admin_bp.route("/ads")
def admin_ads():
    ads=Ads.query.all()
    return render_template('admin/ads.html',ads=ads)      

@admin_bp.route("/new-ad",methods=['GET','POST'])
def admin_new_ad():
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        filePath=f"/{app.config['UPLOAD_PATH']}/{filename}"
        ad=Ads(
            name=request.form['name'],
            img=filePath,
            url=request.form['url']
        )
        db.session.add(ad)
        db.session.commit()
        return redirect ('/admin/new-ad')
    return render_template('admin/new_ad.html')

@admin_bp.route("/addelete/<id>")    
def adDelete(id):
    db.session.delete(Ads.query.get(id))
    db.session.commit()
    return redirect ('/admin/ads')    