#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        sum = 0
        i = 0
        while i < len(s):
            temp_str = s[i:i+2]
            if temp_str in roma:
                sum += roma.get(temp_str)
                i += 2
            else:
                sum += roma.get(s[i])
                i += 1
        return sum
# @lc code=end
