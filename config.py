import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") == "1"  # Check explicitly for "1"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = [
        os.environ.get("ADMIN_EMAIL") or "admin@example.com"
    ]  # Default admin email
    POSTS_PER_PAGE = 25
