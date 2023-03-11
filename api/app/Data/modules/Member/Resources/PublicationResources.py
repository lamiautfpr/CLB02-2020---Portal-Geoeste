from io import BytesIO
from app.Auth.auth import token_required
from app.Auth.models import Patent, User
from app.Data.modules.Member.Entities.Models.PublicationModel import PublicationModel
from app.Protocols.Protocols import ServiceProtocol
from flask_restx import Resource
from flask import request, jsonify, send_file
from json import loads
import datetime

def init_publication_resources(service: ServiceProtocol):

    class PublicationsResource(Resource):
            
            title: str = 'Publication:'
            route: str = '/publications'
    
            def get(self):
                try:
                    publications = service.dao.get()
                    return service.marshall_many(publications), 200
                except Exception as e:
                    return {'message': 'Error: {}'.format(e)}, 500
    
            @token_required
            def post(self, current_user: User):
                try:
                    assert current_user.patent == Patent.a5FB374A934D584AF or current_user.patent == Patent.aF6A29FB56F7AEEC8
                    file = request.files['file']
                    pub_file = file.read()

                    pub_payload = loads(request.form['request'])
                    pub_payload['pub_file'] = pub_file
                    pub_payload['pub_type'] = PublicationModel.check_publication_type(pub_payload['pub_type'])
                    date = datetime.datetime.strptime(pub_payload['pub_date'], '%d/%m/%Y')
                    pub_payload['pub_date'] = date
                    publication = service.dao.create(pub_payload)

                    return service.marshall_one(publication), 201
                except Exception as e:
                    if e.__class__.__name__ == 'AssertionError':
                        return {'message': 'Forbidden'}, 403
                    else:
                        return {'message': '{}'.format(e)}, 400
    

    class PublicationResource(Resource):
            
            title: str = 'Publication:'
            route: str = '/publications/<int:pub_id>'
        
            def get(self, pub_id):
                try:
                    publication = service.dao.get_by(pub_id=pub_id)
                    return service.marshall_one(publication), 200
                except Exception as e:
                    return {'message': 'Error: {}'.format(e)}, 500
        
            @token_required
            def put(self, pub_id, current_user: User):
                try:
                    assert current_user.patent == Patent.a5FB374A934D584AF or current_user.patent == Patent.aF6A29FB56F7AEEC8
                    file = request.files['file']
                    if file != None:
                        pub_file = file.read()
                        pub_payload = request.form['request']
                        pub_payload['pub_file'] = pub_file
                        publication = service.dao.update(pub_id, pub_payload)
                    else:
                        data = service.namespace.payload
                        publication = service.dao.update(pub_id, data)
                    return service.marshall_one(publication), 200
                except Exception as e:
                    if e.__class__.__name__ == 'AssertionError':
                        return {'message': 'Forbidden'}, 403
                    else:
                        return {'message': '{}'.format(e)}, 400
        
            @token_required
            def delete(self, pub_id, current_user: User):
                try:
                    assert current_user.patent == Patent.a5FB374A934D584AF or current_user.patent == Patent.aF6A29FB56F7AEEC8
                    service.dao.delete(pub_id)
                    return {'message': 'Deleted'}, 200
                except Exception as e:
                    if e.__class__.__name__ == 'AssertionError':
                        return {'message': 'Forbidden'}, 403
                    else:
                        return {'message': '{}'.format(e)}, 400


    class ReadPublicationResource(Resource):
                
            title: str = 'Publication:'
            route: str = '/publications/read/<int:pub_id>'
        
            def get(self, pub_id):
                try:
                    publication: PublicationModel = service.dao.get_one_by(pub_id=pub_id)
                    pub_file = publication.pub_file.decode('ISO-8859-1')
                    
                    return jsonify(
                        {
                            'file': pub_file,
                            'content_type': 'application/pdf', 
                            'filename': f'{publication.pub_title}.pdf',
                            'number_of_pages': publication.pub_number_of_pages,
                            'as_attachment': True
                        }
                    )
                except Exception as e:
                    return {'message': 'Error: {}'.format(e)}, 500


    class DownloadPublicationResource(Resource):
                    
            title: str = 'Publication:'
            route: str = '/publications/download/<int:pub_id>'
        
            def get(self, pub_id):
                try:
                    publication: PublicationModel = service.dao.get_one_by(pub_id=pub_id)
                    return send_file(
                        BytesIO(publication.pub_file), 
                        attachment_filename=f'{publication.pub_title}.pdf', 
                        as_attachment=True
                    )
                except Exception as e:
                    return {'message': 'Error: {}'.format(e)}, 500

    return [PublicationsResource, PublicationResource, ReadPublicationResource, DownloadPublicationResource]
