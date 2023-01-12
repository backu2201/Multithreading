import multiprocessing as mp
import math
import time
from time import perf_counter
result1=[]
result2=[]
#result=[]
def cal_one(number):
    for i in number:
        result1.append(math.sqrt(i**3))
def cal_two(number):
    for i in number:
        result2.append(math.sqrt(i**5))
#numlist=list(range(1200000))
# start=perf_counter()
# cal_one(numlist)
# cal_two(numlist)
# end=perf_counter()
# print(f'{end-start}')
# print("hi")
if __name__=='__main__':
    numlist=list(range(200000))
    # p1=mp.Process(target=cal_one,args=(numlist,))
    # p2 = mp.Process(target=cal_one, args=(numlist,))
    start_time=perf_counter()
    # p1.start()
    # p2.start()
    cal_one(numlist)
    cal_two(numlist)
    end_time=perf_counter()
    print(f'{end_time-start_time}')



