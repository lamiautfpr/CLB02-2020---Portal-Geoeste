
from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Protocols.Protocols import ServiceProtocol
from flask_restx import Resource
from typing import Type
from app.Data.modules.Map.Entities.Schemas.CategorySchema import category_validation


def init_category_resources(service: ServiceProtocol):

    class CategoriesResource(Resource):

        route = '/categorias'


        def get(self):
            categories = service.dao.get()
            return service.marshall_many(categories), 201


        @service.namespace.expect(category_validation)
        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                category_validation.validate(service.namespace.payload)
                category = service.dao.create(service.namespace.payload)
                return service.marshall_one(category), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400



    class CategoryResource(Resource):

        route = '/categorias/<int:ctg_id>'


        def get(self, ctg_id):
            try:
                category = service.dao.get_one(ctg_id)
                return service.marshall_one(category), 201
            except Exception as e:
                return {"Error":"{}".format(e)}, 400


        @service.namespace.expect(category_validation)
        @token_required
        def put(self, current_user: User, ctg_id):       
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                category_validation.validate(service.namespace.payload)

                if service.namespace.payload['ctg_desc'] == "":
                    exception = Exception("Category Description  is empty")
                    return {"Error":"Expectation Failed", "Exception":str(exception)}, 417

                category = service.dao.update(ctg_id, service.namespace.payload)
                if category:
                    return service.marshall_one(category), 201
                else:
                    return {"Error":"Category Not Found"}, 404
            except Exception as e:
                return {"Error":"{}".format(e)}, 400


        @token_required
        def delete(self, current_user, ctg_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                service.dao.delete(ctg_id)
                return {"Message":"Category Deleted"}, 200
            except Exception as e:
                return {"Error":"{}".format(e)}, 400

    
    return [CategoriesResource, CategoryResource]
