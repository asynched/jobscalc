from os import environ
from dotenv import load_dotenv

load_dotenv()

ENV = environ.get("ENV")
SECRET_KEY = environ.get("SECRET_KEY")
DATABASE_ENGINE = environ.get("DATABASE_ENGINE")
DATABASE_NAME = environ.get("DATABASE_NAME")
DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_PORT = environ.get("DATABASE_PORT")
