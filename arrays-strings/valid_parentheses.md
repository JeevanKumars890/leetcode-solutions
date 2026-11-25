## Problem: Valid Parentheses (Easy)
**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach
I used a stack. Each opening bracket is pushed onto the stack. When a closing bracket appears, I pop the top of the stack and check that it is the matching opening bracket. At the end, the stack must be empty.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
A string like "(" fails because the stack is not empty at the end. A string like ")" fails because there is nothing to pop, so I check that the stack is not empty first.