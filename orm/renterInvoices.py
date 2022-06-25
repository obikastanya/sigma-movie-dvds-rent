from app import db

class RenterInvoices(db.Model):
    __tablename__='renter_invoices'
    ri_id =db.Column(db.Integer(), nullable=False, primary_key=True)
    ri_mrth_id =db.Column(db.Integer(), nullable=False)
    ri_nominal =db.Column(db.Integer(), nullable=False)
    ri_status_bayar =db.Column(db.String(1), nullable=False)
    ri_bukti_bayar  = db.Column(db.String(200))
    ri_transaction_date = db.Column(db.Date())
    ri_transaction_validation_date = db.Column(db.Date())
    ri_create_date  = db.Column(db.Date())
    ri_create_user = db.Column(db.String(30))
    ri_update_date = db.Column(db.Date())
    ri_update_user = db.Column(db.String(30))