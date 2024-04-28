from .. import db

class UserGymProject(db.Model):
    __tablename__ = 'UserGymProjects'
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('GymProjects.ProjectID'), primary_key=True)
