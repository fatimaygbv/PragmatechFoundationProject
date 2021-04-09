# admin
from main import *

admin_bp=Blueprint('admin',__name__,template_folder='templates',static_folder='static',url_prefix='/admin')

@admin_bp.route("/")
def admin():
    AllResponses=Contact.query.all()
    return render_template('admin/base.html',contact=AllResponses)

@admin_bp.route("/blogs")
def admin_blogs():
    return render_template('admin/blogs.html')    

@admin_bp.route("/new-blog")
def admin_new_blog():
    return render_template('admin/new_blog.html')      

@admin_bp.route("/comments")
def admin_comments():
    return render_template('admin/comments.html')     

@admin_bp.route("/contact-form")
def admin_contact_form():
    AllResponses=Contact.query.all()
    return render_template('admin/contact-form.html',responses=AllResponses)  

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