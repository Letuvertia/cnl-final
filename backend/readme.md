### data format
#### userdata
```
"userdata": {
            "username": "",
            "password":"",
            "email": "",
            "latitude": "",
            "longitude":""
        },
```
#### messagedata
```
"messagedata": {
            "userid": "",
            "msgid":"",
            "msg_content": "",
            "msg_likes":"",
            "msg_location_latitude": "",
            "msg_location_longitude": ""
        },
```
### api in sql.py
- init(),exit(),connect(),execute_sql():just as their name,if neccessary,check the code directly
- check_user_exit(username): check the db if the username already exist. If so ,return -1;else ,return the userid

- add_user(userdata):add the userdata(need to in format) to the db
- get_all_user():list all the user information in userdata-format
- get_user_login(username):get the user information by username in userdata-format
- get_user_id(userid):get the user information by userid in userdata-format

- add_msg(message_data):add the messagedata(need to in format) to db 
- get_msg_new(userid):show the newest message of the userid
- get_msg_all(userid):show all the message which userid post
- show_msg(latitude,longititude,distance_km):the user location is ('latitude','longititude') ,show all the message that is in the 'distance_km' to the user
- like_msg(msgid,userid):update the msg like count

- update_data_location(userid, latitude, longitude):update the database location information(write into the db)
- get_new_location(userid):get the location information from db(read from the db)

### spi in main.py
- /register(username,password,email):(the location is all set to 0, will be discussed)
    return success or not
- /login(username,password,latitude,longitude):
    return userdata if the password match
- /userdata(userid):
    return the userdata by userid
- /users():
    return all userdata
- /feed(userid):
    return the message history(data get by get_msg_all())
- /location(userid,latitude,longitude):
    return success or not(about write the location information to the db)
- /message(userid,msgcontent):(here has the bug that the msgid is set to be a constant ,would be fix to be increased automatically)
    return success or not
- /likes(userid,msgid):(update the like count,but would only add 1)
    return success or not