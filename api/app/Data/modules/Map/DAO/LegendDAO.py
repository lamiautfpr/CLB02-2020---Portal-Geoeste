from ..Entities.Models.LegendModel import LegendModel

class LegendDAO(object):
    
        def __init__(self):
            pass
    
    
        def get(self):
            return LegendModel.get_all()
    
        def get_one(self, leg_id):
            return LegendModel.get_one_by(leg_id=leg_id)
        
        def get_by(self, **kwargs):
            return LegendModel.get_by(**kwargs)
        
    
        def create(self, data):
            return LegendModel.create(
                atr=data['atr'],
                color=data['color'],
                leg_map_id=data['leg_map_id']
            )


        def update(self, leg_id, data):
            legend = self.get_one(leg_id)
            legend.atr=data['atr']
            legend.color=data['color']
            legend.leg_map_id=data['leg_map_id']
            return legend.update_to_db()


        def delete(self, leg_id):
            legend = self.get_one(leg_id)
            return legend.delete_from_db()