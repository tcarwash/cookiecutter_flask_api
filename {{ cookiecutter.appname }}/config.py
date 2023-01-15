import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "verySupeRS3cret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APIFAIRY_TITLE = "{{ cookiecutter.appname }}"
    APIFAIRY_VERSION = "1.0"
    APIFAIRY_UI_PATH = "/api/docs"
