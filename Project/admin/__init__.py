# admin
from main import app
from .routes import admin_bp

app.register_blueprint(admin_bp)