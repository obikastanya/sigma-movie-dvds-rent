from app import db

class MoviewReturnedHead(db.Model):
    __tablename__='movie_returned_head'
    mrh_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    mrh_mrth_id =db.Column(db.Integer(), nullable=False)
    mrh_mrth_msu_id =db.Column(db.Integer(), nullable=False)
    mrth_return_date =db.Column(db.Date(), nullable=False)
    mrh_create_date  = db.Column(db.Date())
    mrh_create_user = db.Column(db.String(30))
    mrh_update_date = db.Column(db.Date())
    mrh_update_user = db.Column(db.String(30))