#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#


# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = self.b2D(a)
        num_b = self.b2D(b)
        num = num_a + num_b
        return self.d2B(num)

    def b2D(self, bin):
        """二进制转换十进制

        Args:
            bin (str): 二进制数的字符串
        """
        deci = 0
        for i in range(len(bin)):
            capital = len(bin) - 1 - i
            deci += int(bin[i]) * 2**capital
        return deci

    def d2B(self, dec):
        """十进制转换二进制

        Args:
            dec (int): 一个十进制整数
        """
        if dec == 0:
            return "0"  # 十进制数为0时，对应的二进制也为0

        binary = ""
        while dec > 0:
            binary = str(dec % 2) + binary
            dec = dec // 2

        return binary


# @lc code=end
