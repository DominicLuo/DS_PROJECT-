import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-long-and-unique-key-that-nobody-knows'
    SQLALCHEMY_DATABASAE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
