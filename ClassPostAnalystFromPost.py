from flask_restful import Resource
from flask import Response
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase
import pymysql
from FuncWordTokenize import wordTokenize, countDuplicate
from FuncSave2DB import saveKeyword2db
from FuncCountKeyword import countKeyword

class AnalystPost(Resource):
  def post(self):

      connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
      mycursor = connection.cursor()
      mycursor.execute("\
        SELECT id, postId, tmdbId, detail \
        FROM Moviefrompost \
        WHERE Moviefrompost.isUsed = 0\
        LIMIT 1")
      post = mycursor.fetchone()
      connection.commit()
      connection.close()
      
      if(post==None):
        return Response("No data to Analyst", status=204, mimetype='application/json')
      
      tableName = 'Moviefrompost'
      id = post[0]
      postId = post[1]
      tmdbId = post[2]
      detail = post[3]

      keywordList = wordTokenize(detail)
      #print(keywordList)

      object_list = countDuplicate(keywordList)
      #print(object_list)

      saveKeyword2db(tableName,id,object_list,tmdbId,postId)
      countKeyword(list(set(keywordList)))
   
      return Response("Success in Analyst of PostId = "+str(postId), status=200, mimetype='application/json')
  