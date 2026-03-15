def three_sum(nums):
    # Initialize an empty list to store the results
    result = []
    # Sort the input list in ascending order to easily manage duplicates and use two pointers
    nums.sort()

    # Iterate through the list up to the third-to-last element
    for i in range(len(nums) - 2):
        # Skip duplicate values at the current position to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set two pointers, 'l' and 'r', to find the other two elements in the triplet
        l, r = i + 1, len(nums) - 1

        # Perform a two-pointer search to find triplets with the sum equal to zero
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                # If sum is positive, the right pointer should move left to decrease the sum
                r -= 1
            elif s < 0:
                # If sum is negative, the left pointer should move right to increase the sum
                l += 1
            else:
                # Found a triplet with the sum equal to zero, add it to the result
                result.append([nums[i], nums[l], nums[r]])
                # Remove duplicates in the left and right pointers
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                # Move the pointers inwards to find the next unique triplet
                l += 1
                r -= 1
    return result

# Example usage from the w3resource snippet
# x = [1, -6, 4, 2, -1, 2, 0, -2, 0]
x = list(map(int,input("Enter element for first array: ").split()))
print(f"Original array: {x}")
print(f"Unique triplets that sum to zero: {three_sum(x)}")
# Sample Output: [(-6, 2, 4), (-2, 0, 2), (-1, 0, 1)]
