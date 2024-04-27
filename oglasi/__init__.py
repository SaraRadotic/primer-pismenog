from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='0140d7e9-6189-4d9b-8d20-7d7e067bf11e',
        DATABASE=os.path.join(app.instance_path, 'oglasi.sqlite'),
    )

    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    @app.route("/heartbeat", methods=["GET"])
    def heartbeat():
        return "OK", 200

    return app

