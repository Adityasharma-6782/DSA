arr = list(map(int,input("Enter element in arr: ").split()))

arr=sorted(arr)

for i in range(0,len(arr)-1):
    if arr[i]==arr[i+1]:
        print("Duplicate value is",arr[i])
        break
