from flask import request, render_template,redirect, url_for, session
from functools import wraps
import bcrypt
from orm.user import User
from lib.response import Resp
from orm.userOnBan import UserOnBan

def pullNotif():
    message=session.get('message')
    session['message']=''
    return message

class LoginController:
    def login(self):
        # try:
        userLogin=dict(request.form)
        user=User.query.filter_by(msu_email=userLogin.get('email')).first()
        # default error message
        
        if not user:
            session['message']='Incorrect email or password'
            return redirect(url_for('user_bp.loginPage')) 
        
        userOnBan=UserOnBan.query.filter(UserOnBan.uob_msu_id== user.msu_id, UserOnBan.uob_release_date==None).first()

        if  bcrypt.checkpw(userLogin.get('password').encode('utf-8'), user.msu_password.encode('utf-8')):
            # success login
            if userOnBan:
                session['message']='You are banned from this site. Please contact the administrator to restore the account.'
                return redirect(url_for('user_bp.loginPage'))

            self.createSession(user)
            return redirect(url_for('user_bp.homePage')) 

        session['message']='Incorrect email or password'
        return redirect(url_for('user_bp.loginPage'))       
        # except:
        #     session['message']='Login Failed'
        #     return redirect(url_for('user_bp.loginPage')) 
            
    def createSession(self,user):
        session['user_id']=user.msu_id
        session['user_name']=user.msu_name

    def loginRequiredApi(self,func):
        @wraps(func)
        def decorated(**kwargs):
            try:
                if not session.get('user_id'):
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
                if not session.get('user_id'):
                    session['message']='You need to login first'
                    return redirect(url_for('user_bp.loginPage')) 
            except:
                session['message']='Bad Request'
                return redirect(url_for('user_bp.loginPage'))
            return func(**kwargs)
        return decorated
    
    def noSessionRequiredPage(self,func):
        @wraps(func)
        def decorated(**kwargs):
            try:
                if session.get('user_id'):
                    return redirect(url_for('user_bp.homePage'))
            except:
                return render_template('loginUser.html', message='Bad Request')
            return func(**kwargs)
        return decorated
    