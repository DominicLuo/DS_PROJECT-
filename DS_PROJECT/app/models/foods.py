from .. import db

class Food(db.Model):
    __tablename__ = 'Foods'
    FoodID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SupplierID = db.Column(db.Integer, db.ForeignKey('Suppliers.SupplierID'))
    Name = db.Column(db.String(255), nullable=False)
    Carbohydrates = db.Column(db.Float)
    Protein = db.Column(db.Float)
    Fat = db.Column(db.Float)
