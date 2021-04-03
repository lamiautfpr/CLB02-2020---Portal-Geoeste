from .main import bp


def blueprints(app):
    app.register_blueprint(bp)