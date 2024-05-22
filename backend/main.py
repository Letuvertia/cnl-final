from flask import Flask, request, jsonify

from sql import MySQLConnector

api = Flask(__name__)

# Sample user data (only for testing)
user_db = [
  {
    "username": "John Doe",
    "email": "john.doe@example.com",
  },
  {
    "username": "Ann Doe",
    "email": "ann.doe@example.com",
  }
]

@api.route("/userdata")
def get_user_data():
  """Returns user data in JSON format"""
  uid = int(request.args.get('uid'))
  if uid in user_db.keys():
    return jsonify(user_db[uid])
  else:
    return "User Not Found"


if __name__ == "__main__":
    # test sql
    connector = MySQLConnector()
    connector.add_user(user_db[0])
    user = connector.get_user(1)
    print(user)

    # start api server
    # api.run(host="0.0.0.0", port=5000)
