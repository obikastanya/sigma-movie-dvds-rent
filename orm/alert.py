from app import db


class Alert(db.Model):
    __tablename__='user_alert'

    al_id =db.Column(db.Integer(), primary_key=True)
    al_read_status = db.Column(db.String(1), unique=True, nullable=False)
    msa_create_date  = db.Column(db.Date())
    msa_create_user = db.Column(db.String(30))
    msa_update_date = db.Column(db.Date())
    msa_update_user = db.Column(db.String(30))
    