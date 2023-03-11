from flask_restx import fields
from app import data_ns

referency_schema=data_ns.model(
    "Referency",
    {
        "ref_id":fields.String(),
        "src":fields.String(),
        "fontes":fields.String(),
        "elaboracao":fields.String()
    }
)


referency_validation_schema=data_ns.model(
    "ReferencyValidation",
    {
        "ref_id":fields.String(required=True),
        "src":fields.String(required=True),
        "fontes":fields.String(required=True),
        "elaboracao":fields.String(required=True),
        "base_cartografica":fields.String(required=False)
    }
)