from models.task import Task

class User:
    def __init__(self,user_id, user_name,email,role):
        self.user_id = user_id
        self.user_name= user_name
        self.email = email
        self.role = role



    def display(self):
        print(f"ID : {self.user_id}")
        print(f"Name: {self.user_name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")

        
class Admin(User):
    def __init__(self,user_id, user_name,email,role):
        super().__init__(user_id, user_name,email,role)
        self.users= []


    # add user
    def add_user(self,user):
        self.users.append(user)
        print("user added successfully.")


    # remove user
    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print("successfully deleted")
                return
        else:
            print("no user found,")


    # find user
    def find_user(self,user_id):
        for user in self.users:
            if user.user_id == user_id:
                user.display()
                return

        else:
            print("user not found.")


#  manager class
class Manager(User):
    def __init__(self,user_id, user_name,email,role):
        super().__init__(user_id, user_name,email,role)
        self.task_basket = []


    # add task method
    def add_task(self,task):
        self.task_basket.append(task)
        print("task added successfully")
        
        

    #  reomve task method
    def remove_task(self,task_id):

        for task in self.task_basket:
            if task.task_id == task_id:
                self.task_basket.remove(task)
                print("Task remove successfully")
                return
            
        else:
            print("No task found")

    # display task method
    def display_task(self):
        for task in self.task_basket:
            task.display_info()



# normal User class
class Normaluser(User):

    def view_task(self):
        print("this is normal user.")

    def update_status(self,new_status):
        valid_status = ["Pending", "In progress","completed"]
    
        if new_status in valid_status:
            self.status = new_status
            print("status updated Successful.")
    
        else:
            print("Invalid status.")







                


    