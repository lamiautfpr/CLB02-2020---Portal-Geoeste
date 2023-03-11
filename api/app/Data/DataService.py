from typing import List
from flask_restx import Namespace
from ..extensions import data_ns


class DataService(object):
    routes: List[Namespace]


    def __init__(self, routes: List[Namespace]):
        self.routes = routes


    def init_services(self):
        for route in self.routes:
            self.namespace = route
        return self.namespace