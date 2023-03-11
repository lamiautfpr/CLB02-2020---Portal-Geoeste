from ..Entities.Models.SubcategoryModel import SubCategoryModel

class SubcategoryDAO(object):
            
        def __init__(self):
            pass
    
    
        def get(self):
            return SubCategoryModel.get_all()
    
        def get_one(self, subcategory_id):
            return SubCategoryModel.get_one_by(subctg_id=subcategory_id)
        
        def get_by_category(self, category_id):
            return SubCategoryModel.query.filter_by(sub_ctg_id=category_id).all()

    
        def create(self, data):
            return SubCategoryModel.create(
                subctg_id=data['subctg_id'],
                subctg_desc=data['subctg_desc'],
                sub_ctg_id=data['sub_ctg_id'],
            )
    
        def update(self, subcategory_id, data):
            subcategory = self.get(subcategory_id)
            subcategory.subctg_desc=data['subctg_desc']
            subcategory.subctg_atr=data['subctg_atr']
            subcategory.sub_ctg_id=data['sub_ctg_id']
            return subcategory.update_to_db()

        
        def delete(self, subcategory_id):
            subcategory = self.get_one(subcategory_id)
            return subcategory.delete_from_db()
                