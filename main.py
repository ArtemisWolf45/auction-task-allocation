from sample_data import WORKERS, TASKS
from models.worker import Worker
from models.task import Task
from auction.auctioneer import auction_all_tasks

Workers = []
Tasks = []

for data in WORKERS:
    Workers.append(
        Worker(data["worker_id"],
               data["position"],
               data["capacity"]
        )
    )

for task in TASKS:
    Tasks.append(
        Task(task["task_id"],
             task["position"],
             task["deadline"],
             task["complexity"]
        )
    )

auction_all_tasks(Tasks, Workers)