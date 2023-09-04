'''
Author       : Tian Haotian qi_7ran@163.com
Date         : 2023-05-11 20:15:52
LastEditors  : Tian Haotian qi_7ran@163.com
LastEditTime : 2023-05-16 22:53:27
FilePath     : \VSCodePros\Python\KeepLearning\day1-15\day1.py
Description  : 
'''
from math import sqrt
from random import randint


def Craps():
    first = randint(1, 6)+randint(1, 6)
    goon = True
    print('first=', first)
    if first == 7 or first == 11:
        print('player win!')
    elif first == 3 or first == 2 or first == 12:
        print('computer win!')
    else:
        while goon:
            second = randint(1, 6)+randint(1, 6)
            print('second=', second)
            goon = False
            if second == 7:
                print('pc win!')
            elif second == first:
                print('player win!')
            else:
                goon = True


def Fibonacci():
    fiob = []
    for i in range(0, 19):
        if i == 0 or i == 1:
            fiob.append(1)
        else:
            fiob.append(fiob[i-2]+fiob[i-1])
    print(fiob)


def PerfectNum():
    for num in range(1, 10000):
        sum = 0
        for factor in range(1, num):
            if num % factor == 0:
                sum += factor
        if sum == num:
            print('%d is a PERFECT number' % num)


def is_Prim():
    prim = []
    for num in range(2, 100):
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
        if(flag):
            prim.append(num)
    print(prim)

