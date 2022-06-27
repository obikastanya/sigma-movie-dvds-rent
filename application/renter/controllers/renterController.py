from datetime import date, datetime, timedelta
from flask import request
from lib.response import Resp
from orm.movieRenterHead import MovieRenterHead
from orm.movieRenterDetail import MovieRenterDetail
from orm.renterInvoices import RenterInvoices
from orm.movieDvds import MovieDvds

from app import db


class RenterController:
    def rentDvd():
        # try:
            parameter=ParameterHandler.getInsertRentingParam()
            newRenterHead=MovieRenterHead(**parameter.get('head'))
            db.session.add(newRenterHead)
            db.session.flush()
            
            detailParameter=parameter.get('detail')
            detailParameter.update({"mrtd_mrth_id":newRenterHead.mrth_id})
            newRenterDetail=MovieRenterDetail(**detailParameter)
            db.session.add(newRenterDetail)
            db.session.flush()

            nominal=RenterController.getNominal()
            invoicesParameter=parameter.get('invoices')
            invoicesParameter.update({"ri_mrth_id":newRenterHead.mrth_id})
            invoicesParameter.update({"ri_nominal":nominal})
            newRenterInvoices=RenterInvoices(**invoicesParameter)
            db.session.add(newRenterInvoices)
            db.session.flush()
            
            dueDate=date.today() + timedelta(days=1)
            dueDate=dueDate.strftime('%d-%m-%Y 23:59')
            returnedData={
                "invoicesId":newRenterInvoices.ri_id,
                "nominal":nominal,
                "payment_due":dueDate,
                'bank':'038922198572 (BCA)'
            }
            db.session.commit()
            return Resp.make(status=True, message="Transaction Success", data=[returnedData])

        # except:
        #     return Resp.make(status=True, message="Transaction Failed")

    def getNominal():
        movieId=request.json.get("movieId")
        movie=MovieDvds.query.filter_by(mvd_id=movieId).first()
        startDate=request.json.get("startDate")
        endDate=request.json.get("endDate")
        datetimeStartDate = datetime.strptime(startDate, '%Y-%m-%d')
        datetimeEndDate = datetime.strptime(endDate, '%Y-%m-%d')
        duration=datetimeEndDate-datetimeStartDate
        if duration.days <0:
            raise  "Invalid date"
        price =movie.mvd_price
        if not price:
            price=0
        return duration.days*price



class ParameterHandler:
    def getInsertRentingParam():
        rawData=request.json
        return {
            "head":{
            "mrth_msu_id":rawData.get("userId"),
            "mrth_rent_start_date":rawData.get("startDate"),
            "mrth_rent_due_date":rawData.get("endDate"),
            "mrth_shipping_destination":rawData.get("address")},
            "detail":{
                "mrtd_mvd_id":rawData.get("movieId"),
                "mrtd_mrth_id":""
            },
            "invoices":{
                "ri_mrth_id":"",
                "ri_status_bayar":"N"
            }

        }

    


