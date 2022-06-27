from app import db
from marshmallow import Schema, fields

class RenterInvoices(db.Model):
    __tablename__='renter_invoices'
    ri_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    ri_mrth_id =db.Column(db.ForeignKey('movie_renter_head.mrth_id'), nullable=False)
    ri_nominal =db.Column(db.Integer(), nullable=False)
    ri_status_bayar =db.Column(db.String(1), nullable=False)
    ri_bukti_bayar  = db.Column(db.String(200))
    ri_transaction_date = db.Column(db.Date())
    ri_transaction_validation_date = db.Column(db.Date())
    ri_create_date  = db.Column(db.Date())
    ri_create_user = db.Column(db.String(30))
    ri_update_date = db.Column(db.Date())
    ri_update_user = db.Column(db.String(30))

class RenterInvoicesSchema(Schema):
    ri_id = fields.Int(data_key='id')
    ri_mrth_id=fields.Int(data_key='transaction_id')
    ri_nominal =fields.Int(data_key='nominal')

class RenterInvoicesFullSchema(Schema):
    ri_id = fields.Int(data_key='id')
    ri_mrth_id=fields.Int(data_key='transaction_id')
    ri_nominal =fields.Int(data_key='nominal')
    ri_status_bayar =fields.Str(data_key='payment_status')
    ri_bukti_bayar=fields.Str(data_key='payment_receipt')
    ri_transaction_date = fields.Date(data_key='transaction_date')
    ri_transaction_validation_date = fields.Date(data_key='validation_date')
    movie_renter_head_renter_invoices=fields.Nested('MovieRenterHeadSchema', data_key='transaction')
    
    