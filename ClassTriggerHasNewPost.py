
from flask_restful import Resource
import json
from flask import Response, request
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase
import pymysql
from datetime import date, datetime


class TriggerHasNewPost(Resource):
  
  def post(self):
    a = request.args
    args = a.to_dict()

    today = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")
    
    connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
    mycursor = connection.cursor()
    mycursor.execute("\
        SELECT statuslog.status\
        FROM statuslog \
        ORDER BY statuslog.date DESC, statuslog.time DESC\
        LIMIT 1",())
    last_status = mycursor.fetchone()
    connection.commit()
    
    if(last_status == None or last_status[0] == 'Stop'):
      mycursor.execute("\
        INSERT INTO statuslog( status , date, time)\
        VALUES(%s,%s,%s)",('Start',today,current_time))
      connection.commit()
      self.isSwitchOn = True
      return Response('Starting ML success', status=200, mimetype='application/json')
    
    if(last_status[0] == 'Start'):
      return Response('ML is processing', status=200, mimetype='application/json')
