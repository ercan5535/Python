from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()
        # processing...
        # without lock in Thread-9 (worker) got 17in Thread-8 (worker) got 18in Thread-7 (worker) got 19
        # with lock every print in single line
        with lock:
            print(f"in {current_thread().name} got {value}")    
        q.task_done()
        """if we set thread.daemon=False. daemon kills the threads if main thraed is completed
        without daemon=True, should put something like this
        if q.empty():
            break
        """
    
if __name__ == "__main__":
    lock = Lock()
    q = Queue()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True
        thread.start()

    for i in range(1,21):
        q.put(i)

    q.join()
    print(q.empty())
    print('End main')