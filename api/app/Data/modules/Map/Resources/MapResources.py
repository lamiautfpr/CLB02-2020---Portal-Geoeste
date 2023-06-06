from io import BytesIO
import os
import sys
import zipfile
from sqlalchemy import create_engine
from app.Data.modules.Map.Resources.file_handling.map_data_upload import MapDataUpload
from werkzeug.utils import secure_filename
from shutil import rmtree
from app.Auth.auth import token_required
from app import db
from app.Auth.models import Patent, User
from app.Errors.exceptions import NotFoundException
from app.Protocols.Protocols import ServiceProtocol
from app.Data.modules.Map.Entities.Schemas.MapSchema import map_validation_schema, map_update_validation_schema
from configs.Configs import config
from flask_restx import Resource
from flask_cors import cross_origin
from flask import request, send_file
import geopandas as gpd
from json import loads


def init_map_resources(service: ServiceProtocol):

    def check_data(data, title):
        if len(data)  > 0:
            return True
        else:
            raise NotFoundException("Nothing Found for {}".format(title))

    class MapsResource(Resource):

        title: str = 'Maps:'
        route: str = '/mapas'

        def get(self):
            try:
                maps = service.dao.get()
                assert(len(maps) > 0)
                return service.marshall_many(maps), 200
            except Exception as e:
                return {'message': 'Error: {}'.format(e)}, 500
                

        @token_required
        def post(self, current_user: User):
            try:
                assert current_user.patent == Patent.a5FB374A934D584AF or current_user.patent == Patent.aF6A29FB56F7AEEC8
                file = request.files['file']
                data_file = file.read()
                map_payload = loads(request.form['request'])
                map_payload['map_id'] = secure_filename(file.filename).replace('.zip', '')
                map_payload['data_file'] = data_file
                map = service.dao.create(map_payload)

                data_upload = MapDataUpload(file=file, atr=map_payload['map_atr'])
                data_upload.upload_proccess()

                return service.marshall_one(map), 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    print(e)
                    return {'message': '{}'.format(e)}, 400

    
    class MapsByCategoryResource(Resource):
        
        title: str = 'Maps by Category:'
        route: str = '/mapas/category/<string:map_ctg>'

        def get(self, map_ctg):
            self.title = self.title + " {}".format(map_ctg)
            maps = service.dao.get_by(map_ctg=map_ctg)
            check_data(maps, self.title)
            return service.marshall_many(maps), 200
                

    class MapsBySubcategoryResource(Resource):
        title: str = 'Maps by Subcategory:'
        route: str = '/mapas/subcategorias/<string:subctg_id>'
        def get(self, subctg_id):
            try:
                self.title = self.title + " {}".format(subctg_id)
                maps = service.dao.get_by(map_subctg_id=subctg_id)
                check_data(maps, self.title)
                return service.marshall_many(maps), 200
            except:
                return {'message': 'Error: Not Found'}, 404


    class MapResource(Resource):

        route = '/mapas/<string:map_id>'
        title= 'Map:'
        
        def get(self, map_id):
            try:
                map = service.dao.get_one_by(map_id=map_id)
                assert map is not None
                return service.marshall_one(map), 200
            except:
                return {"Error":"Not found"}, 404
        

        @token_required
        def put(self, current_user: User, map_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) or current_user.check_permission(Patent.aF6A29FB56F7AEEC8) is not False
                file = request.files['file']

                if file:
                    map_payload['map_id'] = secure_filename(file.filename).replace('.zip', '')
                    data_file = file.read()
                    map_payload['data_file'] = data_file
                    data_upload = MapDataUpload(file=file, atr=map_payload['map_atr'])
                    data_upload.upload_proccess()
                else:
                    map_payload=service.namespace.payload
                    map=service.dao.update(map_id, map_payload)
                    return {"Message":"Map updated"}, 201
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': f'{e}'}, 400

        @token_required
        def delete(self, current_user: User, map_id):
            try:
                assert current_user.check_permission(Patent.a5FB374A934D584AF) or current_user.check_permission(Patent.aF6A29FB56F7AEEC8) is not False
                service.dao.delete(map_id)
                sql = f'DROP TABLE IF EXISTS {map_id}'
                db.engine.execute(sql)
                return {"Message":"Map deleted"}, 200
            except Exception as e:
                if e.__class__.__name__ == 'AssertionError':
                    return {'message': 'Forbidden'}, 403
                else:
                    return {'message': 'Not Found'}, 404
                
    
    class MapDataResource(Resource):

        route = '/mapas/resource/<string:map_id>'
        def get(self, map_id):
            try:
                map = service.dao.get_one_by(map_id=map_id)
                atr = map.map_atr
                
                if map and not map.static:
                    if map.map_atr:
                        if map.map_ctg != None and map.map_ctg != 'Geologia':
                            sql=f'SELECT geometry, colors_{atr} as colors, NOME, {atr} as atr FROM {map.map_ctg}';  
                        else:
                            sql=f'SELECT geometry, colors, {atr} as atr FROM ' + map.map_id
                    df=gpd.read_postgis(sql, config.SQLALCHEMY_DATABASE_URI, geom_col='geometry')
                    geodf=df.to_json()
                    return geodf, 200
                else:
                    return {"Error":"Resource Not found"}, 404
            except Exception as e:
                return {"Error":f"{e}"}, 404


    class MapDownloadResource(Resource):
        route = '/mapas/<string:map_id>/download'
        """        

        @token_required        
        def get(self, current_user: User, map_id):
            try:
                mapa = service.dao.get_one_by(map_id=map_id)
                if mapa:
                    return send_file(BytesIO(mapa.data_file), attachment_filename=mapa.map_id + '.zip', as_attachment=True)
                else:
                    return {"Error":"No data found"}, 404

            except Exception as e:
                return {"Error":"{}".format(e)}, 404
        """    

    return [
                MapsResource, MapsByCategoryResource, MapsBySubcategoryResource, MapResource, 
                MapDataResource, MapDownloadResource
           ]
