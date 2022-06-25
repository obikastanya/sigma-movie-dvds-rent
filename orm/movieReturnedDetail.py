from app import db

class MovieReturnedDetail(db.Model):
    __tablename__='movie_returned_detail'
    mrd_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    mrd_mrh_id =db.Column(db.Integer(),db.ForeignKey('movie_returned_head.mrh_id'), nullable=False)
    mrd_mvd_id =db.Column(db.Integer(),db.ForeignKey('ms_movie_dvds.mvd_id'), nullable=False)
    mrd_dvd_desc =db.Column(db.Date(), nullable=False)
    mrd_create_date  = db.Column(db.Date())
    mrd_create_user = db.Column(db.String(30))
    mrd_update_date = db.Column(db.Date())
    mrd_update_user = db.Column(db.String(30))