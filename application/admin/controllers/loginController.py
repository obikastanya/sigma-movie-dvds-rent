from flask import request, render_template,redirect, url_for, session
from functools import wraps
import bcrypt
from orm.admin import Admin 
from lib.response import Resp

def pullNotif():
    message=session.get('message')
    session['message']=''
    return message

class LoginController:
    def login(self):
        # try:
        adminLogin=dict(request.form)
        print(adminLogin)
        admin=Admin.query.filter_by(msa_email=adminLogin.get('email')).first()
        # default error message
        if not admin:
            session['message']='Incorrect email or password'
            return redirect(url_for('admin_bp.loginPage'))       

        if  bcrypt.checkpw(adminLogin.get('password').encode('utf-8'), admin.msa_password.encode('utf-8')):
            # success login
            self.createSession(admin)
            return redirect(url_for('admin_bp.homePage')) 

        session['message']='Incorrect email or password'
        return redirect(url_for('admin_bp.loginPage'))       
        # except:
        #     session['message']='Login Failed'
        #     return redirect(url_for('admin_bp.loginPage')) 
            
    def createSession(self,admin):
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
                print('session data',session)
                if not session.get('admin_id'):
                    session['message']='You need to login first'
                    return redirect(url_for('admin_bp.loginPage')) 
            except:
                session['message']='Bad Request'
                return redirect(url_for('admin_bp.loginPage'))
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
    