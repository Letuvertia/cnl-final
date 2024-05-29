from flask import Flask, request, jsonify

from sql import MySQLConnector

api = Flask(__name__)

from ex_db_data import user_data, message_data

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

<<<<<<< Updated upstream
=======
#   if not uid:
#     return jsonify({'error': 'User ID is required'}), 400
  
#   if uid in user_db.keys():
#     return jsonify(user_db[uid])
#   else:
#     return jsonify({'error': 'User not found'}), 404

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

>>>>>>> Stashed changes
@api.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
<<<<<<< Updated upstream
=======

    if not username or not password or not email:
        return jsonify({'register_status': 'fail', 'error': 'Username, password, and email are required'}), 400

    if db_connector.get_user_login(email):
        return jsonify({'register_status': 'fail', 'error': 'Email already registered'}), 400

    db_connector.add_user({'username': username, 'password': password, 'email': email, 'location_longitude': '-', 'location_latitude': '-'})
    return jsonify({'register_status': 'success'}), 201

@api.route("/login", methods=['POST'])
def login(): #notdone (-changeloc)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'auth_status': 'fail', 'error': 'Username and password are required'}), 400

    user = db_connector.get_user_login(username)
    
    if user and user[0][2] == password:  # Password verification (hashing should be implemented in real applications)
        uid = user[0][0]
        location = db_connector.get_new_location(uid)
        db_connector.update_user_location(uid, location[0], location[1])
        user_ = db_connector.get_user_id(uid)
        msg_feed = db_connector.get_msg_all(uid)
        return jsonify({
            'auth_status': 'success',
            'data': {
                'userdata': {
                    'username': user_[0][1],
                    'userid': user_[0][0],
                    'email': user_[0][3],
                    'location_longitude': user_[0][4],
                    'location_latitude': user_[0][5]
                },
                'msg_feed': msg_feed
            }
        })
    else:
        return jsonify({'auth_status': 'fail', 'error': 'Invalid username or password'}), 401

@api.route("/userdata", methods=['GET'])
def get_user_data():
    uid = request.args.get('userid')
    if not uid:
        return jsonify({'error': 'User ID is required'}), 400

    user = db_connector.get_user_id(uid)
    if user:
        return jsonify({
            'username': user[0][1],
            'password': user[0][2],  # Password should not be returned in real applications
            'email': user[0][3],
            'location_longitude': user[0][4],
            'location_latitude': user[0][5]
        })
    else:
        return jsonify({'error': 'User not found'}), 404

@api.route("/feed", methods=['GET'])
def get_feed():
    uid = request.args.get('userid')
    if not uid:
        return jsonify({'error': 'User ID is required'}), 400

    msg_feed = db_connector.get_msg_all(uid)
    return jsonify(msg_feed)

@api.route("/location", methods=['POST'])
def update_location(): #notdone(-changeloc)
    data = request.get_json()
    uid = data.get('userid')

    if not uid:
        return jsonify({'error': 'User ID and location are required'}), 400
    location = db_connector.get_new_location(uid)
    db_connector.update_user_location(uid, location[0], location[1])
    msg_feed = db_connector.get_message_all(uid)
    return jsonify(msg_feed)

@api.route("/message", methods=['PUT'])
def post_message():
    data = request.get_json()
    uid = data.get('userid')
    new_msg = data.get('new_msg')

    if not uid or not new_msg:
        return jsonify({'error': 'User ID and message are required'}), 400

    db_connector.add_msg(new_msg)
    return jsonify({'status': 'success'})

@api.route("/like", methods=['PUT'])
def like_message():
    data = request.get_json()
    uid = data.get('userid')
    msg_id = data.get('msg_id')

    if not uid or not msg_id:
        return jsonify({'error': 'User ID and message ID are required'}), 400

    db_connector.like_msg(msg_id, uid)
    return jsonify({'status': 'success'})  
>>>>>>> Stashed changes

    if not username or not password or not email:
        return jsonify({'register_status': 'fail', 'error': 'Username, password, and email are required'}), 400

    if db_connector.get_user_login(email):
        return jsonify({'register_status': 'fail', 'error': 'Email already registered'}), 400

    db_connector.add_user({'username': username, 'password': password, 'email': email})
    return jsonify({'register_status': 'success'}), 201

