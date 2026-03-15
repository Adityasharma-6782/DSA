arr1 = list(map(int,input("Enter element for first array: ").split()))
arr2 = list(map(int,input("Enter element for second array: ").split()))

i=j=0

while i<len(arr1) and j<=len(arr2):
    if arr1[i]==arr2[j]:
        print(arr1[i])
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        i+=1
    else:
        j+=1
    