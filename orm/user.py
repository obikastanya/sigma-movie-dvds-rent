from app import db
from marshmallow import fields, Schema


class User(db.Model):
    __tablename__='ms_user'

    msu_id =db.Column(db.Integer(), primary_key=True)
    msu_email = db.Column(db.String(50), unique=True, nullable=False)
    msu_password = db.Column(db.String(100), nullable=False)
    msu_name = db.Column(db.String(100), nullable=False)
    msu_address =db.Column(db.String(200), nullable=False)
    msu_gender = db.Column(db.String(1), nullable=False)
    msu_birth_date = db.Column(db.Date(), nullable=False)
    msu_banned_status =db.Column(db.String(1))
    msu_create_date  = db.Column(db.Date())
    msu_create_user = db.Column(db.String(30))
    msu_update_date = db.Column(db.Date())
    msu_update_user = db.Column(db.String(30))
    
    # relation with user
    user_user_on_ban=db.relationship('UserOnBan', backref='user_user_on_ban')
    user_movie_reviews=db.relationship('MovieReviews', backref='user_movie_reviews')
    user_movie_renter_head=db.relationship('MovieRenterHead', backref='user_movie_renter_head')
    

class UserSchema(Schema):
    msu_id =fields.Int(data_key='id')
    msu_email = fields.Str(data_key='email')
    msu_name = fields.Str(data_key='name')
    msu_gender = fields.Str(data_key='gender')
    msu_birth_date = fields.Str(data_key='birth_date')
    msu_address =fields.Str(data_key='address')
    msu_banned_status=fields.Str(data_key='banned_status')

