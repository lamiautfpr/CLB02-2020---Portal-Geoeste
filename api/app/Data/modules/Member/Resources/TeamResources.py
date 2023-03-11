from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Data.GenericService import GenericService
from ..Entities.Schemas.TeamSchema import team_validation_schema
from flask_restx import Resource

def init_team_resources(team_service: GenericService):
    
    class TeamsResource(Resource):
        
        route: str = '/teams'

        def get(self):
            try:
                teams = team_service.dao.get()
                return team_service.marshall_many(teams)
            except Exception as e:
                return {'message': 'Error: {}'.format(e)}, 500


        @team_service.namespace.expect(team_validation_schema)
        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                team_validation_schema.validate(team_service.namespace.payload)
                team = team_service.dao.create(team_service.namespace.payload)
                return team_service.marshall_one(team), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


    class TeamResource(Resource):

        route: str = '/teams/<int:id>'

        def get(self, id):
            try:
                team = team_service.dao.get_one(id)
                return team_service.marshall_one(team), 201
            except Exception as e:
                return {"Error":"{}".format(e)}, 404


        @team_service.namespace.expect(team_validation_schema)
        @token_required
        def put(self,current_user: User, team_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                team_validation_schema.validate(team_service.namespace.payload)
                team = team_service.dao.update(team_id, team_service.namespace.payload)
                return team_service.marshall_one(team), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


        @token_required
        def delete(self, current_user: User, team_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                team = team_service.dao.delete(team_id)
                return team_service.marshall_one(team), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400

    return [TeamsResource, TeamResource]