from app import db

class Courier(db.Model):
    __tablename__='ms_courier'
    msc_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    msc_desc =db.Column(db.String(100), nullable=False)
    msc_active_status =db.Column(db.String(1), nullable=False)
    msc_create_date  = db.Column(db.Date())
    msc_create_user = db.Column(db.String(30))
    msc_update_date = db.Column(db.Date())
    msc_update_user = db.Column(db.String(30))

    courier_dvds_shipment=db.relationship('DvdsShipment', backref='courier_dvds_shipment')
    