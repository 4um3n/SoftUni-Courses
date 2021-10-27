class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, name):
        if name == self.name:
            return f"Name cannot be the same."

        self.name = name
        return self.name

    def change_due_date(self, due_date):
        if due_date == self.due_date:
            return f"Date cannot be the same."

        self.due_date = due_date
        return self.due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, index, comment):
        if index not in range(len(self.comments)):
            return f"Cannot find comment."

        self.comments[index] = comment
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
