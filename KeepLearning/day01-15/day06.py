# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total*10+temp % 10
        temp //= 10
    return total == num


def is_prime(num):
    for factor in range(2, int(num*0.5)+1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

print(is_prime(5))