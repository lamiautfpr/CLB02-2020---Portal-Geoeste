from enum import Enum
from app.Data.Model.Generic import Generic


class PublicationType(Enum):
    ARTICLE = 'Artigo'
    BOOK = 'Livro'
    SEMINAR = 'Seminário'
    CONFERENCE = 'Conferência'


class PublicationModel(Generic):
    __tablename__ = "publications"
    pub_id = Generic.db.Column(Generic.db.Integer(), primary_key=True)
    pub_title = Generic.db.Column(Generic.db.String(50), nullable=False)
    pub_desc = Generic.db.Column(Generic.db.String(255), nullable=True)
    pub_file = Generic.db.Column(Generic.db.LargeBinary(), nullable=False)
    pub_number_of_pages = Generic.db.Column(Generic.db.Integer(), nullable=False)
    pub_authors = Generic.db.Column(Generic.db.String(255), nullable=False)
    pub_date = Generic.db.Column(Generic.db.Date(), nullable=True)
    pub_type = Generic.db.Column(Generic.db.Enum(PublicationType), nullable=True)
    pub_keywords = Generic.db.Column(Generic.db.String(255), nullable=True)
    pub_link = Generic.db.Column(Generic.db.String(255), nullable=True)

    def check_publication_type(pub_type: str):
        for type in PublicationType:
            if type._value_ == pub_type:
                return type
        return None
    
