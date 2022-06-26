from flask import Blueprint, render_template,session, redirect, url_for
from .controllers.adminController import AdminController
from .controllers.movieDvdsController import MovieDvdsController
from .controllers.userController import UserController
from .controllers.loginController import LoginController, pullNotif

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

@admin_bp.get('/home')
@auth.loginRequiredPage
def homePage(**kwargs):
    return render_template('dvdRenter.html')

@admin_bp.get('/dvd-renter')
@auth.loginRequiredPage
def dvdRentPage(**kwargs):
    return render_template('dvdRenter.html')


@admin_bp.get('/logout')
@auth.loginRequiredPage
def logout(**kwargs):
    session.clear()
    return redirect(url_for('admin_bp.loginPage'))



# api
# ---login

@admin_bp.post('/login')
def cekLogin():
    return LoginController().login()


# --- admin
@admin_bp.get('/index')
def getAdmins():
    return AdminController.getAdmins()

@admin_bp.post('/index')
def insertAdmin():
    return AdminController.insertAdmin()

@admin_bp.put('/index')
def updateAdmin():
    return AdminController.updateAdmin()

@admin_bp.delete('/index')
def softDeleteAdmin():
    return AdminController.softDeleteAdmin()

# --- user
@admin_bp.get('/user')
def getUsers():
    UserController.banUser()

@admin_bp.put('/user/ban')
def banUser():
    pass

@admin_bp.put('/user/ban-release')
def releaseUserBan():
    pass

# --- movie dvds

@admin_bp.get('/dvd')
def getDvds():
    return MovieDvdsController.getMovieDvds()

@admin_bp.get('/dvd/<id>')
def getDvd(id):
    return MovieDvdsController.getMovieDvd(id)

@admin_bp.put('/dvd')
def updateDvd():
    return MovieDvdsController.updateMovieDvd()

@admin_bp.delete('/dvd')
def softDeleteDvd():
        return MovieDvdsController.softDeleteMovieDvd()

@admin_bp.post('/dvd')
def insertDvd():
    return MovieDvdsController.insertMovieDvd()


@admin_bp.post('/dvd/upload')
def uploadImageDvd():
    return MovieDvdsController.uploadImage()



# mail


