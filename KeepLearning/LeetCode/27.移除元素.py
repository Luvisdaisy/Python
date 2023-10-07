#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#


# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for index in len(nums):
            if nums[index] == val:
                nums[index] = nums[index + 1]


# @lc code=end
