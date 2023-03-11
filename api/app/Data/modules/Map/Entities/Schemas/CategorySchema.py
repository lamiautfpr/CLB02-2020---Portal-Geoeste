from flask_restx import fields
from app import data_ns
from .SubcategorySchema import subcategory_schema

category_schema = data_ns.model('Category', 
    {
        'ctg_id': fields.Integer(required=True, description='Category ID'),
        'ctg_desc': fields.String(required=True, description='Category description'),
        'ctg_subs': fields.Nested(subcategory_schema, description='Subcategories')
    }
)

category_validation = data_ns.model('CategoryValidation',
    {
        'ctg_desc': fields.String(required=True, description='Category description')
    }
)