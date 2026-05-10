"""Starter Flask application for Phase 1 project structure."""

from flask import Flask, jsonify


def create_app() -> Flask:
    """Create the application with a minimal health endpoint."""
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "phase": "project-structure"})

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
