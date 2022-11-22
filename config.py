# config information about databases

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'messagedb'
USERNAME = 'root'
PASSWORD = '86270924'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "asbdabsfbbfajshjfhfgh"

#email config
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "811035239@qq.com"
MAIL_PASSWORD = "lfgyksiikfnxbeia"
MAIL_DEFAULT_SENDER = "811035239@qq.com"
