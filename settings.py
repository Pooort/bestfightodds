import os

PROJECTPATH = os.path.dirname(os.path.realpath(__file__))
SQLITEPATH = os.path.join(PROJECTPATH, 'data.db')
DBCONNECTION = 'sqlite:////{}'.format(SQLITEPATH)
