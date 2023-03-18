#server side
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from ClassGetProcessing import Process
from ClassPostAddNewMovie import AddNewMovie
from classPostUpdatePostData import UpdatePostData
from ClassPostAnalystFromPost import AnalystPost

app = Flask(__name__)
api = Api(app)
CORS(app)

# Called by ML-Frontend
api.add_resource(Process,"/start-one-process")
api.add_resource(AnalystPost,"/start-analyst-one-post")

# Called by Normal Backend
api.add_resource(AddNewMovie,"/add-new-movie") 
api.add_resource(UpdatePostData,"/update-post") 

if __name__ == "__main__":
    app.run(debug=True, port=5556)
    #Change debug to false when deploy
    
    
    
    