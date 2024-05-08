from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'group13'

# Dummy database to store user data
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'Username already exists'}), 400
    users[username] = {'password': password}
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username not in users or users[username]['password'] != password:
        return jsonify({'message': 'Invalid username or password'}), 401
    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
