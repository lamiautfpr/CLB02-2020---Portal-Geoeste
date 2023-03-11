from .....Model.Generic import Generic


class LegendModel(Generic):
    __tablename__ = "legends"
    leg_id=Generic.db.Column(Generic.db.Integer(), primary_key=True)
    atr=Generic.db.Column(Generic.db.String(255), nullable=True)
    color=Generic.db.Column(Generic.db.String(8), nullable=True)
    leg_map_id=Generic.db.Column(Generic.db.String(255), Generic.db.ForeignKey('maps.map_id'), nullable=False)