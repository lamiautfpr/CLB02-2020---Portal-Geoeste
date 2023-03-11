from app import data_ns
from flask_restx import fields
from .MemberSchema import member_schema

team_schema=data_ns.model(
    "Team",
    {
        "id":fields.Integer(),
        "description":fields.String(255),
        "members":fields.List(fields.Nested(member_schema))
    }
)

team_validation_schema=data_ns.model(
    "TeamValidation",
    {
        "description":fields.String(255),
    }
)