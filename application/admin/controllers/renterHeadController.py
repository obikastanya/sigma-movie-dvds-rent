from flask import request
from lib.response import Resp
from lib.parameterValidation import ParameterValidation
from orm.alert import Alert
from orm.movieRenterHead import MovieRenterHead, MovieRenterHeadSchema
from orm.movieRenterDetail import MovieRenterDetail

from app import db


class RenterHeadController:

    def getRenters():
        data=QueryModel.getRenters()
        jsonData=Resp.map(['transaction_id','user_id','name','rent_start_date', 'rent_due_date','rent_duration', 'shipping_destination', 'movie', 'due_status' ],data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    
    def alert():
        try:
            parameter={
                'al_msu_id':request.json.get('userId'),
                'al_desc':request.json.get('message'),
                'al_read_status':'N',
                'al_title':'Reminder'
                }
            newAlert=Alert(**parameter)
            db.session.add(newAlert)
            db.session.commit()
            resp=Resp.withoutData(status=True, message='Alert has been sended')
        except:
            resp=Resp.withoutData(message='Alert failed')    
        return resp
            
    

class QueryModel:
    def getRenters():
        query="""
        select mrth_id,msu_id, msu_name, mrth_rent_start_date, mrth_rent_due_date,mrth_rent_duration, 
        mrth_shipping_destination, array_agg( array[mvd_id||'', mvd_title]), 
        case 
        when mrth_rent_due_date is not NULL and mrth_rent_due_date<=now()  then 'Y' else 'N' end  from movie_renter_head, 
        movie_renter_detail, ms_movie_dvds,  ms_user, renter_invoices
        where mrth_msu_id =msu_id and mrtd_mrth_id=mrth_id and mvd_id=mrtd_mvd_id and 
        ri_mrth_id= mrth_id and ri_status_bayar='Y'
        group by mrth_id,msu_id,msu_id, msu_name, mrth_rent_start_date, mrth_rent_due_date,mrth_rent_duration, mrth_shipping_destination"""
        return db.session.execute(query).all()
    


