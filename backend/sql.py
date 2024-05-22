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
    
    def get_user(self, userid):
        query = f"SELECT * FROM user WHERE userid = {userid};"
        self._execute_query(query)
        return self.cursor.fetchall()

