from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get(
    'DATABASE_URI').replace('postgres://', 'postgresql://', 1)

SECRET_KEY = environ.get('SECRET_KEY')
