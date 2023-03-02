from FuncWordTokenize import wordTokenize
import collections
import pymysql
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

class FindMovie():
  
    def findWithDetail(postDetail):
      keyword2movies = collections.OrderedDict()
      movieId2freq = collections.OrderedDict()
      keywordList = wordTokenize(postDetail)

      connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword, db=connectionDatabase)
      mycursor = connection.cursor()
      
      for keyword in keywordList:
          mycursor.execute("\
            SELECT tmdbId\
            FROM keywordmovie \
            WHERE keywordmovie.keyword = %s",(keyword))
          movieTuple = mycursor.fetchall()
          connection.commit()
          tempMovieList = []
          for columns in movieTuple:
            tempMovieList.append(columns[0])
          keyword2movies[keyword] = list(dict.fromkeys(tempMovieList))
      
      for key, value in keyword2movies.items():
        #print(key," = ",value)
        for movieId in value:
          if(movieId in movieId2freq):
            movieId2freq[movieId] += 1
          else:
            movieId2freq[movieId] = 1
      
      sortedMovieId2Freq = dict(sorted(movieId2freq.items(), key=lambda x:x[1], reverse=True))
      # for key,value in sortedMovieId2Freq.items():
      #   print(key," = ",value)

      return sortedMovieId2Freq