from flask import Blueprint, render_template,session, redirect, url_for
from .controllers.loginController import LoginController, pullNotif

user_bp=Blueprint(
    'user_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static')

auth=LoginController()

# route
@user_bp.get('/login')
@auth.noSessionRequiredPage
def loginPage(**kwargs):
    message=pullNotif()    
    return render_template('loginUser.html', message=message)

@user_bp.get('/home')
@auth.loginRequiredPage
def homePage(**kwargs):
    return render_template('userMaster.html')


@user_bp.get('/register')
@auth.noSessionRequiredPage
def registerPage(**kwargs):
    return render_template('registerUser.html')


@user_bp.get('/logout')
@auth.loginRequiredPage
def logout(**kwargs):
    session.clear()
    return redirect(url_for('user_bp.loginPage'))

# api 
@user_bp.post('/login')
def cekLogin():
    return LoginController().login()