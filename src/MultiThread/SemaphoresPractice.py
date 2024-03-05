import time
from threading import Semaphore, Thread

sema = Semaphore(3)


def display(name):

    sema.acquire()
    for i in range(4):
        print(f"Before Name {name}")
        time.sleep(1)
        print(f"After Name {name}")
        sema.release()

if __name__ == '__main__':
    threads = []

    for i in range(5):
        name = f"Thread {i}"
        t = Thread(target=display, args=(name,))
        threads.append(t)

    for i in threads:
        i.start();

