from threading import Thread, Lock
import time

base_value = 0

def increase(lock):
    global base_value

    #or lock.acquire().
    with lock:
        local_copy = base_value
        local_copy +=1
        time.sleep(0.1)
        base_value = local_copy
    # lock.release()
    # without lock end value = 1

if __name__ == "__main__":
    lock = Lock()

    print('start value', base_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('End value', base_value)
    # 2

    print('End main')