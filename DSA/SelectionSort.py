def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            
    return arr
        

arr = list(map(int, input("Enter elements in an array: ").split()))

arr = selectionSort(arr)

print("Sorted array: ", arr)