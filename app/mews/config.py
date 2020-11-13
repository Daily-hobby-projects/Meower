

class DevConfig:
    SQLALCHEMY_DATABASE_URI='sqlite:///mews.db'
    SECRET_KEY='secrets'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    DEBUG=True