import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(host='localhost', user='root', password='heet',port='3306', database='d_mart')

  return __cnx

