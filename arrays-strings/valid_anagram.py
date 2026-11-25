def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if count.get(ch, 0) == 0:
            return False
        count[ch] -= 1
    return True

# Tests
print(is_anagram("anagram", "nagaram"))  # typical case, expect True
print(is_anagram("rat", "car"))          # typical case, expect False
print(is_anagram("a", "ab"))             # edge case: different lengths, expect False