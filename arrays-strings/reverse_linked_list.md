## Problem: Reverse Linked List (Easy)
**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach
I walked through the list once with three pointers: previous, current, and next. At each node I saved the next node, pointed the current node backward to the previous one, and then moved all pointers forward. At the end, the previous pointer is the new head.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
An empty list works because the loop never runs and the function returns None. A recursive solution is also possible, but it uses O(n) space for the call stack.