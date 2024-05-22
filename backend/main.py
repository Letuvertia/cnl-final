from flask import Flask, request, jsonify,SQLAlchemy
from init_db import Message
#for the test new branch
api = Flask(__name__)

# Sample user data (replace with your data source)
user_db = {
  123: {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "id": 123
  },
  124: {
    "name": "Ann Doe",
    "email": "ann.doe@example.com",
    "id": 124
  }
}

@api.route("/userdata")
def get_user_data():
  """Returns user data in JSON format"""
  uid = int(request.args.get('uid'))
  if uid in user_db.keys():
    return jsonify(user_db[uid])
  else:
    return "User Not Found"
  
@api.route("/userdata")
def get_msg_api():
  # messages = Message.query.all()
  # return jsonify([{
  #   'id':messages.id,
  #   'content':messages.value,
  #   'row':messages.row_number,}])
  return "Hello, World!"

@api.route("/userdata")
def store_msg_api(msg):
  messages_data = request.get_json()
  messages = Message(
    id = messages_data['id'],
    content = messages_data['value'],
  )
  db = SQLAlchemy(api)
  db.session.add(messages)
  db.session.commit()
  return jsonify({'status':'success store msg'}),201



if __name__ == "__main__":
  api.run(host="0.0.0.0", port=5000)
