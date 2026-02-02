import pymysql

pymysql.install_as_MySQLdb()

# Fake mysqlclient version for Django 6+
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.__version__ = "2.2.1"