import collections
import json
from flask_restful import Resource
import pymysql
from flask import request, Response
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

def saveKeyword2db(tableName, id_in_table, keywordList, tmdbId):
  connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
  mycursor = connection.cursor()
  
  #Mark raw data row that already used
  mycursor.execute("\
  UPDATE "+tableName+"\
  SET isUsed = 1\
  WHERE id = %s",(id_in_table))
  connection.commit()
  
  #Loop for save keyword to db
  for keyword in keywordList:
    mycursor.execute("\
      INSERT INTO keywordmovie(tmdbId, keyword)\
      VALUES(%s,%s)",(tmdbId, keyword))
    connection.commit()
  
  connection.close()
