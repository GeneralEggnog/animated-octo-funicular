import os


class Config:
    SECRET_KEY = '681cb3b56395fcc937ab940f15dc66c5'
    CKEDITOR_PKG_TYPE = 'basic'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    