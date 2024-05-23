from flask import Flask, request, jsonify

from sql import MySQLConnector

api = Flask(__name__)
db_connector = MySQLConnector()

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

@api.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'register_status': 'fail', 'error': 'Username, password, and email are required'}), 400

    if db_connector.get_user_by_email(email):
        return jsonify({'register_status': 'fail', 'error': 'Email already registered'}), 400

    db_connector.add_user({'username': username, 'password': password, 'email': email})
    return jsonify({'register_status': 'success'}), 201

@api.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    location = data.get('location')

    if not username or not password:
        return jsonify({'auth_status': 'fail', 'error': 'Username and password are required'}), 400

    user = db_connector.get_user_by_username(username)
    if user and user[0][2] == password:  # Password verification (hashing should be implemented in real applications)
        userid = user[0][0]
        db_connector.update_user_location(userid, location)
        user_data = db_connector.get_user(userid)
        msg_feed = db_connector.get_message_feed(userid)
        return jsonify({
            'auth_status': 'success',
            'data': {
                'userdata': {
                    'username': user_data[0][1],
                    'userid': user_data[0][0],
                    'email': user_data[0][3],
                    'location': user_data[0][4]
                },
                'msg_feed': msg_feed
            }
        })
    else:
        return jsonify({'auth_status': 'fail', 'error': 'Invalid username or password'}), 401

@api.route("/userdata", methods=['GET'])
def get_user_data():
    userid = request.args.get('userid')
    if not userid:
        return jsonify({'error': 'User ID is required'}), 400

    user = db_connector.get_user(userid)
    if user:
        return jsonify({
            'username': user[0][1],
            'password': user[0][2],  # Password should not be returned in real applications
            'email': user[0][3],
            'location': user[0][4]
        })
    else:
        return jsonify({'error': 'User not found'}), 404

@api.route("/feed", methods=['GET'])
def get_feed():
    userid = request.args.get('userid')
    if not userid:
        return jsonify({'error': 'User ID is required'}), 400

    msg_feed = db_connector.get_message_feed(userid)
    return jsonify(msg_feed)

@api.route("/location", methods=['POST'])
def update_location():
    data = request.get_json()
    userid = data.get('userid')
    location = data.get('location')

    if not userid or not location:
        return jsonify({'error': 'User ID and location are required'}), 400

    db_connector.update_user_location(userid, location)
    msg_feed = db_connector.get_message_feed(userid)
    return jsonify(msg_feed)

@api.route("/message", methods=['PUT'])
def post_message():
    data = request.get_json()
    userid = data.get('userid')
    new_msg = data.get('new_msg')

    if not userid or not new_msg:
        return jsonify({'error': 'User ID and message are required'}), 400

    db_connector.add_message(userid, new_msg)
    return jsonify({'status': 'success'})

@api.route("/like", methods=['PUT'])
def like_message():
    data = request.get_json()
    userid = data.get('userid')
    msg_id = data.get('msg_id')

    if not userid or not msg_id:
        return jsonify({'error': 'User ID and message ID are required'}), 400

    db_connector.like_message(userid, msg_id)
    return jsonify({'status': 'success'})

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000)
