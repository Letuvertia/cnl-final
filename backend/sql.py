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
                
    
    def _execute_query(self, sql_query, success_log="") -> None:
        try:
            self.cursor.execute(sql_query)
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
                email varchar(255)
            );
            """
        self._execute_query(query, "Create table 'user'")
    
    def add_user(self, user_data) -> None:
        query = f"""
            INSERT INTO user (username, email)
            VALUES ('{user_data["username"]}', '{user_data["email"]}');
        """
        self._execute_query(query, f"Insert {user_data}")
    
<<<<<<< Updated upstream
    def get_user(self, userid):
        query = f"SELECT * FROM user WHERE userid = {userid};"
=======
    def get_user_login(self, email):
        query = f"SELECT * FROM user WHERE email = '{email}';"
        self._execute_query(query,"get user by email")
        return self.cursor.fetchall()
    
    def get_user_id(self,userid):
        userid = int(userid)
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
>>>>>>> Stashed changes
        self._execute_query(query)
        return self.cursor.fetchall()

