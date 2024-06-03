# LocaSync
極短距離的即時通訊社群軟體

The website v1.0.0 is now deployed on http://ws1.csie.org:5173 !!

## System Design
There are 3 docker containers in this design, `db`, `backend` and `frontend`.

1. `db`

Run the MySQL server exposed at `db:3306` within the docker internal network.

2. `backend`

Run the Flask API server exposed at `backend:5000` within the docker internal network.
The API server provides APIs for the Vue app to register, login, get message feed, like message and update location by interacting with the MySQL server.
See API spec below.

3. `frontend`

Run the Vue app LocaSync on http://localhost:5173.

## Quick Start Up
1. Install Docker
2. Run `./build.sh`
2. Run `./run.sh`

## Notes for Developers
**大家看這裡！！**

### Use Branch!

Open a new branch and develop features (or add new files if needed) in the corresponding folder. When you're finished, open a pull request and fix merge conflict first before merging the branch into the main branch.


```bash
# Create a new branch
git checkout -b "your-new-branch-name"

# If you finished and want to merge the branch to the main,
# 1. Merge the main into your branch first and resolve conflicts.
git checkout "your-branch-name"
git merge main

# 2. Open a pull request on Github (https://github.com/Letuvertia/cnl-final/pulls)

# 3. Ask other teammates to review your branch before you merge.

# 4. If everything is good, merge the branch on the Github by pressing the merge button. This will close the pull request at the same time.
```

### (Optinal) Develop on Local
If you're developing a feature that is only on `backend` or `frontend` side, it is maybe easier to use local environment instead of the docker environment, which connects everything and is more likely to have bugs.

Here's how to install the dependencie on the local environment:

1. `backend`

Install Python and execute files in `./backend`.

```bash
python3 backend/main.py
```

Use `curl` to test APIs. See `backend/test_api.sh` for more examples.

```bash
# POST
curl -X POST -H "Content-Type: application/json" -d '{"username":"newuser1","password":"password123","email":"test@email.com"}' "http://localhost:5000/register"

# GET
curl -X GET "http://localhost:5000/feed?userid=1"

# PUT
curl -X PUT -H "Content-Type: application/json" -d '{"userid":1,"new_msg":{"msg_userid": 1,"msg_content": "Hello!","msg_location_latitude": "125.34","msg_location_longitude": "25.4"}}' "http://localhost:5000/message"
```

2. `frontend`

Install Node.js and run the server. Make sure that you're located at `./frontend` before running `npm` commands.

```bash
# Install Node.js and npm with nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install lts/hydrogen # v18.20.2

# Go to the root folder for the Vue app
cd frontend

# Install dependencies (re-run if add new dependency in package.json)
npm run install

# Build the Vue app (re-run if vite.config.js is changed)
npm run build

# Start the Vue app
npm run dev
```

Go to http://localhost:5173 to check out the website.

## SQL Data Format
### `user` table
```sql
userid serial PRIMARY KEY,
username varchar(255),
password varchar(255),
email varchar(255) ,
location_latitude FLOAT,
location_longitude FLOAT
```

### `message` table
```sql
msg_id serial PRIMARY KEY,
msg_userid integer,
msg_likes integer,
msg_content varchar(255),
msg_location_latitude FLOAT,
msg_location_longitude FLOAT
```

### `likes` table
```sql
userid integer,
msg_id integer
```

## API spec
### `/register` (POST)
Register a new user account.

Arg:
```json
{
    "username": "",
    "password": "",
    "email": ""
}
```
Return:
```json
{
    "register_status": "__success or fail__"
}
```

### `/login` (POST)
Login with user crendentials.

Arg:
```json
{
    "username": "",
    "password": ""
}
```
Return:
```json
{
    "auth_status": "__success or fail__",
    "userdata": {
        "userid": "",
        "username": "",
        "email": ""
    }
}
```

### `/location` (POST)
Update both location and message feed.

Update every 15s.

`msg_liked`: `true` if the user has already liked the message, else `false`.

Arg:
```json
{
    "userid": "",
    "location_latitude": "",
    "location_longitude":""
}
```
Return:
```json
[
    {
        "msg_id": "",
        "msg_userid": "",
        "msg_likes": "",
        "msg_content": "",
        "msg_location_latitude": "",
        "msg_location_longitude": "",
        "msg_liked": true
    },
    {
        "msg_id": "",
        "msg_userid": "",
        "msg_likes": "",
        "msg_content": "",
        "msg_location_latitude": "",
        "msg_location_longitude": "",
        "msg_liked": false
    },
    ...
]
```

### `/feed` (GET)
Update only message feed.

Update every 3s.

Arg:
- `userid`

Return:
```json
[
    {
        "msg_id": "",
        "msg_userid": "",
        "msg_likes": "",
        "msg_content": "",
        "msg_location_latitude": "",
        "msg_location_longitude": "",
        "msg_liked": true
    },
    {
        "msg_id": "",
        "msg_userid": "",
        "msg_likes": "",
        "msg_content": "",
        "msg_location_latitude": "",
        "msg_location_longitude": "",
        "msg_liked": false
    },
    ...
]
```

### `/message` (PUT)
Send a new message that user enters to the backend.
Update the message directly on the main view.

Arg:
```json
{
    "userid": "",
    "new_msg": {
        "msg_userid": "",
        "msg_content": "",
        "msg_location_latitude": "",
        "msg_location_longitude": ""
    }
}
```

### `/like` (PUT)
Send an like of a message from the user to the backend.
Update the number of likes directly on the main view.

Arg:
```json
{
    "userid": "",
    "msg_id": ""
}
```

### `/userdata` (GET)
Get user data and message history.

Arg:
- `userid`

Return:
```json
{
    "userid": "",
    "username": "",
    "email": "",
    "location_latitude": "",
    "location_longitude":"",
    "msg_history": [
        {
            "msg_id": "",
            "msg_userid": "",
            "msg_likes": "",
            "msg_content": "",
            "msg_location_latitude": "",
            "msg_location_longitude": "",
            "msg_liked": true
        },
        {
            "msg_id": "",
            "msg_userid": "",
            "msg_likes": "",
            "msg_content": "",
            "msg_location_latitude": "",
            "msg_location_longitude": "",
            "msg_liked": false
        },
        ...
    ]
}
```