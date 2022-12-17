from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, numbers, lock):
    for i in range(100):
        time.sleep(0.1)
        with lock:
            number.value += 1

        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    shared_number = Value('i', 0)
    # i and d are dtype

    print("array at beginning is", shared_array[:])
    # array at beginning is [0.0, 100.0, 200.0]
    # without [:] <SynchronizedArray wrapper for <multiprocessing.sharedctypes.c_double_Array_3 object at 0x00000193775913D0>>
    print("number at the beginning", shared_number.value)
    # number at the beginning 0

    p1 = Process(target=add_100, args=(shared_number, shared_array, lock))
    p2 = Process(target=add_100, args=(shared_number, shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("array at end is", shared_array[:])
    # array at end is [200.0, 300.0, 400.0]
    print("number at the end", shared_number.value)
    # number at the end 200