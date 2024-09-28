from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient('mongodb+srv://test:sparta@cluster0.roiwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

# Initialize Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# POST route to handle comments submission
@app.route("/homework", methods=["POST"])
def homework_post():
    # Receiving data from the form
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    
    # Create a document to insert into MongoDB
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    
    # Insert document into the collection
    db.fanmessages.insert_one(doc)
    
    # Return a success message
    return jsonify({'msg': 'Comment posted successfully!'})

# GET route to retrieve comments
@app.route("/homework", methods=["GET"])
def homework_get():
    # Retrieve all comments from MongoDB, excluding the '_id' field
    message_list = list(db.fanmessages.find({}, {'_id': False}))
    
    # Return the list of messages as JSON
    return jsonify({'messages': message_list})

# Start the Flask app
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
