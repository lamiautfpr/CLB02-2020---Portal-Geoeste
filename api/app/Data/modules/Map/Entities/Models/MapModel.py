from .LegendModel import LegendModel
from .ReferencyModel import ReferencyModel
from .....Model.Generic import Generic

class MapModel(Generic):

    __tablename__ = "maps"
    map_id=Generic.db.Column(Generic.db.String(255), primary_key=True)
    map_desc=Generic.db.Column(Generic.db.String(255), nullable=False)
    map_atr=Generic.db.Column(Generic.db.String(255), nullable=True)
    map_value=Generic.db.Column(Generic.db.String(255), nullable=True)
    map_ctg=Generic.db.Column(Generic.db.String(255), nullable=True)
    choropleth=Generic.db.Column(Generic.db.Integer(), nullable=True)
    static=Generic.db.Column(Generic.db.Boolean(), nullable=True)
    data_file=Generic.db.Column(Generic.db.LargeBinary(), nullable=True)

    map_subctg_id=Generic.db.Column(Generic.db.Integer(), Generic.db.ForeignKey('subcategories.subctg_id'), nullable=False)

    map_ref_id=Generic.db.Column(Generic.db.Integer(), Generic.db.ForeignKey('referency.ref_id'), nullable=False)


    map_refs=Generic.db.relationship('ReferencyModel', backref=Generic.db.backref('maps', lazy=True))

    map_legs=Generic.db.relationship('LegendModel', backref=Generic.db.backref('maps', lazy=True), order_by=LegendModel.leg_id)

