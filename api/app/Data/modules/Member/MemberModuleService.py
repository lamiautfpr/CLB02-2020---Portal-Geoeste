
from app.Data.DAO.GenericDAO import GenericDAO
from app.Data.GenericService import GenericService
from app.Data.modules.Member.Entities import Models, Schemas
from app.Data.modules.Member.Resources.MemberResources import init_member_resources
from app.Data.modules.Member.Resources.PublicationResources import init_publication_resources
from app.Data.modules.Member.Resources.TeamResources import init_team_resources


class MemberModuleService():
    
        def __init__(self):
            self.member_services = GenericService(
                dao=GenericDAO(Models.MemberModel), schema=Schemas.member_schema, init_resources=init_member_resources
            ).updateNamespace()

            self.team_services = GenericService(
                dao=GenericDAO(Models.TeamModel), schema=Schemas.team_schema, init_resources=init_team_resources
            ).updateNamespace()
            
            self.publication_services = GenericService(
                dao=GenericDAO(Models.PublicationModel), schema=Schemas.publication_schema, init_resources=init_publication_resources
            ).updateNamespace()

        
        def services(self, namespace):
            for attr, value in self.__dict__.items():
                namespace = value.updateNamespace() if isinstance(value, GenericService) else namespace
            return namespace