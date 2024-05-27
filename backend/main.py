from flask import Flask, request, jsonify

from sql import MySQLConnector

api = Flask(__name__)

from ex_db_data import user_data, message_data


# @api.route("/userdata", methods=['POST'])
# def get_user_data():
#   """Returns user data in JSON format"""
#   uid = int(request.args.get('uid'))

#   if not uid:
#     return jsonify({'error': 'User ID is required'}), 400
  
#   if uid in user_db.keys():
#     return jsonify(user_db[uid])
#   else:
#     return jsonify({'error': 'User not found'}), 404
  

import mysql.connector
from mysql.connector import Error


def test_mysql_connector():
    # Create a MySQLConnector instance
    db = MySQLConnector()


    db.add_user(user_data[0])
    print(user_data[0]['email'])
    print("User added successfully.")

    # Test fetching user by email
    user_login = db.get_user_login(user_data[0]['email'])
    print("User login details:", user_login)

    # Test fetching user by ID
    user_by_id = db.get_user_id(user_data[0]['userid'])
    print("User by ID details:", user_by_id)


    db.add_msg(message_data)
    print("Message added successfully.")

    # Test fetching the newest message
    newest_msg = db.get_msg_new(user_data[0]['userid'])
    print("Newest message:", newest_msg)

    # Test fetching all messages
    all_msgs = db.get_msg_all(user_data[0]['userid'])
    print("All messages:", all_msgs)

    # Test liking a message
    db.like_msg(message_data['msg_id'], user_data[0]['userid'])
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
