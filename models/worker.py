class Worker:
    def __init__(self, worker_id, position, capacity):
        self.worker_id = worker_id
        self.position = position
        self.capacity = capacity
        self.tasks = []

    def current_load(self):
        return len(self.tasks)
    
    def can_take_task(self):
        return self.current_load() < self.capacity

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Worker {self.worker_id}: {self.current_load()} tasks"
