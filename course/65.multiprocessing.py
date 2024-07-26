# multiprocessing

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    
    print(cpu_count())
    
    a = Process(target=counter, args=(250,))    
    b = Process(target=counter, args=(250,))
    c = Process(target=counter, args=(250,))    
    d = Process(target=counter, args=(250,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    
    print("finished in:", time.perf_counter(), "seconds")

if __name__ == "__main__":
    main()