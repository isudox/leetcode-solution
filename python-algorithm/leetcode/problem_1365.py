"""1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number
of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:

    2 <= nums.length <= 500
    0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def smaller_numbers_than_current(self, nums: List[int]) -> List[int]:
        store = [0] * 101
        for num in nums:
            store[num] += 1
        ans = []
        prev_cnt, cur_cnt = 0, 0
        for i in range(101):
            if store[i]:
                cur_cnt += store[i]
                store[i] = prev_cnt
                prev_cnt = cur_cnt
        for num in nums:
            ans.append(store[num])
        return ans
