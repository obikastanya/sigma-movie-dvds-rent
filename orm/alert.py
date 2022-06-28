from app import db
from marshmallow import Schema, fields


class Alert(db.Model):
    __tablename__='user_alert'

    al_id =db.Column(db.Integer(), primary_key=True)
    al_msu_id=db.Column(db.Integer())
    al_title=db.Column(db.String(100))
    al_desc=db.Column(db.String(200))
    al_read_status = db.Column(db.String(1))
    al_create_date  = db.Column(db.Date())
    al_create_user = db.Column(db.String(30))
    al_update_date = db.Column(db.Date())
    al_update_user = db.Column(db.String(30))
    
class AlertSchema(Schema):
    al_id =fields.Int(data_key='id')
    al_title=fields.Str(data_key='title')
    al_desc=fields.Str(data_key='desc')