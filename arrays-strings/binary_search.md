## Problem: Binary Search (Easy)
**Link:** https://leetcode.com/problems/binary-search/

### Approach
Because the list is sorted, I compared the target with the middle element and threw away the half that cannot contain it. I repeated this until I found the target or the search range was empty.

### Complexity
- Time: O(log n)
- Space: O(1)

### Notes
The loop condition must be left <= right, or a one-element range is skipped. If the target is missing, the function returns -1.