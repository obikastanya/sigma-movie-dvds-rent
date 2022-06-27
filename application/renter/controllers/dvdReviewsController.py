from flask import request
from lib.response import Resp
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
    
    