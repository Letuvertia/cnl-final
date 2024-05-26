import unittest
from mysql.connector import Error
from sql import *

class TestMySQLConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 在测试开始前运行一次，用于初始化
        cls.db = MySQLConnector(host="localhost", database="locasync", user="admin", password="admin")
        cls.db.create_user_table()
        cls.db.create_message_table()
    
    @classmethod
    def tearDownClass(cls):
        # 在所有测试运行完毕后运行一次，用于清理
        cls.db._execute_query("DROP TABLE IF EXISTS message;", "Drop table 'message'")
        cls.db._execute_query("DROP TABLE IF EXISTS user;", "Drop table 'user'")
        cls.db.__exit__()
    
    def setUp(self):
        # 在每个测试用例开始前运行，用于准备测试环境
        self.test_user = {"username": "testuser", "email": "test@example.com", "password": "testpassword", "location": "TestLocation"}
        self.db.add_user(self.test_user)
        self.user_id = self.db.cursor.lastrowid  # 获取刚刚插入用户的ID

    def tearDown(self):
        # 在每个测试用例结束后运行，用于清理测试环境
        self.db._execute_query("DELETE FROM message;", "Delete all messages")
        self.db._execute_query("DELETE FROM user;", "Delete all users")

    def test_add_user(self):
        # 测试添加用户
        user_data = {"username": "newuser", "email": "new@example.com", "password": "newpassword", "location": "NewLocation"}
        self.db.add_user(user_data)
        result = self.db.get_user(self.user_id)
        self.assertIsNotNone(result)
        self.assertEqual(result[0][1], user_data["username"])

    def test_add_message(self):
        # 测试添加消息
        message_data = {
            "userid": self.user_id,
            "msg_id": 1,
            "msg_content": "This is a test message",
            "msg_likes": 0,
            "msg_location": "TestLocation"
        }
        self.db.add_msg(message_data)
        result = self.db.get_msg_new(self.user_id)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][2], message_data["msg_content"])

    def test_like_message(self):
        # 测试点赞消息
        message_data = {
            "userid": self.user_id,
            "msg_id": 1,
            "msg_content": "This is a test message",
            "msg_likes": 0,
            "msg_location": "TestLocation"
        }
        self.db.add_msg(message_data)
        self.db.like_msg(1, self.user_id)
        result = self.db.get_msg_new(self.user_id)
        self.assertEqual(result[0][4], 1)  # 检查点赞数是否为1

    def test_get_all_messages(self):
        # 测试获取所有消息
        message_data1 = {
            "userid": self.user_id,
            "msg_id": 1,
            "msg_content": "Message 1",
            "msg_likes": 0,
            "msg_location": "Location 1"
        }
        message_data2 = {
            "userid": self.user_id,
            "msg_id": 2,
            "msg_content": "Message 2",
            "msg_likes": 0,
            "msg_location": "Location 2"
        }
        self.db.add_msg(message_data1)
        self.db.add_msg(message_data2)
        result = self.db.get_msg_all(self.user_id)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
