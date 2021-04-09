# admin
from main import *

admin_bp=Blueprint('admin',__name__,template_folder='templates',static_folder='static',url_prefix='/admin')

@admin_bp.route("/")
def admin():
    blogs=Blog.query.all()
    comments=Comments.query.all()
    AllResponses=Contact.query.all()
    return render_template('admin/base.html',contact=AllResponses,blogs=blogs)

@admin_bp.route("/blogs")
def admin_blogs():
    blogs=Blog.query.all()
    return render_template('admin/blogs.html')    

@admin_bp.route("/new-blog",methods=['GET','POST'])
def admin_new_blog():
    blogs=Blog.query.all()
    comments=Comments.query.all()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        post=Blog(
            title=request.form['title'],
            text=request.form['text'],
            img=filename,
            min_read=request.form['min_read'],)
        db.session.add(post)
        db.session.commit()
        redirect ('/admin/blogs')
    return render_template('admin/new_blog.html',blogs=blogs)      

@admin_bp.route("/comments")
def admin_comments():
    return render_template('admin/comments.html')     

@admin_bp.route("/contact-form")
def admin_contact_form():
    AllResponses=Contact.query.all()
    return render_template('admin/contact-form.html',contact=AllResponses)  

@admin_bp.route("/delete/<id>")
def delete(id):
    responseforDelete=Contact.query.get(id)
    db.session.delete(responseforDelete)
    db.session.commit()
    return redirect('/admin/contact-form')    

@admin_bp.route("/ads")
def admin_ads():
    return render_template('admin/ads.html')      

@admin_bp.route("/new-ad")
def admin_new_ad():
    return render_template('admin/new_ad.html')                    