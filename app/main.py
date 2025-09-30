from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    env = os.getenv("APP_ENV", "dev")

    @app.get("/")
    def index():
        return {"message": f"Hello from {env}!"}

    return app

app = create_app()
