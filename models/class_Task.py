class Task:
    def __init__(self, task_id, description, assignee, status='Pending'):
        self.task_id = task_id
        self.description = description
        self.assignee = assignee
        self.status = status

    def __str__(self):
        return f"Task({self.task_id}, {self.description}, assigned to: {self.assignee}, status: {self.status})"
