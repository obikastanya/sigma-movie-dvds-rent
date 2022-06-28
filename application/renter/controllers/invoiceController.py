import os
from flask import request
from werkzeug.utils import secure_filename
from lib.response import Resp
from app import db
from orm.renterInvoices import RenterInvoices, RenterInvoicesSchema


class InvoiceController:

    def getInvoice():
        id=request.json.get('invoiceId')
        data=RenterInvoices.query.filter(RenterInvoices.ri_status_bayar=='N',RenterInvoices.ri_id==id ).all()
        jsonData=RenterInvoicesSchema(many=True).dump(data)
        resp=Resp.make(data=jsonData,status=True)
        return resp
    
    def uploadImage():
        try:
            file = request.files['file']
            file.save(os.path.join('static/file_storage/payment', secure_filename(file.filename)))
            return Resp.make(status=True, message='Upload Success', data=[{'filename':'static/file_storage/payment/'+secure_filename(file.filename)}])
        except:
            return Resp.make(message='Upload fail')

    def validatePayment():
        try:
            invoiceId=request.json.get('invoiceId')
            invoice=RenterInvoices.query.filter_by(ri_id=invoiceId).first()
            invoice.ri_bukti_bayar=request.json.get('paymentImagePath')
            invoice.ri_transaction_date=request.json.get('transactionDate')
            db.session.commit()
            return Resp.make(status=True, message='Payment receipt has been Uploaded')
        except:
            return Resp.make(message='Upload failed')


