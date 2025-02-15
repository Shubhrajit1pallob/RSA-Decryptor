from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "Hi1/tanI/sinx"

    with app.app_context():
        # Import routes here to avoid circular imports
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app