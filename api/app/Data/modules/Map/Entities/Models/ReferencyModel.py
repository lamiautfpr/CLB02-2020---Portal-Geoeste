from .....Model.Generic import Generic


class ReferencyModel(Generic):
    __tablename__ = "referency"
    ref_id=Generic.db.Column(Generic.db.Integer(), primary_key=True)
    src=Generic.db.Column(Generic.db.String(255), nullable=True)
    fontes=Generic.db.Column(Generic.db.String(255), nullable=True)
    elaboracao=Generic.db.Column(Generic.db.String(255), nullable=True)