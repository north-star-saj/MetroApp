from flask import Flask


def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import metro

    app.register_blueprint(metro.bp)
    app.add_url_rule("/", endpoint="index")

    return app
