#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        obj = 0
        for obj in range(len(haystack)):
            tar = 0
            while tar < len(needle) and obj < len(haystack):
                if haystack[obj] == needle[tar]:
                    tar += 1
                    if tar == len(needle):
                        return obj - tar
                obj += 1
            obj += tar
        return -1


test = Solution()
print(test.strStr("wozaizhelikanzheni", "likan"))

# @lc code=end
