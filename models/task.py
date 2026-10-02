from datetime import datetime
from models.user import User

class Task:
    def __init__(self,task_id,title ,description, status,priority,assigned_user,deadline):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.assigned_user = assigned_user
        self.deadline = deadline



    def display_info(self):
        print(f"ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Priority: {self.priority}")
        print(f"Assigned_user: {self.assigned_user.user_name}")
        print(f"Deadline: {self.deadline} ")
        self.check_due(self.deadline)

    # update status method
    def update_status(self,new_status):
        valid_status = ["Pending", "In progress","completed"]

        if new_status in valid_status:
            self.status = new_status
            print("status updated Successful.")

        else:
            print("Invalid status.")


    # update priority method
    def update_priority(self, new_priority):
        valid_priority = ["High", "Medium", "Low"]

        if new_priority in valid_priority:
            self.priority = new_priority
            print("Priority updated successfully.")

        else:
            print("Invalid priority.")


    # check due date
    def check_due(self,deadline):
        deadline_date = deadline.date()
        today = datetime.now().date()

        if today == deadline_date:
            print("Due Today")

        elif deadline_date < today:
            print("Over Due")

        else:
            remaining = deadline_date - today
            print(f"{remaining} days are remaining")


# task manager class
class Manager(User):
    def __init__(self):
        self.task_basket = []


    # add task method
    def add_task(self,task):
        self.task_basket.append(task)
        print("task added successfully")
        
        

    #  reomve task method
    def remove_task(self,task_id):

        for task in self.task_basket:
            if task.task_id == task_id:
                self.task_basket.remove(Task)
                print("Task remove successfully")
                return
            
        else:
            print("No task found")

    # display task method
    def display_task(self):
        for task in self.task_basket:
            task.display_info()
            