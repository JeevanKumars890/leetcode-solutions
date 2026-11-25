## Problem: Valid Anagram (Easy)
**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
I counted how many times each character appears in the first string using a dictionary. Then I went through the second string and reduced the counts. If a character is missing or runs out, the strings are not anagrams.

### Complexity
- Time: O(n)
- Space: O(k), where k is the number of distinct characters (at most 26 for lowercase letters)

### Notes
Checking the lengths first lets me return False early for strings like "a" and "ab". Sorting both strings would also work, but it takes O(n log n).