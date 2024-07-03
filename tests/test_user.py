import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "john_doe", "john@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.user_id, "1")
        self.assertEqual(self.user.username, "john_doe")
        self.assertEqual(self.user.email, "john@example.com")

    def test_user_representation(self):
        self.assertEqual(str(self.user), "User(1, john_doe, john@example.com)")

if __name__ == '__main__':
    unittest.main()
