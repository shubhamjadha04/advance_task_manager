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
    def __init__(self):
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

class Normaluser(User):

    def view_task(self):
        pass

    def update_task_status(self):
        pass

    









                


    