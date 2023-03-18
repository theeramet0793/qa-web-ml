
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase
import pymysql


def FindMovieNameByTMDBId(movieTmdbId):
    #print('tmdbId=',movieTmdbId)
    connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
    mycursor = connection.cursor()
    mycursor.execute("\
      SELECT Movie.name\
      FROM Movie\
      WHERE Movie.tmdbId = %s",(movieTmdbId))
    data = mycursor.fetchone()
    connection.commit()
    connection.close()
    
    movieName = data[0]
    
    return movieName