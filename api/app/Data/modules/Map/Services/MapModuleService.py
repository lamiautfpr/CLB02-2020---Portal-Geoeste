from app.Data.DAO.GenericDAO import GenericDAO
from app.Data.modules.Map.Entities import Schemas
from app.Data.modules.Map.Entities import Models
from app.Data.modules.Map.Resources.CategoryResources import init_category_resources
from app.Data.GenericService import GenericService
from app.Data.modules.Map.Resources.LegendResources import init_legend_resources
from app.Data.modules.Map.Resources.MapResources import init_map_resources
from app.Data.modules.Map.Resources.ReferencyResources import init_referency_resources
from app.Data.modules.Map.Resources.SubcategoryResources import init_subcategory_resources

class MapModuleService(object):

    def __init__(self):
        self.map_services = GenericService(dao=GenericDAO(Models.MapModel), schema=Schemas.map_schema, init_resources=init_map_resources).updateNamespace()
        self.category_services = GenericService(dao=GenericDAO(Models.CategoryModel), schema= Schemas.category_schema, init_resources=init_category_resources)
        self.subcategory_services = GenericService(dao=GenericDAO(Models.SubCategoryModel), schema=Schemas.subcategory_schema, init_resources=init_subcategory_resources).updateNamespace()
        self.referency_services = GenericService(dao=GenericDAO(Models.ReferencyModel), schema=Schemas.referency_schema, init_resources=init_referency_resources).updateNamespace()
        self.legend_services = GenericService(dao=GenericDAO(Models.LegendModel), schema=Schemas.legend_schema, init_resources=init_legend_resources).updateNamespace()

        

    def services(self, namespace):
        for attr, value in self.__dict__.items():
            namespace = value.updateNamespace() if isinstance(value, GenericService) else namespace
        return namespace


        
        
