from ..Entities.Models.ReferencyModel import ReferencyModel

class ReferencyDAO(object):
        
            def __init__(self):
                pass
        
        
            def get(self):
                return ReferencyModel.query.all()
        
            def get_one(self, referency_id):
                return ReferencyModel.query.filter_by(referency_id=referency_id).first()
            
            def get_by(self, **kwargs):
                return ReferencyModel.query.filter_by(**kwargs).all()
                
        
            def create(self, data):
                return ReferencyModel.create(
                    ref_id=data['ref_id'],
                    src=data['src'],
                    fontes=data['fontes'],
                    elaboracao=data['elaboracao'],
                    base_cartografica=data['base_cartografica'],
                )

        
            def update(self, referency_id, data):
                referency = self.get_one(referency_id)
                referency.src=data['src']
                referency.fontes=data['fontes']
                referency.elaboracao=data['elaboracao']
                referency.base_cartografica=data['base_cartografica']
                return referency.update_to_db()


            def delete(self, referency_id):
                referency = self.get_one(referency_id)
                return referency.delete_from_db()
