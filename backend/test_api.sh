#!/bin/bash

# Set the base URL for the APIs
BASE_URL="http://localhost:5000"

# Register
echo "Testing POST @api.route('/register', methods=['POST'])"
curl -X POST -H "Content-Type: application/json" -d '{"username":"newuser1","password":"password123","email":"test@email.com"}' "$BASE_URL/register"
echo -e "\n"

# Login
echo "Testing POST @api.route('/login', methods=['POST'])"
curl -X POST -H "Content-Type: application/json" -d '{"username":"newuser1","password":"password123"}' "$BASE_URL/login"
echo -e "\n"

# Post a new message
echo "Testing PUT @api.route('/message', methods=['PUT'])"
curl -X PUT -H "Content-Type: application/json" -d '{"userid":1,"new_msg":{"msg_userid": 1,"msg_content": "Hello!","msg_location_latitude": "125.34","msg_location_longitude": "25.4"}}' "$BASE_URL/message"
echo -e "\n"

# Update location and get message feed
echo "Testing POST @api.route('/location', methods=['POST'])"
curl -X POST -H "Content-Type: application/json" -d '{"userid":1,"location_latitude":"125.34","location_longitude":"25.4"}' "$BASE_URL/location"
echo -e "\n"

# Like a message
echo "Testing PUT @api.route('/like', methods=['PUT'])"
curl -X PUT -H "Content-Type: application/json" -d '{"userid":"1","msg_id":"1"}' "$BASE_URL/like"
echo -e "\n"

# Get message feed
echo "Testing GET @api.route('/feed', methods=['GET'])"
curl -X GET "$BASE_URL/feed?userid=1"
echo -e "\n"

# Get user data and message history 
echo "Testing GET @api.route('/userdata', methods=['GET'])"
curl -X GET "$BASE_URL/userdata?userid=1"
echo -e "\n"

echo "All tests completed!"