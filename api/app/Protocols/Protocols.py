
from typing import Protocol
from app.Data.DAO.GenericDAO import GenericDAO
from flask_restx import Namespace

class ServiceProtocol(Protocol):
    dao: GenericDAO
    namespace: Namespace
    schema: Namespace.model

    def marshall_one(self, result):
        ...

    
    def marshall_many(self, result_list):
        ...


class MapUploadProtocol(Protocol):
    def upload(self):
        ...


    def extract_zip(self):
        ...


    def delete_file(self):
        ...


    def clean_folder(self):
        ...

    def correct_table_name(self):
        ...


    def create_table(self):
        ...

    
    def upload_proccess(self):
        ...
    





