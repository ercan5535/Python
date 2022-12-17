from threading import Thread
import os 
import time

def square_number(n):
    for i in range(n):
        i * i
    time.sleep(5)

if __name__ == "__main__":
    threads = []
    num_threads = 10 

    # create threads
    for i in range(num_threads):
        t = Thread(target=square_number, args=(100,))
        threads.append(t)

    print(threads)
    # [<Thread(Thread-1 (square_number), initial)>, <Thread(Thread-2 (square_number), initial)>, <Thread(Thread-3 (square_number), initial)>, <Thread(Thread-4 (square_number), initial)>, <Thread(Thread-5 (square_number), initial)>, <Thread(Thread-6 (square_number), initial)>, <Thread(Thread-7 (square_number), initial)>, <Thread(Thread-8 (square_number), initial)>, <Thread(Thread-9 (square_number), initial)>, <Thread(Thread-10 (square_number), initial)>]

    # start
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()
    # The main purpose of join() is to ensure that a child process has completed 
    # before the main process does anything that depends on the work of the child process.

    print('End main')