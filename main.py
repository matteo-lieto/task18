from models.user import User
from models.task import Task
from models.project import Project
from data_access.data_manager import save_data, load_data

def main():
    # Simulate loading data
    users = load_data('data/users.txt') or []
    tasks = load_data('data/tasks.txt') or []

    # Create some users and tasks
    user1 = User("1", "john_doe", "john@example.com")
    users.append(user1)
    task1 = Task("1", "Fix bug in code", user1.username)
    tasks.append(task1)

    # Save data
    save_data(users, 'data/users.txt')
    save_data(tasks, 'data/tasks.txt')

    # Output for demonstration
    for user in users:
        print(user)
    for task in tasks:
        print(task)

if __name__ == '__main__':
    main()
