import threading
import time

n = 5
delay = 0.5

def firstfunc(n):
    for i in range(n):
        time.sleep(delay)
        print(f"first thread {i}")

def secondfunc(n):
    for i in range(n):
        time.sleep(delay)
        print(f"second thread {i}")

def main():
    thread1 = threading.Thread(target=firstfunc, args=(n,))
    thread2 = threading.Thread(target=secondfunc, args=(n,))

    thread1.start()
    thread2.start()
    print("stop")


if __name__ == '__main__':
    main()