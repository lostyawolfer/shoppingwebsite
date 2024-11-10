from multiprocessing import Process
import time

n = 5
delay = 0.5
def firstfunc(n):
    for i in range(n):
        time.sleep(delay)
        print(f'--- {i} is {n} stop ---')

def secondfunc(n):
    for i in range(n):
        time.sleep(delay)
        print(f'=== {i} is {n} stop ===')

def main():
    process1 = Process(target=firstfunc, args=(n,))
    process2 = Process(target=secondfunc, args=(n,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('!!! finished !!!')

if __name__ == '__main__':
    main()