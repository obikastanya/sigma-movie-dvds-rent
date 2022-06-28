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
@auth.loginRequiredApi
def getUsers():
    return UserController.getUsers()

@admin_bp.post('/api/user/ban')
@auth.loginRequiredApi
def banUser():
    return UserController.banUser()

@admin_bp.post('/api/user/release')
@auth.loginRequiredApi
def releaseUser():
    return UserController.releaseUserBan()



# ---------------- admin

@admin_bp.get('/api/index')
@auth.loginRequiredApi
def getAdmins():
    return AdminController.getAdmins()

@admin_bp.post('/api/index')
@auth.loginRequiredApi
def insertAdmin():
    return AdminController.insertAdmin()

@admin_bp.put('/api/index')
@auth.loginRequiredApi
def updateAdmin():
    return AdminController.updateAdmin()

@admin_bp.delete('/api/index')
@auth.loginRequiredApi
def softDeleteAdmin():
    return AdminController.softDeleteAdmin()

@admin_bp.get('/api/index/<id>')
@auth.loginRequiredApi
def getAdmin(**kwargs):
    id=kwargs.get('id')
    return AdminController.getAdmin(id)


#------------- movie dvd
@admin_bp.get('/api/movie')
@auth.loginRequiredApi
def getDvds():
    return MovieDvdsController.getMovieDvds()

@admin_bp.put('/api/movie')
@auth.loginRequiredApi
def updateDvd():
    return MovieDvdsController.updateMovieDvd()

@admin_bp.delete('/api/movie')
@auth.loginRequiredApi
def softDeleteDvd():
    return MovieDvdsController.softDeleteMovieDvd()

@admin_bp.post('/api/movie')
@auth.loginRequiredApi
def insertDvd():
    return MovieDvdsController.insertMovieDvd()

@admin_bp.get('/api/movie/<id>/')
@auth.loginRequiredApi
def getDvd(**kwargs):
    id=kwargs.get('id')
    return MovieDvdsController.getMovieDvd(id)


@admin_bp.post('/api/movie/upload')
@auth.loginRequiredApi
def uploadImageDvd():
    return MovieDvdsController.uploadImage()


# ----------------- invoices

@admin_bp.get('/api/invoices')
@auth.loginRequiredApi
def getInvoices(**kwargs):
    return InvoiceController.getInvoices()

@admin_bp.post('/api/invoices/validate')
@auth.loginRequiredApi
def validateInvoice(**kwargs):
    return InvoiceController.validatePayment()


# ----------------- login
@admin_bp.post('/api/login')
def cekLogin():
    return LoginController().login()

# ------------------ reviews

@admin_bp.delete('/api/review')
@auth.loginRequiredApi
def deleteDvdReviews():
    return DvdReviewController.deleteDvdReviews()

@admin_bp.get('/api/review/<id>')
@auth.loginRequiredApi
def getDvdReviews(id):
    return DvdReviewController.getDvdReviews(id)


# ----------- renter
@admin_bp.get('/api/renter')
@auth.loginRequiredApi
def getRenters():
    return RenterHeadController.getRenters()

@admin_bp.post('/api/renter/alert')
@auth.loginRequiredApi
def alertRenters():
    return RenterHeadController.alert()

