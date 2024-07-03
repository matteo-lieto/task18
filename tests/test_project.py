import unittest
from models.project import Project
from models.task import Task

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = Project("1", "Project Alpha")
        self.task = Task("1", "Setup environment", "john_doe")

    def test_project_creation(self):
        self.assertEqual(self.project.project_id, "1")
        self.assertEqual(self.project.name, "Project Alpha")
        self.assertEqual(len(self.project.tasks), 0)

    def test_add_task(self):
        self.project.add_task(self.task)
        self.assertIn(self.task, self.project.tasks)
        self.assertEqual(len(self.project.tasks), 1)

    def test_project_representation(self):
        self.project.add_task(self.task)
        self.assertEqual(str(self.project), "Project(1, Project Alpha, Tasks: 1)")

if __name__ == '__main__':
    unittest.main()
