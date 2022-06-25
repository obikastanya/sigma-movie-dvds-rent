from app import db

class DvdsShipment(db.Model):
    __tablename__='dvds_shipment'
    dsp_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    dsp_msc_id =db.Column(db.Integer(), db.ForeignKey('ms_courier.msc_id'), nullable=False)
    dsp_mrth_id =db.Column(db.Integer(),db.ForeignKey('movie_renter_head.mrth_id'), nullable=False)
    dsp_mrth_shipping_destination =db.Column(db.String(500), nullable=False)
    dsp_shipping_status  = db.Column(db.String(20))
    dsp_received_date = db.Column(db.Date())
    dsp_create_date  = db.Column(db.Date())
    dsp_create_user = db.Column(db.String(30))
    dsp_update_date = db.Column(db.Date())
    dsp_update_user = db.Column(db.String(30))