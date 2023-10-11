#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = reversed(s.split(" "))
        for w in words:
            if w != "":
                return len(w)


# s = "luffy is still joyboy"
# test = Solution()
# r = test.lengthOfLastWord(s)
# print(r)

# @lc code=end
