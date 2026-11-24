## Problem: Reverse String (Easy)
**Link:** https://leetcode.com/problems/reverse-string/

### Approach
I used two pointers, one at the start and one at the end of the list. I swap the two elements and move the pointers toward each other until they meet. This reverses the list in place.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
A single-element list works because the loop never runs, since left is not less than right. The list is changed in place, so the function returns nothing.