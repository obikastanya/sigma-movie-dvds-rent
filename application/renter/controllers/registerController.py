from flask import request
from sqlalchemy import func
import bcrypt
from orm.user import User, UserSchema
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from app import db


class RegisterController:

    def insertUser():
        try:
            parameter=ParameterHandler.getInsertParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            newUser=User(**parameter)
            db.session.add(newUser)
            db.session.commit()
            return Resp.withoutData(status=True, message='User succesfully registered')
        except:
            return Resp.withoutData(message='Register Failed')

class ParameterHandler:
    def getInsertParameter():
        hashedPassword=bcrypt.hashpw(request.json.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        rawData=request.json
        return {
        'msu_address':rawData.get('address'),
        'msu_birth_date':rawData.get('birth_date'),
        'msu_email':rawData.get('email'),
        'msu_name':rawData.get('name'),
        'msu_gender':rawData.get('gender'),
        'msu_address':rawData.get('address'),
        'msu_password':hashedPassword
        }

    def getUpdateParameter():
        parameter= {
            'msa_id':request.json.get('id'),
            'msa_email':request.json.get('email'),
            'msa_name':request.json.get('name'),
            'msa_active_status': request.json.get('active_status',"Y"),
              
        }
        if(request.json.get('password')):
            hashedPassword=bcrypt.hashpw(request.json.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            parameter.update({'msa_password':hashedPassword})
        return parameter 
        
    
    