from .....Model.Generic import Generic

class MemberModel(Generic):
    __tablename__ = "members"
    id=Generic.db.Column(Generic.db.Integer(), primary_key=True)
    name=Generic.db.Column(Generic.db.String(255), nullable=True)
    lattes=Generic.db.Column(Generic.db.String(255), nullable=True)
    git=Generic.db.Column(Generic.db.String(30), nullable=True)
    member_team_id=Generic.db.Column(Generic.db.Integer(), Generic.db.ForeignKey('team.id'), nullable=False)