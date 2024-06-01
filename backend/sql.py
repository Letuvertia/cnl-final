import time
import mysql.connector


class MySQLConnector:
    def __init__(self, host="db", database="locasync", user="admin", password="admin") -> None:
        self.connected = False
        self.connection = None
        self.cursor = None

        self.database = database
        
        # init
        self._connect(host, database, user, password)
        self.drop_user_table()
        self.drop_message_table()

        self.create_user_table()
        self.create_message_table()

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

    def _execute_query(self, sql_query, success_log="", param = None) -> None:
        try:
            self.cursor.execute(sql_query,param)

            self.connection.commit()

            if success_log:
                print(f"Success: {success_log}")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def drop_message_table(self) -> None:
        query = "DROP TABLE IF EXISTS message"
        self._execute_query(query, "Drop table 'message'")

    def drop_user_table(self) -> None:
        query = "DROP TABLE IF EXISTS user"
        self._execute_query(query, "Drop table 'user'")

    def create_user_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS user (
                userid serial PRIMARY KEY,
                username varchar(255),
                password varchar(255),
                email nvarchar(255) ,
                location_longitude FLOAT,
                location_latitude FLOAT
            );
            """
        self._execute_query(query, "Create table 'user'")

    def create_message_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS message (
                userid integer,
                msg_id integer,
                msg_content varchar(255),
                msg_likes integer,
                msg_location_longitude FLOAT,
                msg_location_latitude FLOAT
            );
            """
        self._execute_query(query, "Create table 'message'")

    def check_user_exit(self, username):
        query = f"SELECT * FROM user WHERE username = '{username}';"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return result[0]
        else:
            return -1

    def add_user(self, user_data) -> None:
        query = f"""
            INSERT INTO user (username, password, email, location_longitude,location_latitude)
            VALUES (
            '{user_data['username']}',
            '{user_data['password']}',
            '{user_data['email']}',
            '{user_data['location_longitude']}',
            '{user_data['location_latitude']}');
        """
        self._execute_query(query, f"Insert {user_data}")
        
    def get_all_user(self):
        query = "SELECT * FROM user;"
        self._execute_query(query,"get all user")
        return self.cursor.fetchall()
    
    def get_user_login(self, username):
        query = f"SELECT * FROM user WHERE username = '{username}';"
        self._execute_query(query,"get user by username")
        return self.cursor.fetchall()
    
    def get_user_id(self,userid):
        query = f"SELECT * FROM user WHERE userid = '{userid}';"
        self._execute_query(query,"get user by id")
        return self.cursor.fetchall()
    
    #def login 
    #def register

    #for testing
    def print_table_schema(self, table_name):
        query = f"SHOW COLUMNS FROM {table_name}"
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        print(f"Schema for table '{table_name}':")
        for column in columns:
            print(column)
    
    def add_msg(self,message_data):
        query = f"""
            INSERT INTO message (userid, msg_id, msg_content, msg_likes, msg_location_longitude, msg_location_latitude)
            VALUES ('{message_data['userid']}',
                  '{message_data['msg_id']}',
                  '{message_data['msg_content']}',
                  '{message_data['msg_likes']}',
                  '{message_data['msg_location_longitude']}',
                  '{message_data['msg_location_latitude']}');
        """
        # params = (message_data["userid"],
        #           message_data["msg_id"],
        #           message_data["msg_content"],
        #           message_data["msg_likes"],
        #           message_data["msg_location_longitude"],
        #           message_data["msg_location_latitude"])
        self._execute_query(query, f"Insert {message_data}")
    
    def get_msg_new(self,userid):
        query = f"SELECT * FROM message WHERE userid = {userid} ORDER BY msg_id DESC LIMIT 1;"
        self._execute_query(query)
        return self.cursor.fetchall()
    
    #to show the user's all message history
    def get_msg_all(self,userid):
        query = f"SELECT * FROM message WHERE userid = {userid}"
        self._execute_query(query)
        return self.cursor.fetchall()
    
    #to show the message around the user
    def show_msg(self,latitude,longitude,distance_km):
        query = f"""
            SELECT *, 
            (6371 * acos(cos(radians({latitude})) * cos(radians(msg_location_latitude)) * cos(radians(msg_location_longitude) 
            - radians({longitude})) + sin(radians({latitude})) * sin(radians(msg_location_latitude)))) 
            AS distance
            FROM message
            HAVING distance < {distance_km}
            ORDER BY distance;
        """
        self._execute_query(query)
        return self.cursor.fetchall()
    

    def like_msg(self, msgid, userid):
        query = f"UPDATE message SET msg_likes = msg_likes + 1 WHERE msg_id = {msgid} AND userid = {userid};"
        self._execute_query(query, f"Like message {msgid}")

    def update_data_location(self, userid, latitude, longitude):
        query = f"UPDATE user SET location_longitude = {longitude}, location_latitude = {latitude} WHERE userid = {userid};"
        self._execute_query(query, f"Update user location {userid}")
    
    def get_new_location(self, userid):
        query = f"SELECT location_longitude, location_latitude FROM user WHERE userid = {userid};"
        self._execute_query(query, f"Get user location {userid}")
        return self.cursor.fetchall()

