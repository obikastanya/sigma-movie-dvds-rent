from app import db
from marshmallow import fields, Schema


class Admin(db.Model):
    __tablename__='ms_admin'

    msa_id =db.Column(db.Integer(), primary_key=True)
    msa_email = db.Column(db.String(50), unique=True, nullable=False)
    msa_password = db.Column(db.String(100), nullable=False)
    msa_name = db.Column(db.String(100), nullable=False)
    msa_active_status =db.Column(db.String(1), nullable=False)
    msa_create_date  = db.Column(db.Date())
    msa_create_user = db.Column(db.String(30))
    msa_update_date = db.Column(db.Date())
    msa_update_user = db.Column(db.String(30))
    

class AdminSchema(Schema):
    msa_id =fields.Int(data_key='id')
    msa_email = fields.Str(data_key='email')
    # msa_password = fields.Str(data_key='password')
    msa_name = fields.Str(data_key='name')
    msa_active_status =fields.Str(data_key='active_status')
