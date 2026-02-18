'''Use threading.Thread to run 5 tasks simultaneously. Each task sleeps for a random time (1-
3 seconds) and prints a completion message. Wait for all threads to finish.'''

import threading
import random
import time
def task():
    slp = random.randint(1,3)
    print(f"{threading.current_thread().name} is going to sleep for {slp} s")
    time.sleep(slp)
    print(f"{threading.current_thread().name} is started runnning")


threads = []

for _ in range(5):
    thread = threading.Thread(target=task)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print("Finished")