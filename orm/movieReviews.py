from app import db

class MoviewReviews(db.Model):
    __tablename__='movie_reviews'
    mr_mvd_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    mr_msu_id =db.Column(db.Integer(), nullable=False)
    mr_desc =db.Column(db.String(500))
    mr_rate =db.Column(db.Integer(), nullable=False)
    mr_active_status =db.Column(db.String(1), nullable=False)
    mr_create_date  = db.Column(db.Date())
    mr_create_user = db.Column(db.String(30))
    mr_update_date = db.Column(db.Date())
    mr_update_user = db.Column(db.String(30))