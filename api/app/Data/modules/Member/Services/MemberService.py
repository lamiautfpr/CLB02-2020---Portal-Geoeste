from flask_restx import Resource, Namespace
from app import data_ns
from ..DAO.MemberDAO import MemberDAO
from ..Entities.Models.TeamModel import TeamModel
from ..Entities.Schemas.MemberSchema import member_schema, member_validation_schema
from ..Routes.MemberRoutes import init_routes

class MemberService():
    member_namespace: Namespace = data_ns
    dao: MemberDAO = MemberDAO()      


    def __init__(self):
        init_routes(self)


    def getNameSpace(self):
        return self.member_namespace
    

    @member_namespace.marshal_list_with(member_schema)
    def ReturnAllMembers(self, members):
        return members


    @member_namespace.marshal_with(member_schema)
    def ReturnMember(self, member):
        return member

