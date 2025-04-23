import threading
import time

"""
Synchronus Example
"""
start = time.perf_counter()

def todo():
    print("start the process and sleep for 1 second")
    time.sleep(1)
    print("end the process of sleep")


# todo()
# todo() # The no. of call increase the sleep process delay is increase
# finish = time.perf_counter()
# print(f'Finished in {round(finish-start, 2)} second(s)\n\n')


"""
Asynchronous Example:
instead of fininsh in two seconds it also complete in almost 1 sec
"""
# Example via threading

# t1 = threading.Thread(target=todo)
# t2 = threading.Thread(target=todo)

# t1.start() # start the thread
# t2.start() # start the thread

# t1.join() # wait until the thread is finished
# t2.join() # wait until the thread is finished


"""
Validate it for 10 calls
which are finishes in almost 1 sec
"""
threads = []

for _ in range(10):
    t = threading.Thread(target=todo)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

