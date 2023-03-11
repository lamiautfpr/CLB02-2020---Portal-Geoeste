from typing import Type


class GenericDAO(object):
    model: Type
    primary_key: str

    def __init__(self, model: Type):
        self.model = model
        self.primary_key = self.model.getPriKey()


    def get(self) -> list:
        return self.model.get_all()


    def get_one(self, id):
        return self.model.get_one_by(**{self.primary_key:id})


    def get_one_by(self, **kwargs):
        return self.model.get_one_by(**kwargs)
        

    def get_by(self, **kwargs) -> list:
        return self.model.get_by(**kwargs)


    def create(self, data):
        return self.model.create(**data)


    def update(self, id, data):
        model = self.get_one(id)
        for key, value in data.items():
            setattr(model, key, value)
        return model.update_to_db()


    def delete(self, id):
        model = self.get_one(id)
        return model.delete_from_db()