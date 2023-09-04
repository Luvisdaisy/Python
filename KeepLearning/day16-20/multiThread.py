import glob
import os
from random import randint
import threading
import time
import math
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

PREFIX = "thumbnails"


def generate_thumbnail(infile, size, format="PNG"):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind("/") + 1 :]
    outfile = f"{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}"
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def image_main():
    """图片压缩主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob("*.png"):
        for size in (32, 64, 128):
            threading.Thread(
                target=generate_thumbnail, args=(infile, (size, size))
            ).start()


class Account(object):
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.RLock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            time.sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        with self.condition:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, ":", money, "====>", account.balance)
        time.sleep(1)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, ":", money, "<====", account.balance)
        time.sleep(1)


def acount_main():
    """存钱主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(10):
            pool.submit(sub_money, account)


PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def prim_main():
    """素数主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print("%d is prime: %s" % (number, prime))


if __name__ == "__main__":
    # acount_main()
    prim_main()
