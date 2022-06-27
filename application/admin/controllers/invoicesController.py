from datetime import date
import os
from flask import request
from werkzeug.utils import secure_filename
from lib.response import Resp
from app import db
from orm.renterInvoices import RenterInvoices, RenterInvoicesFullSchema


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
            db.session.commit()
            return Resp.make(status=True, message='Payment receipt has been validated')
        except:
            return Resp.make(message='Validate failed')
