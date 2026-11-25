## Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach
I went through the prices once while tracking the lowest price seen so far. At each day I checked whether selling at that price would beat my best profit so far. This avoids comparing every pair of days.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
If prices only fall, no profit is possible, so the answer is 0. A brute-force check of every pair of days would take O(n²).