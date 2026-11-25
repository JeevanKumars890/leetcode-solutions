def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return len(stack) == 0

# Tests
print(is_valid("()[]{}"))  # typical case, expect True
print(is_valid("(]"))      # typical case: wrong type, expect False
print(is_valid("("))       # edge case: never closed, expect False