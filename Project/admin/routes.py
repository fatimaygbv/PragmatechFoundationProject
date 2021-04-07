# admin

from flask import Blueprint,render_template

admin_bp=Blueprint('admin',__name__,template_folder='templates',static_folder='static',url_prefix='/admin')

@admin_bp.route("/")
def admin():
    return render_template('admin/base.html')

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
    return render_template('admin/contact-form.html')  

@admin_bp.route("/ads")
def admin_ads():
    return render_template('admin/ads.html')      

@admin_bp.route("/new-ad")
def admin_new_ad():
    return render_template('admin/new_ad.html')                     