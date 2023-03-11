from app.extensions import data_ns
from flask_restx import fields

member_schema=data_ns.model(
    "Member",
    {
        "id":fields.Integer(),
        "name":fields.String(255),
        "lattes":fields.String(255),
        "git":fields.String(30),
        "member_team_id":fields.Integer()
    }
)

member_validation_schema=data_ns.model(
    "MemberValidation",
    {
        "name":fields.String(255),
        "lattes":fields.String(255),
        "git":fields.String(30),
        "member_team_id":fields.Integer()
    }
)