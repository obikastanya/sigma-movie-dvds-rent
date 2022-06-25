from app import db

class MoviewReturnedHead(db.Model):
    __tablename__='movie_returned_head'
    mrh_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    mrh_mrth_id =db.Column(db.Integer(),db.ForeignKey('movie_renter_head.mrth_id'), nullable=False)
    mrh_mrth_msu_id =db.Column(db.Integer(),db.ForeignKey('ms_user.msu_id'), nullable=False)
    mrth_return_date =db.Column(db.Date(), nullable=False)
    mrh_create_date  = db.Column(db.Date())
    mrh_create_user = db.Column(db.String(30))
    mrh_update_date = db.Column(db.Date())
    mrh_update_user = db.Column(db.String(30))

    movie_returned_head_movie_returned_detail=db.relationship('MovieReturnedDetail', backref='movie_returned_head_movie_returned_detail')