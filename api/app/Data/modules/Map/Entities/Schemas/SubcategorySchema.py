from app import data_ns
from flask_restx import fields
from .MapSchema import map_schema

subcategory_schema = data_ns.model(
    "SubCategory", 
    {
        "subctg_id": fields.Integer(required=True),
        "subctg_desc": fields.String(required=True),
        "sub_ctg_id": fields.Integer(required=True),
        "subctg_maps": fields.Nested(map_schema, many=True),
    }
)

subcategory_validation_schema = data_ns.model(
    "SubCategoryValidation",
    {
        "subctg_desc": fields.String(required=True, min_length=6, max_length=100),
        "sub_ctg_id": fields.Integer(required=True),
    }
)
