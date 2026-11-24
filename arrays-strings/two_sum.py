def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

# Tests
print(two_sum([2, 7, 11, 15], 9))  # typical case, expect [0, 1]
print(two_sum([3, 3], 6))          # edge case: duplicates, expect [0, 1]