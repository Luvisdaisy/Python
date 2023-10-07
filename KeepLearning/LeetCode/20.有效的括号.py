#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#


# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in map:
                top_elem = stack.pop() if stack else "#"
                if map[c] != top_elem:
                    return False
            else:
                stack.append(c)
        return not stack


# test = Solution()
# s = "()[]{}"
# test.isValid(s)

# @lc code=end
