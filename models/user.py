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

        
        