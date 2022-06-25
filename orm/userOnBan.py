from app import db

class UserOnBan(db.Model):
    __tablename__='user_on_ban'
    uob_id =db.Column(db.Integer(), primary_key=True, nullable=False)
    uob_msu_id =db.Column(db.Integer(),  db.ForeignKey('ms_user.msu_id'),nullable=False)
    uob_desc =db.Column(db.String(200), nullable=False)
    uob_status =db.Column(db.String(1), nullable=False)
    uob_banned_date = db.Column(db.Date(), nullable=False)
    uob_create_date  = db.Column(db.Date())
    uob_create_user = db.Column(db.String(30))
    uob_update_date = db.Column(db.Date())
    uob_update_user = db.Column(db.String(30))
    