from ..Entities.Models.CategoryModel import CategoryModel

class CategoryDAO(object):
        
        def __init__(self):
            pass
    
    
        def get(self):
            return CategoryModel.get_all()
    
        def get_one(self, category_id):
            return CategoryModel.get_one_by(ctg_id=category_id)

    
        def create(self, data):
            return CategoryModel.create(
                ctg_desc=data['ctg_desc'],
            )

    
        def update(self, category_id, data):
            category = self.get_one(category_id)
            category.ctg_desc=data['ctg_desc']
            return category.update_to_db()

        
        def delete(self, category_id):
            category = self.get_one(category_id)
            return category.delete_from_db()