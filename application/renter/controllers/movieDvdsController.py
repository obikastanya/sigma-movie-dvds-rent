import os
from lib.response import Resp
from app import db
from orm.movieDvds import MovieDvds, MovieDvdsSchema


class MovieDvdsController:

    def getMovieDvds():
        data=MovieDvds.query.filter(MovieDvds.mvd_on_air_status=='Y',MovieDvds.mvd_active_status=='Y' ).all()
        jsonData=MovieDvdsSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp

    
    def getMovieDvd(id):
        data=MovieDvds.query.filter_by(mvd_id=id).first()
        if not data:
            return Resp.make(status=False, message='Movie is not found')
        jsonData=MovieDvdsSchema(many=True).dump([data])
        return Resp.make(status=True, data=jsonData)


