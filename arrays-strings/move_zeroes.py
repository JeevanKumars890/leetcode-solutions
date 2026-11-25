def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1

# Tests
a = [0, 1, 0, 3, 12]
move_zeroes(a)
print(a)  # typical case, expect [1, 3, 12, 0, 0]

b = [0]
move_zeroes(b)
print(b)  # edge case: single zero, expect [0]