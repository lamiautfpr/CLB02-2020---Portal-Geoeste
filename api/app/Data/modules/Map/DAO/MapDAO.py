from ..Entities.Models.MapModel import MapModel

class MapDAO(object):

        def __init__(self):
            pass


        def get(self):
            return MapModel.get_all()

        def get_one(self, map_id):
            return MapModel.get_one_by(map_id=map_id)

        def get_by(self, **kwargs):
            return MapModel.get_by(**kwargs)
        

        def create(self, data):
           return MapModel.create(
                map_id=data['map_id'],
                map_desc=data['map_desc'],
                map_atr=data['map_atr'],
                map_ctg=data['map_ctg'],
                choropleth=data['choropleth'],
                map_subctg_id=data['map_subctg_id'],
            )


        def update(self, map_id, data):
            map = self.get_one(map_id)

            map.map_desc=data['map_desc']
            map.map_atr=data['map_atr']
            map.map_ctg=data['map_ctg']
            map.choropleth=data['choropleth']
            map.map_subctg_id=data['map_subctg_id']
            return map.update_to_db()


        def delete(self, map_id):
            map = self.get_one(map_id)
            return map.delete_from_db()

