from auction.bidding import calculate_bid

def run_auction(task, workers):
    bids = []
    for worker in workers:
        bid = calculate_bid(worker, task)
        if bid is not None:
            bids.append((worker, bid))
    
    if not bids:
        return None, None
    
    winner = min(bids, key=lambda x: (x[1], x[0].worker_id))
    winner[0].add_task(task)
    return winner[0], winner[1]

def print_auction_results(workers, auction_results, unassigned_tasks):

    print("=== Auction Results ===\n")
    for result in auction_results:
        if not result[1]:
            print(f"Task {result[0].task_id} -> Unassigned\n")
        else:
            print(f"Task {result[0].task_id} -> Worker {result[1].worker_id} (Bid: {result[2]})\n")
    
    print("=== Final Worker Loads ===\n")
    for worker in workers:
        task_ids = [task.task_id for task in worker.tasks]
        print(f"Worker {worker.worker_id}")
        print(f"Tasks: {task_ids}")
        print(f"Workload: {worker.current_workload()}\n")

    print("=== Unassigned Tasks ===\n")
    if not unassigned_tasks:
        print("None")
    else:
        for task in unassigned_tasks:
            print(task.task_id)

def auction_all_tasks(tasks, workers):
    auction_results = []
    unassigned_tasks = []
    for task in tasks:
        winner, winning_bid = run_auction(task, workers)
        if winner:
            assigned = (task, winner, winning_bid)
            auction_results.append(assigned)
        else:
            auction_results.append((task, None, None))
            unassigned_tasks.append(task)
    
    print_auction_results(workers, auction_results, unassigned_tasks)