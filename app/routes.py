from .views import views_bp


def route(app):
    app.register_blueprint(views_bp)
