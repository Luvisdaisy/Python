#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#


# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_s = "".join(str(x) for x in digits)
        num_i = int(num_s)
        num_i += 1
        num_s = str(num_i)
        return [int(x) for x in num_s]


# @lc code=end
