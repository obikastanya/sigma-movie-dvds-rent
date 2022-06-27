from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from orm.movieRenterHead import MovieRenterHead,MovieRenterHeadSchema
from app import db


class RenterHeadController:

    def getRenters():
        data=QueryModel.getRenters()
        jsonData=Resp.map(['user_id','name','rent_start_date', 'rent_due_date','rent_duration', 'shipping_destination', 'movie', 'due_status' ],data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    


class QueryModel:
    def getRenters():
        query="""
        select msu_id, msu_name, mrth_rent_start_date, mrth_rent_due_date,mrth_rent_duration, 
        mrth_shipping_destination, array_agg( array[mvd_id||'', mvd_title]), 
        case 
        when mrth_rent_due_date is not NULL and mrth_rent_due_date>=now()  then 'Y' else 'N' end  from movie_renter_head, 
        movie_renter_detail, ms_movie_dvds,  ms_user
        where mrth_msu_id =msu_id and mrtd_mrth_id=mrth_id and mvd_id=mrtd_mvd_id 
        group by msu_id,msu_id, msu_name, mrth_rent_start_date, mrth_rent_due_date,mrth_rent_duration, mrth_shipping_destination
        """
        return db.session.execute(query).all()
    


