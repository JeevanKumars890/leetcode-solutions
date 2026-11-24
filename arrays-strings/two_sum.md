## Problem: Two Sum (Easy)
**Link:** https://leetcode.com/problems/two-sum/

### Approach
I used a hash map to store the numbers I have already seen. For each number, I check whether its complement (target minus the number) is in the map. This avoids a nested loop.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
Duplicates like [3,3] work because I check the map before inserting the current number.