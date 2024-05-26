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
                
    

    def _execute_query(self, sql_query, success_log="",param = None) -> None:
        try:
            self.cursor.execute(sql_query,param)

            self.connection.commit()

            if success_log:
                print(f"Success: {success_log}")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def create_user_table(self) -> None:
        query = """
            CREATE TABLE user (
                userid serial PRIMARY KEY,
                username varchar(255),
                password varchar(255)
                email varchar(255),
                location varchar(255),
                userid integer
            );
            """
        self._execute_query(query, "Create table 'user'")

        # user_data = {
        #     "username": "",
        #     "password": "",
        #     "email": "",
        #     "location": "",
        #     "userid":""
        # }

    def create_message_table(self) -> None:
        query = """
            CREATE TABLE message (
                msgid serial PRIMARY KEY,
                userid integer,
                msg_id integer,
                msg_content varchar(255),
                msg_likes integer,
                msg_location varchar(255),
                FOREIGN KEY (userid) REFERENCES user(userid)
            );
            """
        self._execute_query(query, "Create table 'message'")
        # msg_data = {
        #     "userid": "",
        #     "msg_id": "",
        #     "msg_content": "",
        #     "msg_likes": "",
        #     "msg_location": ""
        # }

    def add_user(self, user_data) -> None:
        check_query = f"SELECT * FROM user WHERE username = '{user_data['username']}' OR email = '{user_data['email']}' OR userid = '{user_data['userid']}'"
        self._execute_query(check_query)

        if self.cursor.fetchone():
            raise ValueError(f"User {user_data['id']} already exists")
        
        query = f"""
            INSERT INTO user (username,password, email,location,userid)
            VALUES ('{user_data["username"]}','{user_data["password"]}', '{user_data["email"]}', '{user_data["location"]}','{user_data["userid"]}');
        """
        self._execute_query(query, f"Insert {user_data}")
        
    
    def get_user_login(self, email):
        query = f"SELECT * FROM user WHERE email = {email};"
        self._execute_query(query,"get user by email")
        return self.cursor.fetchall()
    
    def get_user_id(self,userid):
        query = f"SELECT * FROM user WHERE userid = {userid};"
        self._execute_query(query,"get user by id")
        return self.cursor.fetchall()
    
    #def login 
    #def register
    
    def add_msg(self,message_data):
        query = """
            INSERT INTO message (userid, msg_id, msg_content, msg_likes, msg_location)
            VALUES (%s,%s,%s,%s,%s);
        """
        params = (message_data["userid"],message_data["msg_id"],message_data["msg_content"],message_data["msg_likes"],message_data["msg_location"])
        self._execute_query(query, f"Insert {message_data}",params)
    
    def get_msg_new(self,userid):
        query = f"SELECT * FROM message WHERE userid = {userid} ORDER BY msg_id DESC LIMIT 1;"
        self._execute_query(query)
        return self.cursor.fetchall()
    
    def get_msg_all(self,userid):
        query = f"SELECT * FROM message WHERE userid = {userid}"
        self._execute_query(query)
        return self.cursor.fetchall()
    
    # def show_msg(self,latitude,longitude,distance_km):
    #     query = """
    #     SELECT msg_id, msg_content, msg_likes, ST_AsText(msg_location) AS location, msg_user, userid
    #     FROM messages
    #     WHERE ST_DWithin(
    #         msg_location,
    #         ST_SetSRID(ST_MakePoint(%s, %s), 4326),
    #         %s * 1000
    #     );
    #     """
    #     params = (longitude, latitude, distance_km)
    #     self._execute_query(query, "Select messages within distance", params)
    #     return self.cursor.fetchall()

    def like_msg(self,msgid,userid):
        query = f"UPDATE message SET msg_likes = msg_likes + 1 WHERE msg_id = {msgid} AND userid = {userid};"
        self._execute_query(query, f"Like message {msgid}")

