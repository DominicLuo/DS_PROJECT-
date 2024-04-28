from .. import db

class Diet(db.Model):
    __tablename__ = 'Diets'
    DietID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.String(255))
