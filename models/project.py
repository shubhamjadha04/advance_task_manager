class Project:
    def __init__(self,project_id,name,description):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.tasks = []


    def add_task(self,task):
        self.tasks.append(task)


    def display_info(self):
        print(f"Project ID: {self.project_id}")
        print(f"Project Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Total tasks: {len(self.tasks)}")

        print("\nTasks:")

        for task in self.tasks:
            print(f"-{task.title}")

            