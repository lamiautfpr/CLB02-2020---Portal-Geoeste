from flask_restx import fields
from app import data_ns

legend_schema=data_ns.model(
    "Legend", 
    {
        "atr": fields.String(required=False, description='Attribute'),
        "color": fields.String(required=False, description='Color'),
    }
)

legend_validation=data_ns.model(
    "LegendValidation",
    {
        "atr": fields.String(required=True, description='Attribute'),
        "color": fields.String(required=True, description='Color'),
        "leg_map_id": fields.String(required=True, description='Map ID')
    }
)