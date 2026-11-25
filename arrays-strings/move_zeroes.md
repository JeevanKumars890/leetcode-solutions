## Problem: Move Zeroes (Easy)
**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
I used two pointers. One pointer scans the list, and the other marks where the next non-zero number should go. Each time I find a non-zero number, I swap it into that spot. This pushes the zeros to the end and keeps the order of the other numbers.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
A list with a single zero, like [0], works because there is nothing to swap. The list is changed in place, so the function returns nothing.