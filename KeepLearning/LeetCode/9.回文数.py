#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = 0
        temp = x
        while temp > 0:
            last_num = temp % 10
            temp = temp//10
            y = y * 10 + last_num
        return y == x


# @lc code=end
