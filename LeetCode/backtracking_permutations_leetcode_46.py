"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List

# https://www.youtube.com/watch?v=s7AvT7cGdSo&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
                res.append(perm)
            
            nums.append(n)
        
        return res

