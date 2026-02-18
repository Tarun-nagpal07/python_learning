'''Use heapq to build a priority queue of tasks (priority 1=urgent, 5=low). Add 8 tasks, process
them in priority order, and log each step using the logging module.'''

import logging
import heapq

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

priority_queue = []

tasks = [
    (1, "Fix crash"),
    (3, "Refactor code"),
    (2, "Update UI"),
    (5, "Write docs"),
    (4, "Email team"),
    (2, "Test new feature"),
    (1, "Critical bug fix"),
    (3, "Deploy to server")
]

for task in tasks:
    heapq.heappush(priority_queue,task)
    logging.info(f"Task Added : {task[1]} with P {task[0]}")


logging.info("....Processing Tasks... : ")

while priority_queue:
    priority, task_name = heapq.heappop(priority_queue)
    logging.info(f"Processing: {task_name} (P{priority})")