from .....Model.Generic import Generic
from .MapModel import MapModel


class SubCategoryModel(Generic):
    __tablename__ = "subcategories"
    subctg_id=Generic.db.Column(Generic.db.Integer(), primary_key=True)
    subctg_desc=Generic.db.Column(Generic.db.String(255), nullable=True)
    sub_ctg_id=Generic.db.Column(Generic.db.Integer(), Generic.db.ForeignKey('categories.ctg_id'), nullable=False)
    subctg_maps = Generic.db.relationship('MapModel', backref=Generic.db.backref('subcategories', lazy=True), order_by=MapModel.map_desc)