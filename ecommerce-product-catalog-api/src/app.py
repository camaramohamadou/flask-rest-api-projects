from flask import Flask
from src.routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main, url_prefix='/api')

    @app.route('/')
    def home():
        return "Welcome to the E-commerce Product Catalog API!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
