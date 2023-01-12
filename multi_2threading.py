from  threading import Thread
import multiprocessing as mp
from time import perf_counter
import os
def search_location(n,t):
    a=False
    for r,d,f in os.walk(t):
        for j in f:
            if j==n:
                print("file found in {}".format(r))
                a=True
                break
    if a:
        pass
    else:
        print("not found in",t)
if __name__=="__main__":
    n=input("Enter the name of file to search: ")
    p1 = mp.Process(target=search_location, args=(n, "C:\\"))
    p2 = mp.Process(target=search_location, args=(n, "D:\\"))
    start=perf_counter()
    p1.start()
    p2.start()
    end=perf_counter()
    print(f'{end-start} sec taken')
