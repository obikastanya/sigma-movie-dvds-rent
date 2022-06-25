from app import app


from module.admin.route import first_module_bp
from module.renter.route import second_module_bp

app.register_blueprint(first_module_bp, url_prefix='/first-module')
app.register_blueprint(second_module_bp, url_prefix='/second-module')
