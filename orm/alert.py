from app import db


class Alert(db.Model):
    __tablename__='user_alert'

    al_id =db.Column(db.Integer(), primary_key=True)
    al_msu_id=db.Column(db.Integer())
    al_read_status = db.Column(db.String(1))
    al_create_date  = db.Column(db.Date())
    al_create_user = db.Column(db.String(30))
    al_update_date = db.Column(db.Date())
    al_update_user = db.Column(db.String(30))
    