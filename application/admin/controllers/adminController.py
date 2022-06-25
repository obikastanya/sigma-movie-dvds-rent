from flask import request
import bcrypt
from orm.admin import Admin, AdminSchema
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from app import db


class AdminController:
    def getAdmins():
        data=Admin.query.all()
        jsonData=AdminSchema(many=True).dump(data)
        return Resp.make(status=True, data=jsonData)

    def insertAdmin():
        try:
            parameter=AdminParameterHandler.getInsertParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            newAdmin=Admin(**parameter)
            db.session.add(newAdmin)
            db.session.commit()
            return Resp.withoutData(status=True, message='Admin succesfully added')
        except:
            return Resp.withoutData(status=True, message='Insert Failed')

    def updateAdmin():
        try:
            parameter=AdminParameterHandler.getUpdateParameter()
            if not ParameterValidation.certainKeyShouldExist(['msa_active_status','msa_id'],parameter):
                return Resp.withoutData('Invalid parameter.')
            
            admin=Admin.query.filter_by(msa_id=parameter.get('msa_id')).first()
            if not admin:
                return Resp.withoutData('Admin is not found')
            
            admin.msa_email=parameter.get('msa_email')
            admin.msa_name=parameter.get('msa_name')
            admin.msa_active_status=parameter.get('msa_active_status')
            db.session.commit()
            return Resp.withoutData(status=True, message='Admin succesfully updated')
        except:
            return Resp.withoutData(status=True, message='Update Failed')


    def softDeleteAdmin():
        try:
            parameter=AdminParameterHandler.getUpdateParameter()
            if not ParameterValidation.certainKeyShouldExist(['msa_active_status','msa_id'],parameter):
                return Resp.withoutData('Invalid parameter.')
            
            admin=Admin.query.filter_by(msa_id=parameter.get('msa_id')).first()
            if not admin:
                return Resp.withoutData('Admin is not found')
            admin.msa_active_status=parameter.get('msa_active_status')
            db.session.commit()
            return Resp.withoutData(status=True, message='Admin succesfully deactived')
        except:
            return Resp.withoutData(status=True, message='Failed to deactive admin')



class AdminParameterHandler:
    def getInsertParameter():
        hashedPassword=bcrypt.hashpw(request.json.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return {
            'msa_email':request.json.get('email'),
            'msa_password':hashedPassword, 
            'msa_name':request.json.get('name'),
            'msa_active_status': request.json.get('active_status')  
        }

    def getUpdateParameter():
        return {
            'msa_id':request.json.get('id'),
            'msa_email':request.json.get('email'),
            'msa_name':request.json.get('name'),
            'msa_active_status': request.json.get('active_status')  
        }
    
    def getDeleteParameter():
        return{
            'msa_id':request.json.get('id'),
            'msa_active_status': 'N'  
        }
