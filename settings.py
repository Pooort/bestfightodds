import os

PROJECTPATH = os.path.dirname(os.path.realpath(__file__))
SQLITEPATH = os.path.join(PROJECTPATH, 'data.db')
DBCONNECTION = 'sqlite:////{}'.format(SQLITEPATH)
#DBCONNECTION = 'postgres://zkgjbiyo:0apXlSXRyZhDSxqcuYYpd97tOb220ho2@baasu.db.elephantsql.com:5432/zkgjbiyo'