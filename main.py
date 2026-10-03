from models.user import Admin, Normaluser , Manager
from models.task import Task
from models.project import Project
from datetime import datetime

admin = Admin(
    1,
    "Shubhamjadhao",
    "shubham@gmail.com",
    "Admin"
)
manager = Manager(
    2,
    "raj",
    "rajkumar@gmail.com",
    "manager"
)

user1 = Normaluser(
    3,
    "hanschavhan",
    "hans@gmial.com",
    "user"
)

user2 = Normaluser(
    4,
    "ramesh",
    "ramesh@gmail.com",
    "user"
)


# admin.add_user(admin)
# admin.add_user(manager)
# admin.add_user(user1)









task1 = Task(
    1,
    "navbar",
    "Add a good navbar",
    "IN process",
    "High",
    user1,
    datetime(2026,9,20)
)

task2 = Task(
    2,
    "footer",
    "add a footer",
    "pending",
    "low",
    user1, 
    datetime(2026,9,20)
)

manager.add_task(task1)
manager.add_task(task2)
# manager.remove_task(2)


user1.update_status("completed")
manager.display_task()

# manager = TaskManager()
# manager.add_task(task1)
# manager.add_task(task2)

# manager.display_task()

# manager.remove_task(6)


# project1 = Project(
#     1,
#     "advance task manager",
#     "A task manager App"
# )


# project1.add_task(task2)
# task2.update_status("completed")
# task2.update_priority("High")
# task1.display_info()
# task2.display_info()


# project1.display_info()