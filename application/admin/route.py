from flask import Blueprint, render_template,session, redirect, url_for
from .controllers.adminController import AdminController
from .controllers.movieDvdsController import MovieDvdsController
from .controllers.userController import UserController
from .controllers.loginController import LoginController, pullNotif
from .controllers.dvdReviewsController import DvdReviewController
from .controllers.renterHeadController import RenterHeadController
from .controllers.invoicesController import InvoiceController

admin_bp=Blueprint(
    'admin_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static')

auth=LoginController()

# route
@admin_bp.get('/login')
@auth.noSessionRequiredPage
def loginPage(**kwargs):
    message=pullNotif()    
    return render_template('loginAdmin.html', message=message)

@admin_bp.get('/')
@admin_bp.get('/home')
@admin_bp.get('/dvd-renter')
@auth.loginRequiredPage
def homePage(**kwargs):
    return render_template('dvdRenter.html')

@admin_bp.get('/movies')
@auth.loginRequiredPage
def dvdMasterPage(**kwargs):
    return render_template('dvdMaster.html')


@admin_bp.get('/index')
@auth.loginRequiredPage
def adminMasterPage(**kwargs):
    return render_template('adminMaster.html')

@admin_bp.get('/logout')
@auth.loginRequiredPage
def logout(**kwargs):
    session.clear()
    return redirect(url_for('admin_bp.loginPage'))

@admin_bp.get('/review/<id>')
@auth.loginRequiredPage
def dvdMasterReviewPage(**kwargs):
    id=kwargs.get('id')
    return render_template('dvdMasterReview.html', id=id)

@admin_bp.get('/invoices')
@auth.loginRequiredPage
def invoicesPage(**kwargs):
    return render_template('renterInvoices.html')

@admin_bp.get('/users')
@auth.loginRequiredPage
def userMasterPage(**kwargs):
    return render_template('userMaster.html')



# API
# ----------------- users api

@admin_bp.get('/api/users')
def getUsers():
    return UserController.getUsers()

@admin_bp.post('/api/user/ban')
def banUser():
    return UserController.banUser()

@admin_bp.post('/api/user/release')
def releaseUser():
    return UserController.releaseUserBan()



# ---------------- admin

@admin_bp.get('/api/index')
def getAdmins():
    return AdminController.getAdmins()

@admin_bp.post('/api/index')
def insertAdmin():
    return AdminController.insertAdmin()

@admin_bp.put('/api/index')
def updateAdmin():
    return AdminController.updateAdmin()

@admin_bp.delete('/api/index')
def softDeleteAdmin():
    return AdminController.softDeleteAdmin()

@admin_bp.get('/api/index/<id>')
def getAdmin(id):
    return AdminController.getAdmin(id)


#------------- movie dvd
@admin_bp.get('/api/movie')
def getDvds():
    return MovieDvdsController.getMovieDvds()

@admin_bp.put('/api/movie')
def updateDvd():
    return MovieDvdsController.updateMovieDvd()

@admin_bp.delete('/api/movie')
def softDeleteDvd():
    return MovieDvdsController.softDeleteMovieDvd()

@admin_bp.post('/api/movie')
def insertDvd():
    return MovieDvdsController.insertMovieDvd()

@admin_bp.get('/api/movie/<id>/')
def getDvd(id):
    return MovieDvdsController.getMovieDvd(id)


@admin_bp.post('/api/movie/upload')
def uploadImageDvd():
    return MovieDvdsController.uploadImage()


# ----------------- invoices api

@admin_bp.get('/invoices/data')
# @auth.loginRequiredApi
def getInvoices(**kwargs):
    return InvoiceController.getInvoices()

@admin_bp.post('/invoices/data/validate')
# @auth.loginRequiredApi
def validateInvoice(**kwargs):
    return InvoiceController.validatePayment()

# api
# ---login

@admin_bp.post('/login')
def cekLogin():
    return LoginController().login()


# --- admin
# --- user


# reviews
@admin_bp.get('/dvd/reviews/<id>')
def getDvdReviews(id):
    return DvdReviewController.getDvdReviews(id)

@admin_bp.delete('/dvd/reviews')
def deleteDvdReviews():
    return DvdReviewController.deleteDvdReviews()

# renter
@admin_bp.get('/dvd-renter/data')
def getRenters():
    return RenterHeadController.getRenters()


# renter
@admin_bp.post('/dvd/renter/alert')
def alertRenters():
    return RenterHeadController.alert()


# mail