@api.route("/login", methods=['POST'])
def login(): #notdone (-changeloc)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    location = data.get('location')

    if not username or not password:
        return jsonify({'auth_status': 'fail', 'error': 'Username and password are required'}), 400

    user = db_connector.get_user_login(username)
    if user and user[0][2] == password:  # Password verification (hashing should be implemented in real applications)
        uid = user[0][0]
        #db_connector.update_user_location(uid, location)
        user_data = db_connector.get_user_id(uid)
        msg_feed = db_connector.get_msg_all(uid)
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

@api.route("/userdata", methods=['POST'])
def get_user_data():
    uid = request.args.get('userid')
    if not uid:
        return jsonify({'error': 'User ID is required'}), 400

    user = db_connector.get_user_id(uid)
    if user:
        return jsonify({
            'username': user[0][1],
            'password': user[0][2],  # Password should not be returned in real applications
            'email': user[0][3],
            'location': user[0][4]
        })
    else:
        return jsonify({'error': 'User not found'}), 404

@api.route("/feed", methods=['POST'])
def get_feed():
    uid = request.args.get('userid')
    if not uid:
        return jsonify({'error': 'User ID is required'}), 400

    msg_feed = db_connector.get_msg_all(uid)
    return jsonify(msg_feed)

@api.route("/location", methods=['POST'])
def update_location(): #notdone(-changeloc)
    data = request.get_json()
    uid = data.get('userid')
    location = data.get('location')

    if not uid or not location:
        return jsonify({'error': 'User ID and location are required'}), 400

    db_connector.update_user_location(uid, location)
    msg_feed = db_connector.get_message_all(uid)
    return jsonify(msg_feed)

@api.route("/message", methods=['PUT'])
def post_message():
    data = request.get_json()
    uid = data.get('userid')
    new_msg = data.get('new_msg')

    if not uid or not new_msg:
        return jsonify({'error': 'User ID and message are required'}), 400

    db_connector.add_msg(new_msg)
    return jsonify({'status': 'success'})

@api.route("/like", methods=['PUT'])
def like_message():
    data = request.get_json()
    uid = data.get('userid')
    msg_id = data.get('msg_id')

    if not uid or not msg_id:
        return jsonify({'error': 'User ID and message ID are required'}), 400

    db_connector.like_msg(msg_id, uid)
    return jsonify({'status': 'success'})

def test_mysql_connector():
    # Create a MySQLConnector instance
    


    db_connector.add_user(user_data[0])
    print(user_data[0]['email'])
    print("User added successfully.")

<<<<<<< Updated upstream
=======
    db_connector.check_user_exit(user_data[0]['email'])
    s = db_connector.check_user_exit("iansu1220@gmail.com")
    print(s)

>>>>>>> Stashed changes
    # Test fetching user by email
    user_login = db_connector.get_user_login(user_data[0]['email'])
    print("User login details:", user_login)

    # Test fetching user by ID
    user_by_id = db_connector.get_user_id(user_data[0]['userid'])
    print("User by ID details:", user_by_id)

<<<<<<< Updated upstream

    db.add_msg(message_data)
=======
    db_connector.print_table_schema("message")
    db_connector.add_msg(message_data)
>>>>>>> Stashed changes
    print("Message added successfully.")

    # Test fetching the newest message
    newest_msg = db_connector.get_msg_new(user_data[0]['userid'])
    print("Newest message:", newest_msg)

    # Test fetching all messages
    all_msgs = db_connector.get_msg_all(user_data[0]['userid'])
    print("All messages:", all_msgs)

    # Test liking a message
    db_connector.like_msg(message_data['msg_id'], user_data[0]['userid'])
    print("Message liked successfully.")

<<<<<<< Updated upstream
=======
    db_connector.update_data_location(1,128.245,189.123)
    print(db_connector.get_new_location(1))

    db_connector.show_msg(user_data[0]['location_longitude'],user_data[0]['location_latitude'],1)

>>>>>>> Stashed changes

if __name__ == "__main__":
    test_mysql_connector()

# if __name__ == "__main__":
#     # Test SQL
#     connector = MySQLConnector()
#     for user in user_db:
#         connector.add_user(user)
#     user = connector.get_user(1)
#     print(user)

<<<<<<< Updated upstream
#     # Start API server
#     api.run(host="0.0.0.0", port=5000)
=======
    # start api server
    api.run(host="0.0.0.0", port=5000)
>>>>>>> Stashed changes
