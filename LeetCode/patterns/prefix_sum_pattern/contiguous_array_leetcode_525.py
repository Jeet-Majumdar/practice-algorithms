"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Ref Video: https://www.youtube.com/watch?v=Xkl4EknqW8Y
        # 111 000
        # How to know to shrink window or increase?
        # Have to split, thus recursive and worse than O(n^2)

        # Not every result starts at beginning, e.g. 111 00

        # is it possible to know exactly where the first 1 was, and verify that after it
        # count[1] == count[0]

        # map each index to pair (count[0], count[1])
        # Use diff between counts for O(1) lookup of what we need
        
        count = 0
        res = 0
        diff_index = {} # diff --> index   [diff=count[1]-count[0]]
        diff_index[0] = -1

        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1
        
            if count not in diff_index:
                diff_index[count] = i
            else:
                res = max(res, i -  diff_index[count])
        
        return res
