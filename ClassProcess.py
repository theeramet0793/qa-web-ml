from flask_restful import Resource
import json
from flask import Response, request
import requests
from Const import api_url_for_get_post, api_url_for_post_movie_list
from ClassFindMovie import FindMovie
from FuncFindMovieName import FindMovieNameByTMDBId

class Process(Resource):
  def post(self):
    x = 1
    while(x==1):
      x = 0
      req = requests.get(api_url_for_get_post)
      data = req.json()
      
      if(len(data) == 0):
        break
      
      movieDict = FindMovie.findWithDetail(postDetail=data['postDetail'])
      movieList = (createMovieObjList(movieDict))
      body = {
        "postId":data['postId'],
        "movielist":movieList
      }
      requests.post(api_url_for_post_movie_list, json=body)
      
    return 'End of ML process'
  
def createMovieObjList(movieDict):
    mylist = []
    for key, value in movieDict.items():
      mylist.append(createMovieObj(key, value))
    return mylist
  
def createMovieObj(tmdbId, freq):
    obj = {
      "tmdbId":tmdbId,
      "name":FindMovieNameByTMDBId(tmdbId),
      "freq":freq
    }
    return obj