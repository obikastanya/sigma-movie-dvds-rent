from flask import request
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


    def deleteDvdReviews():
        try:
            parameter=ParameterHandler.getDeleteParameter()
            if not ParameterValidation.cantBeEmpty(parameter):
                return Resp.withoutData('Invalid parameter.')
            
            review=MovieReviews.query.filter_by(mr_msu_id=parameter.get('mr_msu_id'), mr_mvd_id=parameter.get('mr_mvd_id')).first()
            if not review:
                return Resp.withoutData('Review is not found')
            review.mr_active_status='N'
            db.session.commit()
            return Resp.withoutData(status=True, message='Review has been deleted')
        except:
            return Resp.withoutData(status=True, message='Delete Failed')


class ParameterHandler:
    def getDeleteParameter():
        return {
            'mr_mvd_id':request.json.get('movieId'),
            'mr_msu_id':request.json.get('userId')
        }

    
    