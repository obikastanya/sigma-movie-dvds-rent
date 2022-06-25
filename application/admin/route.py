import re
from flask import Blueprint, render_template
from .controllers.adminController import AdminController
from .controllers.movieDvdsController import MovieDvdsController
from .controllers.userController import UserController

admin_bp=Blueprint(
    'admin_bp', 
    __name__, 
    template_folder='templates', 
    static_folder='static')

# route
@admin_bp.get('/')
def home():
    return render_template('admHome.html')


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


