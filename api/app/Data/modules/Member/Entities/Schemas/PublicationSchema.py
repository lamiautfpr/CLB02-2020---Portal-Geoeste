from app.Data.modules.Member.Entities.Models.PublicationModel import PublicationType
from flask_restx import fields
from app import data_ns

class PublicationTypeField(fields.Raw):
    def format(self, value: PublicationType):
        return value._value_

publication_schema = data_ns.model(
    "Publication",
    {
        "pub_id": fields.String(description="Publication ID"),
        "pub_title": fields.String(description="Publication title"),
        "pub_desc": fields.String(description="Publication description"),
        "pub_number_of_pages": fields.Integer(description="Publication number of pages"),
        "pub_authors": fields.String(description="Publication's Authors"),
        "pub_date": fields.Date(description="Publication date"),
        "pub_type": PublicationTypeField(description="Publication type"),
        "pub_keywords": fields.String(description="Publication keywords"),
        "pub_link": fields.String(description="Publication link"),
    }
)

publication_validation_schema = data_ns.model(
    "PublicationValidation",
    {
        "pub_title": fields.String(required=True, min_length=6, max_length=50),
        "pub_desc": fields.String(required=False, min_length=6, max_length=255),    
        "pub_number_of_pages": fields.Integer(required=True),
        "pub_date": fields.Date(required=False),
        "pub_type": fields.String(required=False),
        "pub_keywords": fields.String(required=False, max_length=255),
    }
)
