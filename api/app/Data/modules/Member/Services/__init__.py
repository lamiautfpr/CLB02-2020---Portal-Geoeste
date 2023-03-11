
from app.Data.DataService import DataService
from app.Data.modules.Member.Services.MemberService import MemberService
from app.Data.modules.Member.Services.TeamService import TeamService

member_service = MemberService()
team_service = TeamService()

member_module_service = DataService(routes=[member_service.getNameSpace(), team_service.getNameSpace()])
member_module_service.init_services()