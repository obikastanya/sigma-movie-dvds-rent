import os
from flask import request
from sqlalchemy import func
from werkzeug.utils import secure_filename
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from app import db
from orm.movieDvds import MovieDvds, MovieDvdsSchema


class MovieDvdsController:

    def getMovieDvds():
        isExistFilter, filter=MovieDvdsController.getFilter()
        data=None
        if isExistFilter:
            data=MovieDvds.query.filter(*filter).all()
        else:
            data=MovieDvds.query.all()
        jsonData=MovieDvdsSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp

    
    def getMovieDvd(id):
        data=MovieDvds.query.filter_by(mvd_id=id).first()
        if not data:
            return Resp.make(status=False, message='Movie is not found')
        jsonData=MovieDvdsSchema(many=True).dump([data])
        return Resp.make(status=True, data=jsonData)


    def insertMovieDvd():
        try:
            parameter=MovieDvdsParameterHandler.getInsertParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            newMovieDvd=MovieDvds(**parameter)
            db.session.add(newMovieDvd)
            db.session.commit()
            return Resp.withoutData(status=True, message='Movie succesfully added')
        except:
            return Resp.withoutData(status=True, message='Insert Failed')


    def updateMovieDvd():
        try:
            parameter=MovieDvdsParameterHandler.getUpdateParameter()
            if not ParameterValidation.certainKeyShouldExist(['mvd_id'],parameter):
                return Resp.withoutData('Invalid parameter.')
            
            movie=MovieDvds.query.filter_by(mvd_id=parameter.get('mvd_id')).first()
            if not movie:
                return Resp.withoutData('Movie is not found')
                    
            movie.mvd_title =parameter.get('mvd_title')
            movie.mvd_desc =parameter.get('mvd_desc')
            movie.mvd_release_date = parameter.get('mvd_release_date')
            movie.mvd_age_certification =parameter.get('mvd_age_certification')
            movie.mvd_genre =parameter.get('mvd_genre')
            movie.mvd_total_dvds =parameter.get('mvd_total_dvds')
            movie.mvd_available_stock =parameter.get('mvd_available_stock')
            movie.mvd_image_path =parameter.get('mvd_image_path')
            movie.mvd_active_status =parameter.get('mvd_active_status')
            db.session.commit()
            return Resp.withoutData(status=True, message='Movie succesfully updated')
        except:
            return Resp.withoutData(status=True, message='Update Failed')


    def softDeleteMovieDvd():
        try:
            parameter=MovieDvdsParameterHandler.getDeleteParameter()
            if not ParameterValidation.certainKeyShouldExist(['mvd_id'],parameter):
                return Resp.withoutData('Invalid parameter.')
            
            movie=MovieDvds.query.filter_by(mvd_id=parameter.get('mvd_id')).first()
            if not movie:
                return Resp.withoutData('Movie is not found')
            movie.mvd_active_status =parameter.get('mvd_active_status')
            db.session.commit()
            return Resp.withoutData(status=True, message='Movie succesfully deleted')
        except:
            return Resp.withoutData(status=True, message='Delete Failed')
    
    def uploadImage():
        try:
            file = request.files['file']
            file.save(os.path.join('static/file_storage', secure_filename(file.filename)))
            return Resp.make(status=True, message='Upload Success', data=[{'filename':'static/file_storage/'+file.filename}])
        except:
            Resp.make(message='Upload fail')

    def getFilter():
        parameter={'id':request.args.get('id'),'title':request.args.get('title')}
        if not ParameterValidation.atLeastOneNotEmpty(parameter):
            return False,(None,)
        # saved the query statement inside list so we can append and make it more dynamic,
        # then parse them to tuple since its the alchemy requirement
        groupOfFilterStatement=[]
        if parameter.get('id'):
            groupOfFilterStatement.append(*(MovieDvds.mvd_id==int(parameter.get('id')),))
        if parameter.get('title'):
            groupOfFilterStatement.append(*(func.lower(MovieDvds.mvd_title)==func.lower(parameter.get('title')),))
        return True,tuple(groupOfFilterStatement)

class MovieDvdsParameterHandler:
    def getInsertParameter():
        rawData=request.json
        return {
        'mvd_title' :rawData.get('title'),
        'mvd_desc'  :rawData.get('desc'),
        'mvd_release_date':rawData.get('release_date'),
        'mvd_age_certification':rawData.get('age_certification'), 
        'mvd_genre':rawData.get('genre'),
        'mvd_total_dvds':rawData.get('total_dvds'),
        'mvd_available_stock':rawData.get('available_stock'),
        'mvd_image_path':rawData.get('image_path'),
        'mvd_active_status':'Y'
        }
    def getUpdateParameter():
        rawData=request.json
        return {
        'mvd_id':rawData.get('id'),
        'mvd_title' :rawData.get('title'),
        'mvd_desc'  :rawData.get('desc'),
        'mvd_release_date':rawData.get('release_date'),
        'mvd_age_certification':rawData.get('age_certification'), 
        'mvd_genre':rawData.get('genre'),
        'mvd_total_dvds':rawData.get('total_dvds'),
        'mvd_available_stock':rawData.get('available_stock'),
        'mvd_image_path':rawData.get('image_path'),
        'mvd_active_status':rawData.get('active_status')
        }
    
    def getDeleteParameter():
        return{
            'mvd_id':request.json.get('id'),
            'mvd_active_status': 'N'  
        }
