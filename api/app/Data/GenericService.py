
from typing import Callable, Type
from flask_restx import Namespace
from ..extensions import data_ns
from app.Data.DAO.GenericDAO import GenericDAO


class GenericService(object):
    namespace: Namespace = data_ns
    schema: Namespace.model
    dao: GenericDAO
    resources: list


    def __init__(self, dao: GenericDAO, schema: Namespace.model, init_resources: Callable):
        self.dao = dao
        self.schema = schema
        self.resources = init_resources(self) if init_resources else []


    def getNamespace(self):
        return self.namespace


    def updateNamespace(self):
        for resource in self.resources:
            self.namespace.add_resource(resource, resource.route)
        return self.namespace

    def marshall_one(self, result):
        @self.namespace.marshal_with(self.schema)
        def marshal(result):
            return result

        return marshal(result)


    def marshall_many(self, result_list):
        @self.namespace.marshal_list_with(self.schema)
        def marshal_list(result_list):
            return result_list
        
        return marshal_list(result_list)
        







