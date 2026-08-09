"""Simple Flask service for ECS Fargate deployment."""
import os
import socket
from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/health")
    def healthcheck():
        return jsonify(status="healthy", service="ecs-fargate-demo"), 200

    @app.route("/")
    def index():
        return jsonify(
            message="Hello from ECS Fargate",
            hostname=socket.gethostname(),
            environment=os.getenv("APP_ENV", "dev"),
        ), 200

    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", "80"))
    create_app().run(host="0.0.0.0", port=port, debug=False)
