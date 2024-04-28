from .. import db

class Conference(db.Model):
    __tablename__ = 'Conferences'
    ConferenceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date = db.Column(db.Date, nullable=False)
    Address = db.Column(db.String(255), nullable=True)
    Topic = db.Column(db.String(255), nullable=True)
