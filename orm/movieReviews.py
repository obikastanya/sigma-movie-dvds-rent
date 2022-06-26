from app import db
from marshmallow import fields, Schema


class MovieReviews(db.Model):
    __tablename__='movie_reviews'

    mr_mvd_id =db.Column(db.Integer(),db.ForeignKey('ms_movie_dvds.mvd_id'), nullable=False, primary_key=True)
    mr_msu_id =db.Column(db.Integer(),db.ForeignKey('ms_user.msu_id'), nullable=False,primary_key=True)
    mr_desc =db.Column(db.String(500))
    mr_rate =db.Column(db.Integer(), nullable=False)
    mr_active_status =db.Column(db.String(1), nullable=False)
    mr_create_date  = db.Column(db.Date())
    mr_create_user = db.Column(db.String(30))
    mr_update_date = db.Column(db.Date())
    mr_update_user = db.Column(db.String(30))


class MovieReviewsUserSchema(Schema):
    mr_mvd_id =fields.Int(data_key='id')
    mr_desc = fields.Str(data_key='desc')
    mr_rate = fields.Int(data_key='rate')
    user_movie_reviews=fields.Nested('UserSchema',  only=('msu_id','msu_name'),data_key='users')


class MovieReviewsMovieSchema(Schema):
    mr_mvd_id =fields.Int(data_key='id')
    mr_desc = fields.Str(data_key='desc')
    mr_rate = fields.Int(data_key='rate')
    movie_dvds_movie_reviews=fields.Nested('MovieDvdsSchema',  only=('mvd_id','mvd_title'), data_key='movies')
    