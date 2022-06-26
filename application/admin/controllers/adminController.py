from flask import request
from sqlalchemy import func
import bcrypt
from orm.admin import Admin, AdminSchema
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from app import db


class AdminController:

    def getAdmins():
        isExistFilter, filter=AdminController.getFilter()
        data=None
        if isExistFilter:
            data=Admin.query.filter(*filter).all()
        else:
            data=Admin.query.all()
        jsonData=AdminSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp

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
    
    def getFilter():
        parameter={'email':request.args.get('email'),'name':request.args.get('name'),}
        # saved the query statement inside list so we can append and make it more dynamic,
        # then parse them to tuple since its the alchemy requirement
        groupOfFilterStatement=[*(Admin.msa_active_status=='Y',)]
        if parameter.get('email'):
            groupOfFilterStatement.append(*(func.lower(Admin.msa_email)==func.lower(parameter.get('email')),))
        if parameter.get('name'):
            groupOfFilterStatement.append(*(func.lower(Admin.msa_name)==func.lower(parameter.get('name')),))
        return True,tuple(groupOfFilterStatement)


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
