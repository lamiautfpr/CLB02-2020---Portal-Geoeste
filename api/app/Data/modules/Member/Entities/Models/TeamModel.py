from .....Model.Generic import Generic
from .MemberModel import MemberModel

class TeamModel(Generic):
    __tablename__ = "team"
    id=Generic.db.Column(Generic.db.Integer(), primary_key=True)
    description=Generic.db.Column(Generic.db.String(255), nullable=True)
    members = Generic.db.relationship('MemberModel', backref=Generic.db.backref('team', lazy=True), order_by=MemberModel.id)