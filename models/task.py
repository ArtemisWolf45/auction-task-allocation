class Task:
    def __init__(self, task_id, position, deadline, complexity):
        self.task_id = task_id
        self.position = position
        self.complexity = complexity  # 1 to 5 scale describing the complexity of the task
        self.deadline = deadline
        
