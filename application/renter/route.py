from flask import Blueprint, render_template,session, redirect, url_for
from .controllers.userController import UserController
from .controllers.loginController import LoginController, pullNotif
from .controllers.registerController import RegisterController
from .controllers.movieDvdsController import MovieDvdsController
from .controllers.dvdReviewsController import DvdReviewController
from .controllers.renterController import RenterController
from .controllers.invoiceController import InvoiceController
from .controllers.alertController import AlertController

user_bp=Blueprint(
    'user_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static',
    static_url_path='/user/static')

auth=LoginController()

# route -> returning html


@user_bp.get('/register')
@auth.noSessionRequiredPage
def registerPage(**kwargs):
    return render_template('registerUser.html')

@user_bp.get('/login')
@auth.noSessionRequiredPage
def loginPage(**kwargs):
    message=pullNotif()    
    return render_template('loginUser.html', message=message)

@user_bp.get('/home')
@user_bp.get('/')
@auth.loginRequiredPage
def homePage(**kwargs):
    return render_template('movieDashboard.html')


@user_bp.get('/notification')
@auth.loginRequiredPage
def notifPage(**kwargs):
    return render_template('notif.html')


@user_bp.get('/review/<id>/')
@auth.loginRequiredPage
def reviewDvd(**kwargs):
    id=kwargs.get('id')
    return render_template('movieReview.html', id=id)


@user_bp.get('/history')
@auth.loginRequiredPage
def rentDvdHistoryPage(**kwargs):
    id=kwargs.get('id')
    return render_template('rentingHistory.html', id=id)

@user_bp.get('/profile')
@auth.loginRequiredPage
def profilePage(**kwargs):
    return render_template('profile.html')


@user_bp.get('/rent/<id>/')
@auth.loginRequiredPage
def rentingMovieDvd(**kwargs):
    id=kwargs.get('id')
    return render_template('movieRenting.html', id=id)


@user_bp.get('/logout')
@auth.loginRequiredPage
def logout(**kwargs):
    auth.logout()
    return redirect(url_for('user_bp.loginPage'))




# ------- api 
@user_bp.post('/login')
def cekLogin():
    return LoginController().login()

@user_bp.post('/api/register')
def registerUser(**kwargs):
    return RegisterController.insertUser()


# ---------- user
@user_bp.get('/api/movies')
@auth.loginRequiredApi
def getDvds():
    return MovieDvdsController.getMovieDvds()


@user_bp.post('/api/review/movie')
@auth.loginRequiredApi
def insertReview(**kwargs):
    return DvdReviewController.insertReview()


@user_bp.get('/api/review/movie/<id>')
@auth.loginRequiredApi
def reviewPage(**kwargs):
    id=kwargs.get('id')
    return DvdReviewController.getDvdReviews(id)

# ------------ movie renting
@user_bp.post('/api/movie/rent')
@auth.loginRequiredApi
def rentDvd(**kwargs):
    return RenterController.rentDvd()


@user_bp.post('/api/movie/rent/history')
@auth.loginRequiredApi
def rentDvdHistory(**kwargs):
    return RenterController.getRentHistory()


# -------------notif/alert

@user_bp.post('/api/alert')
@auth.loginRequiredApi
def getAlert(**kwargs):
    return AlertController.getAlerts()

@user_bp.post('/api/alert/count')
@auth.loginRequiredApi
def getAlertCount(**kwargs):
    return AlertController.getAlertCount()

# ---------- invoices

@user_bp.post('/api/rent/invoice')
@auth.loginRequiredApi
def getInvoice(**kwargs):
    return InvoiceController.getInvoice()

@user_bp.post('/api/invoice/upload')
@auth.loginRequiredApi
def uploadPayment():
    return InvoiceController.uploadImage()


@user_bp.post('/api/invoice/validate')
@auth.loginRequiredApi
def validatePayment():
    return InvoiceController.validatePayment()


# ---------- user
@user_bp.post('/api/user/index')
@auth.loginRequiredApi
def getUser():
    return UserController.getUser()

@user_bp.put('/api/user/index')
@auth.loginRequiredApi
def updateUser():
    return UserController.updateUser()
