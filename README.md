# Auction Task Allocation

A decentralized task allocation simulation where workers compete for tasks using a reverse auction mechanism.

## Features
- Reverse-auction based task allocation
- Dynamic bidding based on distance and current workload
- Capacity constraints
- Deadline feasibility checks
- Deterministic tie-breaking
- Handling of unassigned tasks

## Project Structure
```
project/
|
├── auction/
|   ├── auctioneer.py
|   └── bidding.py
|
├── models/
|   ├── task.py
|   └── worker.py
|
├── .gitignore
├── sample_data.py
├── main.py
└── README.md
```

## How to Run
```bash
python main.py
```

## Bidding Function

Each worker calculates a bid using:
```text
Bid = Distance + (Current Workload x Load Penalty)
```

The distance component of a worker's bid is calculated as the absolute difference between the worker's position and the task's position. A worker's workload is the sum of the complexities of all previously assigned tasks i.e the more complex tasks completed, the more workload a worker has. As a worker's workload increases, a load penalty raises future bids, making heavily loaded workers less likely to win additional tasks.

## Tie-Breaking Rule

If multiple workers submit the same lowest bid, then the worker with the lowest id is selected. This ensures deterministic and reproducible results.

## Design Assumptions

- Workers move to the location of a completed task
- Task complexity contributes to a workers workload
- Tasks are auctioned sequentially
- Distance is calculated on a one-dimensional number line
- Deadlines represent the maximum travel distance a worker can cover to reach a task

## Sample Outputs

### Auction Results
<img src="screenshots/sample_output_1.png" width="350" alt="Auction results output">

### Final Worker Loads + Unassigned Tasks
<img src="screenshots/sample_output_2.png" width="350" alt="Final worker loads and unassigned tasks output">

## Possible Improvements
- Allow workers to drop previously assigned tasks when a more suitable task is available
- Auction multiple tasks concurrently instead of sequentially
- Have workers and tasks be placed on a two-dimensional grid instead of a number line