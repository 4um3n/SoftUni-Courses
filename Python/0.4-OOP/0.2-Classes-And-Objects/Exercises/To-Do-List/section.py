class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        [self.tasks.remove(task) for task in completed_tasks]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        info = [f"Section {self.name}:"]
        info.extend([task.details() for task in self.tasks])
        return '\n'.join(info)
