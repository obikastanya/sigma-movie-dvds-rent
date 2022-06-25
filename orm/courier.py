from app import db

class Courier(db.Model):
    __tablename__='courier'
    msc_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    msc_desc =db.Column(db.Integer(), nullable=False)
    msc_active_status =db.Column(db.Integer(), nullable=False)
    ri_create_date  = db.Column(db.Date())
    ri_create_user = db.Column(db.String(30))
    ri_update_date = db.Column(db.Date())
    ri_update_user = db.Column(db.String(30))
    