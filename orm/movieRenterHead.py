from app import db
from marshmallow import fields, Schema

class MovieRenterHead(db.Model):
    __tablename__='movie_renter_head'
    mrth_id =db.Column(db.Integer(),  primary_key=True,nullable=False)
    mrth_msu_id =db.Column(db.Integer(), db.ForeignKey('ms_user.msu_id'), nullable=False)
    mrth_rent_start_date =db.Column(db.Date(),  nullable=False)
    mrth_rent_due_date =db.Column(db.Date(), nullable=False)
    mrth_rent_duration =db.Column(db.Integer())
    mrth_shipping_destination =db.Column(db.String(500), nullable=False)
    mrth_create_date  = db.Column(db.Date())
    mrth_create_user = db.Column(db.String(30))
    mrth_update_date = db.Column(db.Date())
    mrth_update_user = db.Column(db.String(30))

    movie_renter_head_dvd_shipment=db.relationship('DvdsShipment', backref='movie_renter_head_dvd_shipment')
    movie_renter_head_movie_renter_detail=db.relationship('MovieRenterDetail', backref='movie_renter_head_movie_renter_detail')
    movie_renter_head_renter_invoices=db.relationship('RenterInvoices', backref='movie_renter_head_renter_invoices')


class MovieRenterHeadSchema(Schema):
    mrth_id =fields.Int(data_key='id')
    mrth_rent_start_date = fields.Date(data_key='rent_start_date')
    mrth_rent_due_date = fields.Date(data_key='rent_due_date')
    mrth_shipping_destination =fields.Str(data_key='shipping_destination')
    user_movie_renter_head=fields.Nested('UserSchema', only=('msu_id', 'msu_name'), data_key='user')
    
