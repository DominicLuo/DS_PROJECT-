from .. import db

class Product(db.Model):
    __tablename__ = 'Products'
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SupplierID = db.Column(db.Integer, db.ForeignKey('Suppliers.SupplierID'))
    ProductName = db.Column(db.String(255), nullable=False)
    Intro = db.Column(db.String(255), nullable=True)
    Price = db.Column(db.Integer, nullable=False)
