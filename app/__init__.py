from .extensions import db, migrate

from flask import Flask
from flask_admin import Admin

from flask_admin.contrib.geoa import ModelView


def create_app(extra_config_settings={}):
    app = Flask(__name__)

    app.config.from_object('app.config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import blueprints
    blueprints(app)

    admin = Admin(app, 
                name='Example: GeoAlchemy',
                template_mode='bootstrap4')
    
    from .models.geometry import Point, MultiPoint, Polygon, MultiPolygon, LineString, MultiLineString
    admin.add_view(ModelView(Point, db.session, category='Points'))
    admin.add_view(ModelView(MultiPoint, db.session, category='Points'))
    admin.add_view(ModelView(Polygon, db.session, category='Polygons'))
    admin.add_view(ModelView(MultiPolygon, db.session, category='Polygons'))
    admin.add_view(ModelView(LineString, db.session, category='Lines'))
    admin.add_view(ModelView(MultiLineString, db.session, category='Lines'))

    return app