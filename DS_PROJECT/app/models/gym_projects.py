from .. import db

class GymProject(db.Model):
    __tablename__ = 'GymProjects'
    ProjectID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Projectname = db.Column(db.String(255), nullable=False)
    Duration = db.Column(db.Integer)
    Frequency = db.Column(db.Integer)
