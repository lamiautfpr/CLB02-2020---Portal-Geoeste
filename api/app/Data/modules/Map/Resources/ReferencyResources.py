from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Protocols.Protocols import ServiceProtocol
from app.Data.modules.Map.Entities.Schemas.ReferencySchema import referency_validation_schema
from flask_restx import Resource


def init_referency_resources(service: ServiceProtocol):

    class ReferenciesResource(Resource):

        route: str = '/referencies'

        def get(self):
            try:
                res = service.dao.get()
                return service.marshall_many(res), 201
            except:
                return {"Error":"No Data Found"}, 404
                
        
        @service.namespace.expect(referency_validation_schema)
        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                referency_validation_schema.validate(service.namespace.payload)
                referency = service.dao.create(service.namespace.payload)
                return service.marshall_one(referency), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


    
    class ReferencyResource(Resource):

        route: str = "/referencies/<int:id>"

        def get(self, id):
            try:
                r = service.dao.get_one(id)
                return service.marshall_one(r), 201
            except:
                return {"Error":"No Data Found"}, 404


        @service.namespace.expect(referency_validation_schema)
        @token_required
        def put(self, current_user: User, id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                referency_validation_schema.validate(service.namespace.payload)
                referency = service.dao.update(id, service.namespace.payload)
                return service.marshall_one(referency), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400
                

        @token_required
        def delete(self, current_user: User, id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                service.dao.delete(id)
                return {"Message":"Referency Deleted"}, 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


    return [ReferenciesResource, ReferencyResource]
