from flask_restful import Resource
import json
from flask import Response, request
import requests
from Const import api_url_for_get_new_solved_post 
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase
import pymysql

class UpdatePostData(Resource):
  def post(self):
      a = request.json
      postId = a.get("postId")
      tmdbId = a.get("tmdbId")
      postDetail = a.get('postDetail')
      
      if(tmdbId == None):
        tmdbId = '0'

      if(postId == None ):
        return Response("postId is required", status=400, mimetype='application/json')
      if(tmdbId ==  None ):
        return Response("tmdbId is required", status=400, mimetype='application/json')
      if(postDetail == None):
        return Response("postDetail is required", status=400, mimetype='application/json')
      
      connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
      mycursor = connection.cursor()
      
      # Delete duplicate data
      mycursor.execute("\
        DELETE FROM Moviefrompost WHERE Moviefrompost.postId = %s",(postId))
      connection.commit()
      
      # Delete duplicate data
      mycursor.execute("\
        DELETE FROM Keywordmovie WHERE Keywordmovie.fromPostId = %s",(postId))
      connection.commit()
      
      print(tmdbId, type(tmdbId))
      if(tmdbId != 0):
        mycursor.execute("\
          INSERT INTO Moviefrompost(postId, tmdbId, detail, isUsed)\
          VALUES(%s, %s, %s, %s)",(postId,tmdbId,postDetail,'0'))
        connection.commit()
      connection.close()
      
      return Response("Success in sync data of postID = "+str(postId), status=200, mimetype='application/json')
