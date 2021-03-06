from datetime import date
import os
from flask import request
from werkzeug.utils import secure_filename
from lib.response import Resp
from app import db
from orm.renterInvoices import RenterInvoices, RenterInvoicesFullSchema
from orm.movieRenterHead import MovieRenterHead
from orm.movieRenterDetail import MovieRenterDetail
from orm.movieDvds import MovieDvds
from orm.alert import Alert


class InvoiceController:

    def getInvoices():
        data=RenterInvoices.query.filter(RenterInvoices.ri_status_bayar=='N',RenterInvoices.ri_transaction_date != None ).all()
        jsonData=RenterInvoicesFullSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    
    def validatePayment():
        try:
            invoiceId=request.json.get('id')
            invoice=RenterInvoices.query.filter_by(ri_id=invoiceId).first()
            invoice.ri_transaction_validation_date=date.today()
            invoice.ri_status_bayar='Y'

            headTransaction=MovieRenterHead.query.filter_by(mrth_id=invoice.ri_mrth_id).first()
            alertParameter={
                'al_msu_id':headTransaction.mrth_msu_id,
                'al_desc':'Your payment (invoice id: '+invoiceId+') has been validated by admin. We will send the dvd to your place.',
                'al_read_status':'N',
                'al_title':'Payment Validated'
                }
            newAlert=Alert(**alertParameter)
            db.session.add(newAlert)
            InvoiceController.recalculateStock(headTransaction.mrth_id)
            db.session.commit()
            return Resp.make(status=True, message='Payment receipt has been validated')
        except:
            return Resp.make(message='Validate failed')
    
    def recalculateStock(transaction_id):
        detailTransaction=MovieRenterDetail.query.filter_by(mrtd_mrth_id=transaction_id).first()
        if not detailTransaction:
            raise 'Detail transaction is not found'
        movie=MovieDvds.query.filter_by(mvd_id=detailTransaction.mrtd_mvd_id).first()
        if not movie:
            raise 'Detail movie is not found'
        if movie.mvd_available_stock<1:
            raise 'Movie out of stock'
        
        movie.mvd_available_stock=movie.mvd_available_stock-1


