def peakValue(arr):
    i, j = 0, len(arr) - 1

    while i < j:
        mid = i + (j - i) // 2

        if arr[mid] < arr[mid + 1]:
            i = mid + 1
        else:
            j = mid

    return i


arr = list(map(int, input("Enter Element of array: ").split()))

print("Peak Value at index", peakValue(arr))