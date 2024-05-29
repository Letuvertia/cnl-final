#!/bin/bash

# Set the base URL for the APIs
BASE_URL="http://localhost:5000"

# Test API 1: Register a new user (POST /register)
echo "Testing POST @api.route('/register', methods=['POST'])"
curl -s -X POST -H "Content-Type: application/json" -d '{"username":"newuser","password":"password123"}' "$BASE_URL/register"
echo -e "\n"

# Test API 2: Authenticate a user (POST /login)
echo "Testing POST @api.route('/login', methods=['POST'])"
curl -s -X POST -H "Content-Type: application/json" -d '{"username":"john","password":"password123"}' "$BASE_URL/login"
echo -e "\n"

# Test API 3: Get list of users (GET /users)
echo "Testing GET @api.route('/users', methods=['GET'])"
curl -s -X GET "$BASE_URL/users"
echo -e "\n"

# Test API 4: Get feed for a user (GET /feed)
echo "Testing GET @api.route('/feed', methods=['GET'])"
curl -s -X GET "$BASE_URL/feed?userid=1"
echo -e "\n"

# Test API 5: Update location (POST /location)
echo "Testing POST @api.route('/location', methods=['POST'])"
curl -s -X POST -H "Content-Type: application/json" -d '{"userid":"1","location":"New York"}' "$BASE_URL/location"
echo -e "\n"

# Test API 6: Post a new message (PUT /message)
echo "Testing PUT @api.route('/message', methods=['PUT'])"
curl -s -X PUT -H "Content-Type: application/json" -d '{"userid":"1","new_msg":"Hello, world!"}' "$BASE_URL/message"
echo -e "\n"

# Test API 7: Like a message (PUT /like)
echo "Testing PUT @api.route('/like', methods=['PUT'])"
curl -s -X PUT -H "Content-Type: application/json" -d '{"userid":"1","msg_id":"101"}' "$BASE_URL/like"
echo -e "\n"

echo "All tests completed!"