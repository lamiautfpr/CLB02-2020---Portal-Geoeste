from flask_restx import fields
from app import data_ns
from .LegendSchema import legend_schema
from .ReferencySchema import referency_schema

map_schema=data_ns.model(
    "Map",
    {
        "map_id":fields.String(),
        "map_desc":fields.String(),
        "map_value":fields.String(),
        "map_atr": fields.String(),
        "map_ctg": fields.String(),
        "choropleth": fields.Integer(),
        "map_subctg_id": fields.Integer(),
        "map_refs": fields.Nested(referency_schema),
        "map_legs": fields.Nested(legend_schema),
    }
)


map_validation_schema=data_ns.model(
    "MapValidation",
    {
        "map_id":fields.String(required=True),
        "map_desc":fields.String(required=True, min_length=6, max_length=100),
        "map_atr": fields.String(required=True),
        "map_ctg": fields.String(required=False),
        "choropleth": fields.Integer(required=True),
        "map_subctg_id": fields.Integer(required=True),
    }
)

map_update_validation_schema=data_ns.model(
    "MapUpdateValidation",
    {
        "map_desc":fields.String(min_length=6, max_length=100),
        "map_atr": fields.String(),
        "map_ctg": fields.String(),
        "choropleth": fields.Integer(),
        "map_subctg_id": fields.Integer(),
    }
)