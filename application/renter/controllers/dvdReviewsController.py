from curses import raw
from flask import request, session
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from app import db
from orm.movieDvds import MovieDvds, MovieDvdsSchema
from orm.movieReviews import MovieReviews, MovieReviewsUserSchema


class DvdReviewController:

    def getDvdReviews(id):
        movie=MovieDvds.query.filter_by(mvd_id=id).first()
        reviews=MovieReviews.query.filter(MovieReviews.mr_mvd_id==id, MovieReviews.mr_active_status=='Y').all()
        jsonMovie=MovieDvdsSchema().dump(movie)
        jsonReviews=MovieReviewsUserSchema(many=True).dump(reviews)
        resp=Resp.make(data=jsonReviews,status=True)
        resp.update({'movieData':jsonMovie})
        return resp

    
    def insertReview():
        try:
            parameter=ParameterHandler.getInsertParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            newAdmin=MovieReviews(**parameter)
            db.session.add(newAdmin)
            db.session.commit()
            return Resp.withoutData(status=True, message='Review has been submitted')
        except:
            return Resp.withoutData(status=True, message='Failed to submit review')

    
    
class ParameterHandler:
    def getInsertParameter():
        rawData=request.json
        return {
            'mr_mvd_id' : rawData.get('movieId'),
            'mr_msu_id' : session.get('user_id'),
            'mr_desc' : rawData.get('desc'),
            'mr_rate': rawData.get('rate'),
            'mr_active_status':'Y'
        }