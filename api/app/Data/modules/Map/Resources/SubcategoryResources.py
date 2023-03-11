from typing import Type
from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Protocols.Protocols import ServiceProtocol
from flask_restx import Resource
from app.Data.modules.Map.Entities.Schemas.SubcategorySchema import subcategory_validation_schema


def init_subcategory_resources(service: ServiceProtocol):

    class SubcategoriesResource(Resource):

        route='/subcategorias'

        def get(self):            
            try:
                subcategories = service.dao.get()
                return service.marshall_many(subcategories), 200
            except Exception as e:
                return {'message': 'Not Found'}, 404
               
        
        
        @service.namespace.expect(subcategory_validation_schema)
        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                subcategory_validation_schema.validate(service.namespace.payload)
                subcategory = service.dao.create(service.namespace.payload)
                return service.marshall_one(subcategory), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


    class SubcategoryResource(Resource):

        route="/subcategorias/<int:id>"

        def get(self, id):
            try:
                subcategories = service.dao.get_one(id)
                return service.marshall_one(subcategories), 200
            except Exception as e:
                return {'message': 'Not Found'}, 404

        @service.namespace.expect(subcategory_validation_schema)
        @token_required
        def put(self, current_user: User, id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                subcategory_validation_schema.validate(service.namespace.payload)
                subcategory = service.dao.update(id, service.namespace.payload)
                return service.marshall_one(subcategory), 201
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
                return {"Message":"SubCategory Deleted"}, 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


    return [SubcategoriesResource, SubcategoryResource]
