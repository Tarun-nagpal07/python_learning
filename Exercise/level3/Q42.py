'''Create a shared counter incremented by 5 threads, each adding 1000. First show the race
condition (no lock), then fix it with threading.Lock() and verify the correct result of 5000.'''


import threading


count = 0

def task(lock):
    global count
    lock.acquire()
    print(f"Thread {threading.current_thread().name} is updating count")
    count += 1000
    lock.release()
lock = threading.Lock()

threads = [  threading.Thread(target=task,args=(lock,)) for _ in range(5) ]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Final Value of count : {count}")