def squareRoot(n):
    s,e = 0,n
    ans = 0
    while s<=e:
        mid = s+(e-s)/2
        if mid * mid <= n:
            ans = mid
            s = mid+1
        else:
            e = mid-1
        
    # Decimal precision
    factor = 0.1
    for i in range(5):
        while (ans + factor) * (ans + factor) <= n:
            ans += factor
        factor /= 10

    return ans


num = int(input("Enter Number: "))

print(f"Sqrt of {num} is", squareRoot(num))