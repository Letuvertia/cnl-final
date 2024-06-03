import time
import mysql.connector


class MySQLConnector:
    def __init__(self, host="db", database="locasync", user="admin", password="admin") -> None:
        self.connected = False
        self.connection = None
        self.cursor = None

        self.database = database
        
        # initialize database
        self._connect(host, database, user, password)
        self._create_user_table()
        self._create_message_table()
        self._create_likes_table()

    def __exit__(self):
        if self.connection:
            self.connection.close()

    def _connect(self, host, database, user, password) -> None:
        while not self.connected:
            print("Try to connect ...")
            try:
                # Connect to the MySQL server
                self.connection = mysql.connector.connect(
                    host=host, database=database, user=user, password=password
                )

                # Create a cursor object
                self.cursor = self.connection.cursor(buffered=True)
                self.connected = True
                print(f"Success: Connect to the server@{host}:3306")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                time.sleep(2)

    def _execute_query(self, sql_query, success_log="", param=None) -> None:
        try:
            self.cursor.execute(sql_query, param)
            self.connection.commit()

            if success_log:
                print(f"Success: {success_log}")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def _create_user_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS user (
                userid serial PRIMARY KEY,
                username varchar(255),
                password varchar(255),
                email varchar(255) ,
                location_latitude FLOAT,
                location_longitude FLOAT
            );
            """
        self._execute_query(query, "Create table 'user'")

    def _create_message_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS message (
                msg_id serial PRIMARY KEY,
                msg_userid integer,
                msg_likes integer,
                msg_content varchar(255),
                msg_location_latitude FLOAT,
                msg_location_longitude FLOAT
            );
            """
        self._execute_query(query, "Create table 'message'")
    
    def _create_likes_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS likes (
                userid integer,
                msg_id integer
            );
            """
        self._execute_query(query, "Create table 'likes'")
    
    def _truncate_table(self, table) -> None:
        query = f"TRUNCATE TABLE {table};"
        self._execute_query(query, f"Empty table '{table}'")

    def _print_table_schema(self, table):
        query = f"SHOW COLUMNS FROM {table};"
        self.cursor.execute(query)
        for column in self.cursor.fetchall():
            print(column)

    def clear_database(self) -> None:
        """
        Empty all tables.
        """
        self._truncate_table("user")
        self._truncate_table("message")
        self._truncate_table("likes")
    
    @staticmethod
    def _to_user_dict(user:tuple) -> dict:
        return {
            "userid": user[0],
            "username": user[1],
            "password": user[2],
            "email": user[3],
            "location_latitude": user[4],
            "location_longitude": user[5]
        }

    def _to_msg_dict(self, msg:tuple, userid:int) -> dict:
        msg_liked = self.is_liked_by_user(msg_id=msg[0], userid=userid)
        return {
            "msg_id": msg[0],
            "msg_userid": msg[1],
            "msg_likes": msg[2],
            "msg_content": msg[3],
            "msg_location_latitude": msg[4],
            "msg_location_longitude": msg[5],
            "msg_liked": msg_liked
        }

    def add_user(self, username, password, email,
                 location_latitude=0.0, location_longitude=0.0) -> None:
        """
        Add a new user.
        """
        query = f"""
            INSERT INTO user (username, password, email, location_latitude, location_longitude)
            VALUES (
                '{username}',
                '{password}',
                '{email}',
                '{location_latitude}',
                '{location_longitude}'
            );
        """
        self._execute_query(query, f"Insert user {username}")
    
    def get_user_by_name(self, username) -> dict:
        """
        Get user by `username`.
        """
        query = f"SELECT * FROM user WHERE username = '{username}';"
        self._execute_query(query, f"Get user {username}")
        user = self.cursor.fetchall()
        return self._to_user_dict(user[0]) if user else {}

    def get_user_by_id(self, userid) -> dict:
        """
        Get user by `userid`.
        """
        query = f"SELECT * FROM user WHERE userid = {userid};"
        self._execute_query(query, f"Get user {userid}")
        user = self.cursor.fetchall()
        return self._to_user_dict(user[0]) if user else {}
    
    def is_username_exist(self, username) -> bool:
        """
        Check if the user exists by `username`.
        """
        return True if self.get_user_by_name(username) else False

    def is_userid_exist(self, userid) -> bool:
        """
        Check if the user exists by `userid`.
        """
        return True if self.get_user_by_id(userid) else False

    def add_msg(self, msg_userid, msg_content,
                msg_location_latitude, msg_location_longitude) -> None:
        """
        Add a new message.
        """
        query = f"""
            INSERT INTO message (msg_userid, msg_likes, msg_content, msg_location_latitude, msg_location_longitude)
            VALUES (
                '{msg_userid}',
                '0',
                '{msg_content}',
                '{msg_location_latitude}',
                '{msg_location_longitude}'
            );
        """
        self._execute_query(query, f"Insert message \"{msg_content}\" by user {msg_userid}")
    
    def get_user_all_msg(self, userid) -> list:
        """
        Get user's message history by `userid`.

        Return: a list of msg dict
        """
        query = f"SELECT * FROM message WHERE msg_userid = {userid}"
        self._execute_query(query, f"Get all messages by user {userid}")
        msgs = self.cursor.fetchall()
        return [self._to_msg_dict(msg, userid) for msg in msgs] if msgs else []
    
    def _get_msg_feed_by_location(self, latitude, longitude, distance_km) -> list:
        """
        Get all messages around the location (`latitude`, `longitude`) within `distance_km`.

        Return: a list of msg tuple
        """
        query = f"""
            SELECT *, 
            (6371 * acos(cos(radians({latitude})) * cos(radians(msg_location_latitude)) * cos(radians(msg_location_longitude) 
            - radians({longitude})) + sin(radians({latitude})) * sin(radians(msg_location_latitude)))) 
            AS distance
            FROM message
            HAVING distance < {distance_km}
            ORDER BY distance;
        """
        self._execute_query(query, f"Get message feed based on location ({latitude}, {longitude})")
        return self.cursor.fetchall()
    
    def get_msg_feed(self, userid, distance_km=1) -> list:
        """
        Get all messages around the user.

        Return: a list of msg dict
        """
        user = self.get_user_by_id(userid)
        msgs = self._get_msg_feed_by_location(latitude=user['location_latitude'],
                                              longitude=user['location_longitude'],
                                              distance_km=distance_km)
        return [self._to_msg_dict(msg, userid) for msg in msgs] if msgs else []
    
    def update_location(self, userid, latitude, longitude) -> None:
        """
        Update user's location.
        """
        query = f"UPDATE user SET location_latitude = {latitude}, location_longitude = {longitude} WHERE userid = {userid};"
        self._execute_query(query, f"Update user {userid}'s location ({latitude, longitude})")
    
    def update_likes(self, userid, msg_id) -> None:
        """
        Like the message `msg_id` by the user `userid`.
        """
        if self.is_liked_by_user(userid, msg_id):
            return
        query = f"INSERT INTO likes (userid, msg_id) VALUES ('{userid}', '{msg_id}');"
        self._execute_query(query, f"Insert record: user {userid} liked message {msg_id}")

        query = f"UPDATE message SET msg_likes = msg_likes + 1 WHERE msg_id = {msg_id};"
        self._execute_query(query, f"Add 1 like to message {msg_id}")
    
    def is_liked_by_user(self, userid, msg_id) -> bool:
        """
        Check if the message `msg_id` is liked by the user `userid`.
        """
        query = f"SELECT * FROM likes WHERE userid = {userid} AND msg_id = {msg_id};"
        self._execute_query(query, f"Check if the message {msg_id} is liked by the user {userid}")
        return True if self.cursor.fetchall() else False


class Test:

    def __init__(self):
        self.db = MySQLConnector()
        self.db.clear_database()

        print("=====Table 'user'=====")
        self.db._print_table_schema("user")
        print("=====Table 'message'=====")
        self.db._print_table_schema("message")
        print("=====Table 'likes'=====")
        self.db._print_table_schema("likes")

    def run_unit_test(self):
        # test sample data
        test_user = {
            "username": "JohnDoe",
            "password": "123456",
            "email": "johndoe@example.com",
            "location_latitude": 121.123,
            "location_longitude": 25.123,
        }

        test_msg = {
            "msg_userid": 1,
            "msg_content": "Hello, world!",
            "msg_location_latitude": 121.123,
            "msg_location_longitude": 25.123,
        }

        # unit test
        ## user
        self.db.add_user(username=test_user['username'],
                         password=test_user['password'],
                         email=test_user['email'])
        print("User: ", self.db.get_user_by_name(username=test_user['username']))
        print("User: ", self.db.get_user_by_id(userid=1))

        ## msg
        self.db.add_msg(msg_userid=test_msg['msg_userid'],
                        msg_content=test_msg['msg_content'],
                        msg_location_latitude=test_msg['msg_location_latitude'],
                        msg_location_longitude=test_msg['msg_location_longitude'])
        print("User 1's message: ", self.db.get_user_all_msg(userid=1))

        # location
        self.db.update_location(userid=1,
                                latitude=test_msg['msg_location_latitude'],
                                longitude=test_msg['msg_location_longitude'])
        print("Message feed: ", self.db.get_msg_feed(userid=1))

        # likes
        self.db.update_likes(userid=1, msg_id=1)
        print("Message 1 liked by user 1: ", self.db.is_liked_by_user(userid=1, msg_id=1))
        print("User 1's message: ", self.db.get_user_all_msg(userid=1))


if __name__ == "__main__":
    tester = Test()
    tester.run_unit_test()