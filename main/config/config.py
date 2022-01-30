import os
from dotenv import load_dotenv


def _load_configuration():
    env = os.getenv("COLLECTIVE_ENV")

    if not env:
        raise EnvironmentError("COLLECTIVE_ENV 환경 변수를 찾을 수 없습니다."
                               "해당 환경 변수에 DEV 또는 TEST")

    basedir = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(basedir, f"{env.lower()}.env")

    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"{config_path}를 찾을 수 없습니다.")

    load_dotenv(dotenv_path=config_path, encoding="UTF-8")


_load_configuration()


def _get_conn_str(user, pwd, host, database):
    return f"mysql+pymysql://{user}:{pwd}@{host}/{database}"




class Config:
    # ENV = os.getenv("ENV")
    DEBUG = os.getenv("DEBUG")
    TESTING = os.getenv("TESTING")
    RUN_HOST = os.getenv("RUN_HOST")
    RUN_PORT = os.getenv("RUN_PORT")
    DB_CONNECTION_STRING = _get_conn_str(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_DATABASE"))
    # SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    LOG_FILENAME = os.getenv("LOG_FILENAME")
