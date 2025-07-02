from .travel import travel_bp

def init_routes(app):
    app.register_blueprint(travel_bp)
