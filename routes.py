from app import app
from application.admin.route import admin_bp
from application.renter.route import user_bp

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp)