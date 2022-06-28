from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from config import Config


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://{user}:{password}@{host}:{port}/{database}'.format(
    user=Config.user,
    host=Config.host,
    password=Config.password,
    database=Config.database,
    port=Config.port,
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key= Config.appSecretKey
app.config['SESSION_COOKIE_HTTPONLY']=False
app.config['SESSION_COOKIE_NAME']='sigma_movie'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=60)

db= SQLAlchemy(app)
migrate=Migrate(app,db)

