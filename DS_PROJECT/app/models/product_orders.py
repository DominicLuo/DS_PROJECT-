from .. import db
from datetime import datetime

class ProductOrder(db.Model):
    __tablename__ = 'ProductOrders'
    OrderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)
    SupplierID = db.Column(db.Integer, db.ForeignKey('Suppliers.SupplierID'), nullable=False)
    OrderDate = db.Column(db.DateTime, default=datetime.utcnow)
    ArrivalDATE = db.Column(db.DateTime)
    DeliveryStatus = db.Column(db.String(50), nullable=False)
