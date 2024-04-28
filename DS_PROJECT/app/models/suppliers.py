from .. import db

class Supplier(db.Model):
    __tablename__ = 'Suppliers'
    SupplierID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
