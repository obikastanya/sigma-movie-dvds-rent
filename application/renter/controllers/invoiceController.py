import os

from flask import request
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

