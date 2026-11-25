## Problem: Longest Common Prefix (Easy)
**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
I started with the first word as the prefix. For each other word, I shortened the prefix one letter at a time until the word started with it. If the prefix becomes empty, there is no common prefix.

### Complexity
- Time: O(S), where S is the total number of characters in all words
- Space: O(1)

### Notes
The shortest word limits the prefix, and the loop handles this automatically. An empty list returns an empty string.