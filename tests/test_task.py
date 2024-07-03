import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("1", "Fix bug in code", "john_doe")

    def test_task_creation(self):
        self.assertEqual(self.task.task_id, "1")
        self.assertEqual(self.task.description, "Fix bug in code")
        self.assertEqual(self.task.assignee, "john_doe")
        self.assertEqual(self.task.status, "Pending")

    def test_task_representation(self):
        expected = "Task(1, Fix bug in code, assigned to: john_doe, status: Pending)"
        self.assertEqual(str(self.task), expected)

if __name__ == '__main__':
    unittest.main()
