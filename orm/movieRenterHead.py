from app import db

class MoviewRenterHead(db.Model):
    __tablename__='movie_rental_head'
    mrth_id =db.Column(db.Integer(),  primary_key=True,nullable=False)
    mrth_msu_id =db.Column(db.Integer(), nullable=False)
    mrth_rent_start_date =db.Column(db.Date(), nullable=False)
    mrth_rent_due_date =db.Column(db.Date(), nullable=False)
    mrth_rent_duration =db.Column(db.Integer())
    mrth_shipping_destination =db.Column(db.String(500), nullable=False)
    mrth_create_date  = db.Column(db.Date())
    mrth_create_user = db.Column(db.String(30))
    mrth_update_date = db.Column(db.Date())
    mrth_update_user = db.Column(db.String(30))