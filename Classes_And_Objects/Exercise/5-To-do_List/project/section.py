from project.task import Task


class Section:

    def __init__(self, string):
        self.string = string
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.string}"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task_name == task:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with name {task_name}"

    def clean_section(self):
        complete_tasks = 0
        for task in self.tasks:
            if task.completed:
                complete_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {complete_tasks} tasks."

    def view_section(self):
        view = ""
        view += f"Section {self.string}\n"
        for task in self.tasks:
            view += f"{task.details()}\n"
        return view
