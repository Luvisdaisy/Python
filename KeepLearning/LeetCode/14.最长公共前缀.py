#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        m = len(strs)
        n = len(strs[0])
        for col in range(n):
            for row in range(1, m):
                thisStr, prevStr = strs[row], strs[row - 1]
                if (
                    col >= len(thisStr)
                    or col >= len(prevStr)
                    or thisStr[col] != prevStr[col]
                ):
                    return strs[row][:col]
        return strs[0]


# @lc code=end
