from .extensions import app
from .routes import init_routes

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)