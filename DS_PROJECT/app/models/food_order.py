from .. import db
from datetime import datetime

class FoodOrder(db.Model):
    __tablename__ = 'FoodOrder'
    FDeliveryID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DeliveryStatus = db.Column(db.String(255), nullable=False)
    OrderTime = db.Column(db.Time, default=datetime.utcnow)
    SupplierID = db.Column(db.Integer, db.ForeignKey('Suppliers.SupplierID'))
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    CurrentLocation = db.Column(db.String(255), nullable=False)
    EstimateTime = db.Column(db.Integer)
