
from flask_restful import Resource
from flask import Response
from flask import request
import pymysql
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

class AddNewMovie(Resource):
  def post(self):
      a = request.json
      tmdbId = a.get("tmdbId")
      movieName = a.get('movieName')
      
      connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
      mycursor = connection.cursor()
      mycursor.execute("\
        INSERT INTO Movie( tmdbId, name)\
        VALUES (%s,%s)",(tmdbId,movieName))
      connection.commit()
      connection.close()
    
      return Response("OK", status=200, mimetype='application/json')