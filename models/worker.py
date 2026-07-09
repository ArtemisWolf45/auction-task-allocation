class Worker:
    def __init__(self, worker_id, position, capacity):
        self.worker_id = worker_id
        self.position = position
        self.capacity = capacity
        self.tasks = []

    def current_workload(self):
        return sum(task.complexity for task in self.tasks)
    
    def can_take_task(self, task):
        return self.current_workload() + task.complexity <= self.capacity

    def add_task(self, task):
        self.tasks.append(task)
        self.position = task.position

    def __str__(self):
        return f"Worker {self.worker_id}: {self.current_load()} tasks"
