from .....Model.Generic import Generic
from .SubcategoryModel import SubCategoryModel

class CategoryModel(Generic):
    __tablename__ = "categories"
    ctg_id=Generic.db.Column(Generic.db.Integer(), primary_key=True)
    ctg_desc=Generic.db.Column(Generic.db.String(255), nullable=True)
    ctg_subs = Generic.db.relationship('SubCategoryModel', backref=Generic.db.backref('categories', lazy=True), order_by= SubCategoryModel.subctg_desc)