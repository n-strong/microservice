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

# define MongoDB client
client = pymongo.MongoClient(dbURI)

# define MongoDB collection 
collection = client.test['test_post'] # test attribute is database and ['test_post'] is collection within database

# handle requests from frontend
@app.route('/blog_post', methods=['POST'])
@cross_origin(origins=['http://localhost:3000'])
def blog_post():

    # post data from front end
    user_input = request.json 
   
   # try posting data to MongoDB and handle any errors 
    try:
        post(user_input)
        print('Posted user post to database')

    except Exception as e:
        print('Unable to make user post at this time because: %s\n', e)
   
    return jsonify(user_input) 

# function to handle post requests for MongoDB
def post(blog_post):
    # inserts document into database collection 
    collection.insert_one(blog_post)
 

@app.route('/get_blog_posts', methods=['POST'])
@cross_origin(origins=['http://localhost:3000'])
def fetch():
    username = request.json['username']
    posts = get_blog_posts(username)
    return jsonify({'posts': posts})
   
def get_blog_posts(username):
    docs = collection.find({'username': username})
   
    # unpack docs object and store 'posts' in list 
    posts = [doc['post'] for doc in docs]
    
    return posts

if __name__ == '__main__':
    app.run(debug=True)