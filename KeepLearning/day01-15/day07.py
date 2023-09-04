import os
import time
import sys
import random


# 练习1：在屏幕上显示跑马灯文字。
def zoumadeng():
    content = '北京欢迎你为你开天辟地…………'

    while True:
        os.system('cls')
        print(content)

        time.sleep(0.2)
        content = content[1:]+content[0]


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
def generate_code():
    code_len = 4
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


# 练习3：设计一个函数返回给定文件名的后缀名。
def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename)-1:
        index = pos if has_dot else pos+1
        return filename[index:]
    else:
        return ''


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


# 练习5：计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    return year % 4 == 0 and year % 100 == 0 or year % 400 == 0


def which_day(year, month, date):
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total+date


# 练习6：打印杨辉三角。
def triangles():
    num = int(input('Number of rows:'))
    yh = [[]]*num
    for row in range(len(yh)):
        yh[row] = [None]*(row+1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col]+yh[row-1][col-1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    triangles()
