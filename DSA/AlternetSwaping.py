import numpy as np

arr = np.array([1,2,3,4,5,6])

for i in range(0,len(arr),2):
    x = arr[i]
    arr[i]=arr[i+1]
    arr[i+1]=x

for i in range(len(arr)):
    print(arr[i])