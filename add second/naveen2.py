import matplotlib.pyplot as plt
from numpy.random import randint
def lenearSerch(arr,n,num):
    for i in range (n):
        if arr [i]==num:
            return i
    return -1
element=[]
times=[]
import time
arr=[10,15,30,85]
num=17
loc=lenearSerch(arr,len(arr),num)
if loc==1:
    print("not successful")
else:
    print("the element is present in index")
print("time complexity")
for i in range (1,10):
    arr=randint(0,10000*i,10000*i)
    start=time.time()
    lenearSerch(arr, len(arr), num)
    end=time.time()
    element.append(len(arr))
    times.append(end-start)
    print(len(arr),"element=...",end-start)
plt.xlabel("list length")
plt.ylabel("time complexity")
plt.plot(element,times,label="leneSerch")
plt.grid()
plt.legend()
plt.show()