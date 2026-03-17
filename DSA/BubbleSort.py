def bubblSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

arr = list(map(int, input("Enter elements in an array: ").split()))

arr = bubblSort(arr)

print("Sorted array: ", arr)
