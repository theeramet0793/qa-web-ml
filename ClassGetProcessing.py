from flask_restful import Resource
import json
from flask import Response, request
import requests
from Const import api_url_for_get_post, api_url_for_post_movie_list
from ClassFindMovie import FindMovie
from FuncFindMovieName import FindMovieNameByTMDBId
from itertools import islice

class Process(Resource):
  def get(self):

    req = requests.get(api_url_for_get_post)
    data = req.json()
      
    if(len(data) > 0):
      movieDict = FindMovie.findWithDetail(postDetail=data['postDetail'])
      movieList = (createMovieObjList(movieDict))
      body = {
        "postId":data['postId'],
        "userId":data['userId'],
        "movielist":movieList
      }
      requests.post(api_url_for_post_movie_list, json=body)
      
      l = json.dumps(body)
      return json.loads(l)
    else:
      return Response("No new post to process", status=204, mimetype='application/json')
  
def createMovieObjList(movieDict):
    mylist = []
    for key, value in movieDict.items():
      mylist.append(createMovieObj(key, value))
    return mylist #mylist[0:3]
  
def createMovieObj(tmdbId, freq):
    obj = {
      "tmdbId":tmdbId,
      "name":FindMovieNameByTMDBId(tmdbId),
      "freq":freq
    }
    return obj