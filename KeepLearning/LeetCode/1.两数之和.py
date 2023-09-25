#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#


# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index:
                return [index[complement], i]
            index[num] = i
        return []


# @lc code=end
