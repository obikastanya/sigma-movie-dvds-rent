from email import message
from flask import request, render_template,redirect, url_for
import bcrypt
from orm.admin import Admin 

class LoginController:
    def login():
        try:
            adminLogin=dict(request.form)
            admin=Admin.query.filter_by(msa_email='obi@gmail.com').first()
            if not admin:
                return render_template('loginAdmin.html', message='Incorrect email or password')

            if  bcrypt.checkpw(adminLogin.get('password').encode('utf-8'), admin.msa_password.encode('utf-8')):
                return redirect(url_for('admin_bp.homePage'))
            return render_template('loginAdmin.html', message='Incorrect email or password')       
        except:
            return render_template('loginAdmin.html', message='Login Failed')