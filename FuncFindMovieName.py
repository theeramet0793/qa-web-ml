
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase
import pymysql


def FindMovieNameByTMDBId(movieTmdbId):
    connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
    mycursor = connection.cursor()
    mycursor.execute("\
      SELECT movie.name\
      FROM movie\
      WHERE movie.tmdbId = %s",(movieTmdbId))
    data = mycursor.fetchone()
    connection.commit()
    connection.close()
    
    movieName = data[0]
    
    return movieName