API_KEY = "supersecret123"

from flask import Flask
from .models import db
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stories.db"
    db.init_app(app)
    app.register_blueprint(bp)
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
