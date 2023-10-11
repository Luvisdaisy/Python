#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.left_bound(nums, target)
        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index
        #     elif index + 1 == len(nums):
        #         return index + 1
        #     elif num < target and nums[index + 1] > target:
        #         return index + 1

    def left_bound(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                right = mid + 1
            elif nums[mid] > target:
                right = mid
        return right


# nums = [1, 3, 5, 6]
# target = 7
# s = Solution()
# r = s.searchInsert(nums, target)
# print(r)
# @lc code=end
