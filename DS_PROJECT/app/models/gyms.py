from .. import db

class Gym(db.Model):
    __tablename__ = 'Gyms'
    GymID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.String(255), nullable=True)
