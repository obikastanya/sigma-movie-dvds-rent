from app import db

class MoviewRenterDetail(db.Model):
    __tablename__='movie_rental_detail'
    mrtd_mvd_id =db.Column(db.Integer(),  primary_key=True,nullable=False)
    mrtd_mrth_id =db.Column(db.Integer(), nullable=False)
    mrtd_create_date  = db.Column(db.Date())
    mrtd_create_user = db.Column(db.String(30))
    mrtd_update_date = db.Column(db.Date())
    mrtd_update_user = db.Column(db.String(30))