from flask import request
from lib.response import Resp
from app import db
from orm.user import User, UserSchema

class UserController:
    def getUser():
        id=request.json.get('userId')
        data=User.query.filter_by(msu_id=id).all()
        jsonData=UserSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    
        