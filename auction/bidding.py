def calculate_distance(worker, task):
    # Calculates absolute distance of the positions on a number line
    return abs(worker.position - task.position)

def calculate_bid(worker, task, load_penalty=3):
    if not(worker.can_take_task(task)):
        return None
    
    distance = calculate_distance(worker, task)

    if distance > task.deadline: # Checks if worker will reach task in time
        return None
    
    bid = distance + (worker.current_workload() * load_penalty) # penalises workers with larger workloads
    return bid