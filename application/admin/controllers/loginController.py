from asyncio import constants
from email import message
from flask import request, render_template,redirect, url_for, session
from functools import wraps
import bcrypt
from orm.admin import Admin 
from lib.response import Resp

class LoginController:
    def login(self):
        try:
            adminLogin=dict(request.form)
            admin=Admin.query.filter_by(msa_email='obi@gmail.com').first()
            if not admin:
                return render_template('loginAdmin.html', message='Incorrect email or password')

            if  bcrypt.checkpw(adminLogin.get('password').encode('utf-8'), admin.msa_password.encode('utf-8')):
                self.createSession(admin)
                return redirect(url_for('admin_bp.homePage'))
            return render_template('loginAdmin.html', message='Incorrect email or password')       
        except:
            return render_template('loginAdmin.html', message='Login Failed')

    def createSession(self,admin):
        print(admin)
        session['admin_id']=admin.msa_id
        session['admin_name']=admin.msa_name

    def loginRequiredApi(self,func):
        @wraps(func)
        def decorated(**kwargs):
            try:
                if not session.get('admin_id'):
                    return Resp.withoutData('Forbidden Access')
            except:
                return Resp.withoutData('Bad Request')
            return func(**kwargs)
        return decorated
    
    def loginRequiredPage(self,func):
        @wraps(func)
        def decorated(**kwargs):
            try:
                print(session)
                if not session.get('admin_id'):
                    return render_template('loginAdmin.html', message='You need to login first')
            except:
                return render_template('loginAdmin.html', message='Bad Request')
            return func(**kwargs)
        return decorated
    
    def noSessionRequiredPage(self,func):
        @wraps(func)
        def decorated(**kwargs):
            try:
                if session.get('admin_id'):
                    return redirect(url_for('admin_bp.homePage'))
            except:
                return render_template('loginAdmin.html', message='Bad Request')
            return func(**kwargs)
        return decorated
    