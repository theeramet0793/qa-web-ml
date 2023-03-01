import pymysql
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

def fetch_sorted_keyword_db():
  connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
  mycursor = connection.cursor()
  mycursor.execute("\
    SELECT *\
    FROM keywordcount\
    ORDER BY freq DESC")
  data = mycursor.fetchall();
  connection.commit()
  connection.close()
  
  for item in data:
    print(item) 

fetch_sorted_keyword_db()