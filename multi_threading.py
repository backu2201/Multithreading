from threading import Thread
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
        print("no")
if __name__=="__main__":
    n=input("Enter the name of file to search: ")
    start=perf_counter()
    t1=Thread(target=search_location,args=(n,"c:\\"))
    print("Now thread2is working")
    t2=Thread(target=search_location,args=(n,"c:\\"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=perf_counter()
    print(f'{end-start} sec taken')
