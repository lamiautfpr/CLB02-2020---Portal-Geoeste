from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Data.GenericService import GenericService
from flask_restx import Resource
from ..Entities.Schemas.MemberSchema import member_validation_schema

def init_member_resources(member_service: GenericService):

    class MembersResource(Resource):

        route: str = '/members'

        def get(self):
            try:
                members = member_service.dao.get()
                return member_service.marshall_many(members)
            except Exception as e:
                return {'message': 'Error: {}'.format(e)}, 500

        @member_service.namespace.expect(member_validation_schema)
        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                member_validation_schema.validate(member_service.namespace.payload)
                member = member_service.dao.create(member_service.namespace.payload)
                return member_service.marshall_one(member), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


    class MemberResource(Resource):
        route: str = '/members/<int:id>'
        def get(self, id):
            try:
                member = member_service.dao.get_one(id)
                return member_service.marshall_one(member), 201
            except Exception as e:
                return {"Error":"{}".format(e)}, 404


        @member_service.namespace.expect(member_validation_schema)
        @token_required
        def put(self, current_user: User, member_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                member_validation_schema.validate(member_service.namespace.payload)
                member = member_service.dao.update(member_id, member_service.namespace.payload)
                return member_service.marshall_one(member), 201
            except:
                return {"Error":"Not Found"}, 404

        @token_required
        def delete(self, current_user: User, member_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                member = member_service.dao.delete(member_id)
                return member_service.marshall_one(member), 201
            except:
                return {"Error":"Not Found"}, 404


    return [MemberResource, MembersResource]