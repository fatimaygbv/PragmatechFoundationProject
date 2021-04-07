# main

from flask import Blueprint,render_template

main_bp=Blueprint('main',__name__,template_folder='templates',static_folder='static', url_prefix='/main')

@main_bp.route("/")
def main():
    return render_template('main/home.html')