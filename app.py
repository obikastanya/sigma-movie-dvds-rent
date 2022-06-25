from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
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

db= SQLAlchemy(app)
migrate=Migrate(app,db)

