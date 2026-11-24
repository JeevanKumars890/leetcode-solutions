def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Tests
a = ["h", "e", "l", "l", "o"]
reverse_string(a)
print(a)  # typical case, expect ['o', 'l', 'l', 'e', 'h']

b = ["a"]
reverse_string(b)
print(b)  # edge case: single element, expect ['a']