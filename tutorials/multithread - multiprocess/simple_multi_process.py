from multiprocessing import Process
import os 
import time

def square_number(n):
    for i in range(n):
        i * i
    time.sleep(5)

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()
    print(num_processes)
    # 8 

    # create processes
    for i in range(num_processes):
        p = Process(target=square_number, args=(100,))
        processes.append(p)

    print(processes)
    # [<Process name='Process-1' parent=7204 initial>, <Process name='Process-2' parent=7204 initial>, <Process name='Process-3' parent=7204 initial>, <Process name='Process-4' parent=7204 initial>, <Process name='Process-5' parent=7204 initial>, <Process name='Process-6' parent=7204 initial>, <Process name='Process-7' parent=7204 initial>, <Process name='Process-8' parent=7204 initial>]

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()
    # The main purpose of join() is to ensure that a child process has completed 
    # before the main process does anything that depends on the work of the child process.

    print('End main')