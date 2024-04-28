from .. import db

class UserLevel(db.Model):
    __tablename__ = 'USERLEVEL'
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key=True)
    Level = db.Column(db.Integer, nullable=False)
    Point = db.Column(db.Integer, nullable=False)
