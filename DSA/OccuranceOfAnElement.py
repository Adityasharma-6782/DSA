def FirstOccurrence(arr, num):
    i, j = 0, len(arr) - 1
    ans = -1

    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid] == num:
            ans = mid
            j = mid - 1   # move left to find first occurrence
        elif arr[mid] < num:
            i = mid + 1
        else:
            j = mid - 1

    return ans

def LastOccurrence(arr, num):
    i, j = 0, len(arr) - 1
    ans = -1

    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid] == num:
            ans = mid
            i = mid + 1   # move right to find first occurrence
        elif arr[mid] < num:
            i = mid + 1
        else:
            j = mid - 1

    return ans

arr = list(map(int, input("Enter element of array: ").split()))
num = int(input("Enter number: "))
x = FirstOccurrence(arr, num)
y = LastOccurrence(arr, num)
print("First Occurrence:", x)
print("Last Occurrence:", y)
