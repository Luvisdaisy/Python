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
        first_string = strs[0]
        if not first_string:
            return ''
        longest_pre = ''
        for i in range(len(first_string)+1):
            pre = first_string[:i]
            for s in strs:
                if not s.startswith(pre):
                    return longest_pre
            longest_pre = pre


# @lc code=end
