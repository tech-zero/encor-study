from multiprocessing import Process
from time import sleep, perf_counter

start = perf_counter()

processes = []

def test_func():
    sleep(2)
    print("Voila!")

for x in range(3):
    proc = Process(target=test_func)
    processes.append(proc)

for proc in processes:
    proc.start()

for proc in processes:
    proc.join()

end = perf_counter()
total_time = end - start
print(total_time)
