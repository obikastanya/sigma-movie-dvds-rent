from app import db
from marshmallow import fields, Schema

class MovieRenterDetail(db.Model):
    __tablename__='movie_renter_detail'
    mrtd_mvd_id =db.Column(db.Integer(), db.ForeignKey('ms_movie_dvds.mvd_id'), primary_key=True,nullable=False)
    mrtd_mrth_id =db.Column(db.Integer(), db.ForeignKey('movie_renter_head.mrth_id'), primary_key=True, nullable=False)
    mrtd_create_date  = db.Column(db.Date())
    mrtd_create_user = db.Column(db.String(30))
    mrtd_update_date = db.Column(db.Date())
    mrtd_update_user = db.Column(db.String(30))

class MovieRenterDetailSchema(Schema):
    movie_dvds_movie_returned_detail=fields.Nested('MovieDvdsSchema', only=('mvd_id', 'mvd_desc'), data_key='movie')