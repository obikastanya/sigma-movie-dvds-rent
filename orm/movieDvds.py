from app import db

class MovieDvds(db.Model):
    __tablename__='ms_movie_dvds'
    mvd_id =db.Column(db.Integer(), primary_key=True, nullable=False)
    mvd_desc =db.Column(db.String(500), nullable=False)
    mvd_release_date = db.Column(db.Date(), nullable=False)
    mvd_age_certification =db.Column(db.Integer(), nullable=False)
    mvd_genre =db.Column(db.String(50), nullable=False)
    mvd_total_dvds =db.Column(db.Integer(), nullable=False)
    mvd_available_stock =db.Column(db.Integer(), nullable=False)
    mvd_image_path =db.Column(db.String(200))
    mvd_active_status =db.Column(db.String(1), nullable=False)
    mvd_create_date  = db.Column(db.Date())
    mvd_create_user = db.Column(db.String(30))
    mvd_update_date = db.Column(db.Date())
    mvd_update_user = db.Column(db.String(30))

    movie_dvds_movie_reviews=db.relationship('MovieReviews', backref='movie_dvds_movie_reviews')
    movie_dvds_movie_returned_detail=db.relationship('MovieReturnedDetail', backref='movie_dvds_movie_returned_detail')
    movie_dvds_movie_renter_detail=db.relationship('MovieRenterDetail', backref='movie_dvds_movie_renter_detail')
    
    