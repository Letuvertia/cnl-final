from flask import Flask, request, jsonify

from sql import MySQLConnector

api = Flask(__name__)

# Sample user data (only for testing)
user_data = [
  {
    "userid": 1,
    "username": "John Doe",
    "password": "123456",
    "email": "john.doe@example.com",
    "location": "New York",
  }
  # {
  #   "username": "Ann Doe",
  #   "password": "56aaaaaa",
  #   "email": "dududud@example.com",
  #   "location": "taiwan",
  #   "userid": 2
  # }
]

message_data = {
        "userid": 1,
        "msg_id": 1,
        "msg_content": "Hello, world!",
        "msg_likes": 0,
        "msg_location": "Test Location"
}

@api.route("/userdata", methods=['POST'])
def get_user_data():
  """Returns user data in JSON format"""
  uid = int(request.args.get('uid'))

  if not uid:
    return jsonify({'error': 'User ID is required'}), 400
  
  if uid in user_db.keys():
    return jsonify(user_db[uid])
  else:
    return jsonify({'error': 'User not found'}), 404
  

import mysql.connector
from mysql.connector import Error


def test_mysql_connector():
    # Create a MySQLConnector instance
    db = MySQLConnector()


    db.add_user(user_data)
    print("User added successfully.")

    # Test fetching user by email
    user_login = db.get_user_login(user_data['email'])
    print("User login details:", user_login)

    # Test fetching user by ID
    user_by_id = db.get_user_id(user_data['userid'])
    print("User by ID details:", user_by_id)


    db.add_msg(message_data)
    print("Message added successfully.")

    # Test fetching the newest message
    newest_msg = db.get_msg_new(user_data['userid'])
    print("Newest message:", newest_msg)

    # Test fetching all messages
    all_msgs = db.get_msg_all(user_data['userid'])
    print("All messages:", all_msgs)

    # Test liking a message
    db.like_msg(message_data['msg_id'], user_data['userid'])
    print("Message liked successfully.")

if __name__ == "__main__":
    test_mysql_connector()

# if __name__ == "__main__":  
#     # test sql
#     connector = MySQLConnector()
#     connector.add_user(user_db[0])
#     user = connector.get_user(1)
#     print(user)

    # start api server
    # api.run(host="0.0.0.0", port=5000)
