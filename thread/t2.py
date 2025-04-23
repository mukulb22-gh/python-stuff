"""
Asynchronus Example with how to pass arguments in thread
"""

import threading
import time

start = time.perf_counter()

def todo(sec):
    print(f"start the process and sleep for {sec} second")
    time.sleep(sec)
    print(f"end the process of {sec} sleep")

threads = []

for _ in range(15):
    t = threading.Thread(target=todo, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 4)} second(s)')

