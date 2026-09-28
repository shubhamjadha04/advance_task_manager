from models.user import User
from models.task import Task
from models.project import Project

user1 = User(
    1,
    "Shubhamjadhao",
    "shubham@gmail.com",
    "Admin"
)

# user1.display()


task1 = Task(
    1,
    "navbar",
    "Add a good navbar",
    "IN process",
    "High",
    user1
)

task2 = Task(
    2,
    "footer",
    "add a footer",
    "pending",
    "low",
    user1
)


project1 = Project(
    1,
    "advance task manager",
    "A task manager App"
)

project1.add_task(task1)
project1.add_task(task2)

project1.display_info()