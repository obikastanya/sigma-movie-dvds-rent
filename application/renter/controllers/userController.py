from flask import request
from lib.response import Resp
from app import db
from orm.user import User, UserSchema
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
import bcrypt


class UserController:
    def getUser():
        id=request.json.get('userId')
        data=User.query.filter_by(msu_id=id).all()
        jsonData=UserSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    
    def updateUser():
        parameter=ParameterHandler.getUpdateParameter()
        id=parameter.get('msu_id')
        user=User.query.filter_by(msu_id=id).first()
        if not user:
            return  Resp.make('User is not found')
        if  not bcrypt.checkpw(parameter.get('old_password').encode('utf-8'), user.msu_password.encode('utf-8')):
            return  Resp.make('Incorrect Password')
        if request.json.get('newPassword'):
           user.msu_password=parameter.get('msu_password')
        
        user.msu_address=parameter.get('msu_address') 
        user.msu_email=parameter.get('msu_email') 
        user.msu_name=parameter.get('msu_name') 
        user.msu_gender=parameter.get('msu_gender') 
        db.session.commit()
        return Resp.make(status=True, message='User data successfully updated')
        
class ParameterHandler:
    def getUpdateParameter():
        hashedPassword=bcrypt.hashpw(request.json.get('newPassword').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        rawData=request.json
        return {
        'msu_id':rawData.get('userId'),
        'msu_address':rawData.get('address'),
        'msu_birth_date':rawData.get('birth_date'),
        'msu_email':rawData.get('email'),
        'msu_name':rawData.get('name'),
        'msu_gender':rawData.get('gender'),
        'msu_address':rawData.get('address'),
        'msu_password':hashedPassword,
        'old_password':rawData.get('password')
        }
        