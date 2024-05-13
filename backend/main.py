from flask import Flask, request, jsonify

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

if __name__ == "__main__":
  api.run(host="0.0.0.0", port=5000)
