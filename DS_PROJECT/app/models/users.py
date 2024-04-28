from .. import db

class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=True)
    Age = db.Column(db.Integer, nullable=True)
    Country = db.Column(db.String(50), nullable=True)
