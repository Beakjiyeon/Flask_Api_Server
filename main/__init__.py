from flask import Flask

app = Flask(__name__)

from flask_cors import CORS

CORS(app)

from flask_sqlalchemy import SQLAlchemy

app_db = SQLAlchemy()

from flask_migrate import Migrate

migrate = Migrate()

test = {}

from flask import g
import time


@app.before_request
def every_request():
    g.start = time.time()
    test.clear()
    g.test = test


from .dto.response import *


@app.after_request
def final_return(response):
    res = response.json
    if res["code"] == ResponseCode.OK.code:
        logger.info(f"{res['code']} - {time.time() - g.start}")
    else:
        logger.error(f"{res['code']} - {time.time() - g.start} - {res['message']}")
    return response


@app.errorhandler(Exception)
def handle_bad_request(e):
    status = ResponseCode.ERROR.code if not hasattr(e, 'code') or e.code == None else e.code
    error_message = e.error_message if type(e) == ParameterException or type(
        e) == ApiException else ResponseCode.ERROR.message if status == ResponseCode.ERROR.code else str(e)[4:]
    print(str(e))
    return ApiResponse(status, error_message)


from .config.config import *


def configure_settings(app):
    app.config.update({
        'DEBUG': Config.DEBUG,
        'TESTING': Config.TESTING
    })


def configure_blueprints(app):
    from .controller.v0 import v0_controller as v0
    app.register_blueprint(v0.api_v0, url_prefix='/v0')

    from .controller.v1 import board_controller as bc_v1, monitoring_controller as mc_v1, query_controller as qc_v1
    app.register_blueprint(bc_v1.board_api, url_prefix='/v1/board-service')
    app.register_blueprint(mc_v1.monitoring_api, url_prefix='/v1/monitoring-service')
    app.register_blueprint(qc_v1.query_api, url_prefix='/v1/query-service')

    from .controller.v2 import board_controller as bc_v2, monitoring_controller as mc_v2, query_controller as qc_v2
    app.register_blueprint(bc_v2.board_api, url_prefix='/v2/board-service')
    app.register_blueprint(mc_v2.monitoring_api, url_prefix='/v2/monitoring-service')
    app.register_blueprint(qc_v2.query_api, url_prefix='/v2/query-service')


def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_CONNECTION_STRING
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    app_db.init_app(app)
    migrate.init_app(app, app_db)


from main.log.log_formatter import RequestFormatter


def configure_logging(app):
    import logging
    logger = logging.getLogger('api_logger')
    from concurrent_log_handler import ConcurrentRotatingFileHandler

    file_handler = ConcurrentRotatingFileHandler(Config.LOG_FILENAME, maxBytes=10000, backupCount=1, encoding='UTF-8')
    formatter = RequestFormatter(
        '[%(asctime)s] - %(levelname)s - %(remote_addr)s - [%(url)s] - %(message)s'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


configure_settings(app)
connect_db(app)
configure_blueprints(app)
logger = configure_logging(app)
