from ..Entities.Models.MemberModel import MemberModel

class MemberDAO(object):
    
        def __init__(self):
            pass


        def get(self):
            return MemberModel.get_all()

        def get_one(self, member_id):
            return MemberModel.get_one_by(id=member_id)

        def get_by(self, **kwargs):
            return MemberModel.get_by(**kwargs)


        def create(self, data):
            return MemberModel.create(
                name=data['name'],
                lattes=data['lattes'],
                git=data['git'],
                member_team_id=data['member_team_id']
            )

        
        def update(self, member_id, data):
            member = self.get_one(member_id)
            member.name=data['name']
            member.lattes=data['lattes']
            member.git=data['git']
            member.member_team_id=data['member_team_id']
            return member.update_to_db()

        
        def delete(self, member_id):
            member = self.get_one(member_id)
            return member.delete_from_db()
