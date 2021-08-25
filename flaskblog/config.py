import os


class Config:
    SECRET_KEY = '681cb3b56395fcc937ab940f15dc66c5'
    CKEDITOR_PKG_TYPE = 'basic'
    uri = os.environ.get("DATABASE_URL")    
    uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = os.environ.get(uri)
    