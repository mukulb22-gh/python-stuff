import concurrent.futures
import time

start = time.perf_counter()

def todo(sec):
    print(f'start process for {sec} seconds sleep')
    time.sleep(sec)
    #print(f'end process of {sec} seconds sleep')
    return f'end process of {sec} seconds sleep'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(todo, 1.5)
#     f2 = executor.submit(todo, 1.5)
#     print(f1.result())
#     print(f2.result())

"""
Run in loop
"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    # using list comprehension method
    results = [executor.submit(todo, sec) for sec in seconds]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 4)} second(s)')