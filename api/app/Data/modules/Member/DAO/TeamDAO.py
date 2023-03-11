from ..Entities.Models.TeamModel import TeamModel

class TeamDAO(object):
        
        def __init__(self):
            pass


        def get(self):
            return TeamModel.get_all()

        def get_one(self, team_id):
            return TeamModel.get_one_by(team_id=team_id)

        def get_by(self, **kwargs):
            return TeamModel.get_by(**kwargs)

        def create(self, data):
            return TeamModel.create(
                description=data['description'],
            )

        
        def update(self, team_id, data):
            team = self.get_one(team_id)
            team.description=data['description']
            return team.update_to_db()

        
        def delete(self, team_id):
            team = self.get_one(team_id)
            return team.delete_from_db()