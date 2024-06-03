from flask import Flask, request, jsonify

from sql import MySQLConnector

# api server
api = Flask(__name__)
db_connector = MySQLConnector()
db_connector.clear_database() # run this line to empty the database

@api.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username:
        return jsonify({'register_status': 'fail', 'error': 'username is missing.'}), 200
    if not password:
        return jsonify({'register_status': 'fail', 'error': 'password is missing'}), 200
    if not email:
        return jsonify({'register_status': 'fail', 'error': 'email is missing'}), 200
    if db_connector.is_username_exist(username=username):
        return jsonify({'register_status': 'fail', 'error': f'user \'{username}\' already registered'}), 200

    db_connector.add_user(username=username,
                          password=password,
                          email=email)
    return jsonify({'register_status': 'success'}), 200


@api.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username:
        return jsonify({'auth_status': 'fail', 'error': 'username is missing.'}), 200
    if not password:
        return jsonify({'auth_status': 'fail', 'error': 'password is missing'}), 200

    user = db_connector.get_user_by_name(username=username)
    if not user:
        return jsonify({'auth_status': 'fail', 'error': f'user {username} does not exists'}), 200
    if user['password'] != password:
        return jsonify({'auth_status': 'fail', 'error': 'incorrect password'}), 200

    return jsonify({
        "auth_status": "success",
        "userdata": {
            "userid": user['userid'],
            "username": user['username'],
            "email": user['email']
        }
    }), 200


@api.route("/location", methods=['POST'])
def update_location():
    data = request.get_json()
    userid = data.get('userid')
    latitude = data.get('location_latitude')
    longitude = data.get('location_longitude')

    if not userid:
        return "userid is missing", 400
    userid = int(userid)
    if not db_connector.is_userid_exist(userid):
        return f"user {userid} does not exists", 400
    
    if not latitude or not longitude:
        return "latitude or longitude is missing", 400
    
    db_connector.update_location(userid=userid, latitude=latitude, longitude=longitude)
    msgs = db_connector.get_msg_feed(userid=userid)
    return jsonify(msgs), 200


@api.route("/feed", methods=['GET'])
def get_feed():
    userid = request.args.get('userid')
    if not userid:
        return "userid is missing", 400
    userid = int(userid)
    if not db_connector.is_userid_exist(userid):
        return f"user {userid} does not exists", 400

    msgs = db_connector.get_msg_feed(userid=userid)
    return jsonify(msgs), 200


@api.route("/message", methods=['PUT'])
def add_message():
    data = request.get_json()
    userid = data.get('userid')
    new_msg = data.get('new_msg')

    if not userid:
        return "userid is missing", 400
    userid = int(userid)
    if not db_connector.is_userid_exist(userid):
        return f"user {userid} does not exists", 400
    
    if not new_msg:
        return "new_msg is missing", 400
    
    db_connector.add_msg(msg_userid=new_msg.get('msg_userid'),
                         msg_content=new_msg.get('msg_content'),
                         msg_location_latitude=new_msg.get('msg_location_latitude'),
                         msg_location_longitude=new_msg.get('msg_location_longitude'))
    return "", 200


@api.route("/like", methods=['PUT'])
def add_like():
    data = request.get_json()
    userid = data.get('userid')
    msg_id = data.get('msg_id')

    if not userid:
        return "userid is missing", 400
    userid = int(userid)
    if not db_connector.is_userid_exist(userid):
        return f"user {userid} does not exists", 400
    
    if not msg_id:
        return "msg_id is missing", 400

    db_connector.update_likes(userid=userid, msg_id=msg_id)
    return "", 200


@api.route("/userdata", methods=['GET'])
def get_userdata():
    userid = request.args.get('userid')
    if not userid:
        return "userid is missing", 400
    userid = int(userid)
    if not db_connector.is_userid_exist(userid):
        return f"user {userid} does not exists", 400
    
    data = db_connector.get_user_by_id(userid=userid)
    del data['password']
    data['msg_history'] = db_connector.get_user_all_msg(userid=userid)

    return jsonify(data), 200


if __name__ == "__main__":
    # start api server
    api.run(host="0.0.0.0", port=5000, debug=True)
