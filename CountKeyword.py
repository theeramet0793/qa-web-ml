
import pymysql
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

def countKeyword(keywordList):
  connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
  mycursor = connection.cursor()
  for keyword in keywordList:
    mycursor.execute("\
      INSERT INTO keywordcount( keyword, freq)\
      VALUES(%s, %s)\
      ON DUPLICATE KEY\
      UPDATE freq = freq + 1",(keyword, 1))
    connection.commit()
  connection.close()
