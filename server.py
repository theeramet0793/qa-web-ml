#server side
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from FuncWordTokenize import word_tokenize
from ClassProcess import Process

#==== Class method Post ============================================
from ClassTriggerHasNewPost import TriggerHasNewPost

app = Flask(__name__)
api = Api(app)
CORS(app)

# POST 
#api.add_resource(TriggerHasNewPost,"/hasnewpost") #support {params:{ a:1, b:2}}
api.add_resource(Process,"/hasnewpost") #support {params:{ a:1, b:2}}

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    #Change debug to false when deploy
    
    #=== Main Process ==================================================
    
    