from app import db

class User(db.Model):
    __tablename__='ms_user'

    msu_id =db.Column(db.Integer(), primary_key=True)
    msu_email = db.Column(db.String(50), unique=True, nullable=False)
    msu_password = db.Column(db.String(100), nullable=False)
    msu_name = db.Column(db.String(100), nullable=False)
    msu_address =db.Column(db.String(200), nullable=False)
    msu_gender = db.Column(db.String(1), nullable=False)
    msu_birth_date = db.Column(db.Date(), nullable=False)
    msu_create_date  = db.Column(db.Date())
    msu_create_user = db.Column(db.String(30))
    msu_update_date = db.Column(db.Date())
    msu_update_user = db.Column(db.String(30))
    
