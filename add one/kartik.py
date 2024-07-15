from numpy.random import randint
import matplotlib.pyplot as plt
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

elements=[]
times=[]
import time
arr=[13,26,28,30]
print("before sorting=",arr)
bubblesort(arr)
print("after sorting=",arr)
print("time complexities")
for i in range(1,10):
    arr=randint(0,1000*i,1000*i)
    start=time.time()
    bubblesort(arr)
    end=time.time()
    elements.append(len(arr))
    times.append(end-start)
    print(len(arr),"elements=",end-start)
plt.xlabel("list length")
plt.ylabel("time complexities")
plt.plot(elements,times,label="bubblesort")
plt.grid()
plt.legend()
plt.show()
