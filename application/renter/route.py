from flask import Blueprint, render_template,session, redirect, url_for
from .controllers.loginController import LoginController, pullNotif
from .controllers.registerController import RegisterController
from .controllers.movieDvdsController import MovieDvdsController
from .controllers.dvdReviewsController import DvdReviewController

user_bp=Blueprint(
    'user_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static',
    static_url_path='/user/static')

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
    return render_template('movieDashboard.html')


@user_bp.get('/register')
@auth.noSessionRequiredPage
def registerPage(**kwargs):
    return render_template('registerUser.html')


@user_bp.get('/review/dvd/<id>/')
@auth.loginRequiredPage
def reviewDvd(**kwargs):
    id=kwargs.get('id')
    print('shiit happened')
    return render_template('movieReview.html', id=id)


@user_bp.get('/logout')
@auth.loginRequiredPage
def logout(**kwargs):
    session.clear()
    return redirect(url_for('user_bp.loginPage'))

# api 
@user_bp.post('/login')
def cekLogin():
    return LoginController().login()

@user_bp.post('/register')
def registerUser(**kwargs):
    return RegisterController.insertUser()

@user_bp.get('/user/dvd')
def getDvds():
    return MovieDvdsController.getMovieDvds()

@user_bp.get('/user/dvd/<id>/')
def getDvd(id):
    return MovieDvdsController.getMovieDvd(id)

@user_bp.get('/user/review/dvd-data/<id>')
# @auth.loginRequiredApi
def reviewPage(**kwargs):
    id=kwargs.get('id')
    return DvdReviewController.getDvdReviews(id)
