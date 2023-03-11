from typing import Type
from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Protocols.Protocols import ServiceProtocol
from flask_restx import Resource
from app.Data.modules.Map.Entities.Schemas.LegendSchema import legend_validation


def init_legend_resources(service: ServiceProtocol):

    
    class LegendsResource(Resource):

        route = '/mapas/legendas'

        @service.namespace.expect(legend_validation)
        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                legend_validation.validate(service.payload)
                legend = service.dao.create(service.payload)
                return service.marshall_one(legend), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400

    
    class LegendResource(Resource):

        route = '/mapas/legendas/<int:leg_id>'

        @service.namespace.expect(legend_validation)
        @token_required
        def put(self, current_user: User, leg_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                legend_validation.validate(service.payload)
                legend = service.dao.update(leg_id, service.payload)
                if legend:
                    return service.marshall_one(legend), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400


        @token_required
        def delete(self, current_user: User, leg_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) is not False
                service.dao.delete(leg_id)
                return {"Message":"Item Deleted"}, 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Bad Request'}, 400

    return [LegendsResource, LegendResource]
