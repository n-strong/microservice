# install Flask server
from flask import Flask, request, jsonify
import os
import pymongo
from dotenv import load_dotenv, find_dotenv
# dependency to handle cross origin requests (Node.js --> Flask)
from flask_cors import CORS, cross_origin

# Flask instance
app = Flask(__name__)
CORS(app)

# get environment variables
find_env_path = find_dotenv()
load_dotenv()

dbURI = os.environ['LOGININFO']

# handle requests from frontend
@app.route('/blog_post', methods=['POST'])
@cross_origin(origins=['http://localhost:3000'])
def blog_post():
    
    # define post container
    user_dict = {}

    # post data from front end
    user_input = request.json 
    username = user_input['username'] 
  
    # username as key and post data as value
    user_dict[username] = user_input['post']
   
   # try posting data to MongoDB and handle any errors 
    try:
        post(user_dict)
        print('Posted user post to database')
    
    except Exception as e:
        print('Unable to make user post at this time because: %s\n', e)
   
    return jsonify(user_dict) # send signal to webpage to reload after blog post received

# function to handle post requests for MongoDB
def post(blog_post):
    # define MongoDB client
    client = pymongo.MongoClient(dbURI)

    # define MongoDB collection 
    collection = client.test['test_post'] # test attribute is database and ['test_post'] is collection within database

    # inserts document into database collection 
    collection.insert_one(blog_post)
    

if __name__ == '__main__':
    app.run(debug=True)