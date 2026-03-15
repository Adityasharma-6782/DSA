def BinarySearch(arr, num):
    s,e=0,len(arr)-1
    while s<=e:
        mid = s+(e-s)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            s = mid+1
        else:
            e = mid-1
    return -1

arr = list(map(int,input("Enter element in ascending of array: ").split()))
num = int(input("Enter Number: "))
x = BinarySearch(arr,num)    
if x != -1:
    print(f"Number is present at index {x}.")
else:
    print("Number is not present")