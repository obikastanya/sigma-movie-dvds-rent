from app import app
from application.admin.route import admin_bp

app.register_blueprint(admin_bp, url_prefix='/admin')