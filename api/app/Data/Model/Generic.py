from app import db

class Generic(db.Model):
    __abstract__ = True

    db = db

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def get_one_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_or_create(cls, **kwargs):
        instance = cls.get_one_by(**kwargs)
        if instance:
            return instance
        else:
            instance = cls(**kwargs)
            instance.add_to_db()
            return instance

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.add_to_db()
        return instance

    @classmethod
    def getPriKey(self):
        return self.__table__.primary_key.columns.keys()[0]