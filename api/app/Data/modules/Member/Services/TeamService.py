from flask_restx import Namespace
from app import data_ns
from ..DAO.TeamDAO import TeamDAO
from ..Entities.Schemas.TeamSchema import team_schema
from ..Routes.TeamRoutes import init_routes

class TeamService():
    team_namespace: Namespace = data_ns
    dao: TeamDAO = TeamDAO()      

    def __init__(self):
        init_routes(self)

    def getNameSpace(self):
        return self.team_namespace
    
    @team_namespace.marshal_list_with(team_schema)
    def ReturnAllTeams(self, teams):
        return teams

    @team_namespace.marshal_with(team_schema)
    def ReturnTeam(self, team):
        return team