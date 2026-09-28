class Task:
    def __init__(self,task_id,title ,description, status,priority,assigned_user,):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.assigned_user = assigned_user



    def display_info(self):
        print(f"ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Priority: {self.priority}")
        print(f"Assigned_user: {self.assigned_user.user_name}")



        