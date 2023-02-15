
import pymysql
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

def fetch_data_from_facebook_db():
  connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
  mycursor = connection.cursor()
  mycursor.execute("\
    SELECT id, tmdbId, detail, isUsed\
    FROM moviefromfbg\
    WHERE moviefromfbg.isUsed = 0\
    LIMIT 1")
  data = mycursor.fetchall();
  connection.commit()
  connection.close()
  return data