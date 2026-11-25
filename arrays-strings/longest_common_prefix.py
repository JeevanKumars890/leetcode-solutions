def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

# Tests
print(longest_common_prefix(["flower", "flow", "flight"]))  # typical case, expect fl
print(longest_common_prefix(["dog", "racecar", "car"]))     # edge case: no common prefix, expect empty line