def b2D(bin):
    """二进制转换十进制

    Args:
        bin (str): 二进制数的字符串
    """
    deci = 0
    for i in range(len(bin)):
        capital = len(bin) - 1 - i
        deci += int(bin[i]) * 2**capital
    return deci


print(b2D("10111010101"))
