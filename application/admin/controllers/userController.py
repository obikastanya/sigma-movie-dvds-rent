import datetime
from flask import request
from sqlalchemy import func
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from app import db


from orm.user import User, UserSchema
from orm.userOnBan import UserOnBan

class UserController:
    def getUsers():
        isExistFilter, filter=UserController.getFilter()
        data=None
        if isExistFilter:
            data=User.query.filter(*filter).all()
        else:
            data=User.query.all()
        jsonData=UserSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    
        
    def banUser():
        try:
            parameter=UserParameterHandler.getBannParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            
            user=User.query.filter_by(msu_id=parameter.get('msu_id')).first()
            if not user:
                return Resp.withoutData('User is not found')

            user.msu_banned_status='B'
            parameter.pop('msu_id',None)
            newUserOnBann=UserOnBan(**parameter)
            db.session.add(newUserOnBann)
            db.session.commit()
            return Resp.withoutData(status=True, message='Banned success')
        except:
            return Resp.withoutData(message='Failed to Ban')


    def releaseUserBan():
        try:
            parameter=UserParameterHandler.getReleaseParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            
            user=User.query.filter_by(msu_id=parameter.get('msu_id')).first()
            if not user:
                return Resp.withoutData('User is not found')

            user.msu_banned_status='R'
    
            userOnBann=UserOnBan.query.filter(UserOnBan.uob_msu_id==parameter.get('uob_msu_id'), UserOnBan.uob_release_date == None ).first()

            userOnBann.uob_release_date=datetime.datetime.now()
            db.session.commit()
            return Resp.withoutData(status=True, message='Release success')
        except:
            return Resp.withoutData(message='Failed to Release User Ban')


    def getFilter():
        parameter={'email':request.args.get('email'),'name':request.args.get('name'),}
        # saved the query statement inside list so we can append and make it more dynamic,
        # then parse them to tuple since its the alchemy requirement
        groupOfFilterStatement=[]
        if parameter.get('email'):
            groupOfFilterStatement.append(*(func.lower(User.msu_email)==func.lower(parameter.get('email')),))
        if parameter.get('name'):
            groupOfFilterStatement.append(*(func.lower(User.msu_name)==func.lower(parameter.get('name')),))
        return True,tuple(groupOfFilterStatement)



class UserParameterHandler:
    def getBannParameter():
        return {
            'msu_id':request.json.get('id'),
            'uob_msu_id':request.json.get('id'),
            'uob_desc': request.json.get("desc"),
            'uob_banned_date': datetime.datetime.now()
        
        }
    def getReleaseParameter():
        return {
            'msu_id':request.json.get('id'),
            'uob_msu_id':request.json.get('id')
        }
