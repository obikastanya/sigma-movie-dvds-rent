from flask import Blueprint, render_template
from .controllers.adminController import AdminController
from .controllers.movieDvdsController import MovieDvdsController
from .controllers.userController import UserController
from .controllers.loginController import LoginController

admin_bp=Blueprint(
    'admin_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static')

# route
@admin_bp.get('/login')
def loginPage():
    return render_template('loginAdmin.html')

@admin_bp.get('/home')
def homePage():
    return render_template('homeAdmin.html')


@admin_bp.post('/login')
def cekLogin():
    return LoginController.login()


# api
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

# mail


