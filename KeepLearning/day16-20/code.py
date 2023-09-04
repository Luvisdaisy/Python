import sys
import time


def merge(item1, item2, copm=lambda x, y: x < y):
    item = []
    index1 = 0
    index2 = 0
    while index1 < len(item1) and index2 < len(item2):
        if copm(item1[index1], item2[index2]):
            item.append(item1[index1])
            index1 += 1
        else:
            item.append(item2[index2])
            index2 += 1
    item += item1[index1:]
    item += item2[index2:]
    return item


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def seq_search(items, key):
    """顺序查找"""
    for index, items in enumerate(items):
        if items == key:
            return index
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key < items[mid]:
            end = mid - 1
        elif key > items[mid]:
            start = mid + 1
        else:
            return mid
    return -1


def fish():
    """穷举法 五人分鱼"""
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5
    return fish


"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价值重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


"""
* 是一个操作符，它用于将一个可迭代对象（如列表、元组或集合）解包（splat）并将其元素作为参数传递给一个函数或方法。这在参数数量不确定的函数或方法中非常有用，因为它允许您直接将可迭代对象作为参数传递，而不需要先创建一个元组或列表。
"""


def thief_pick_helper():
    """贪婪法求解带走最高价值物品"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.price, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            total_weight += thing.weight
            total_price += thing.price
            print(f"拿走了{thing.name}")
    print(f"总价值：$ {total_price}")


def quick_sort(items, comp=lambda x, y: x <= y):
    """
    快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
    """
    items = list(items[:])
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end="")
        print()


def patrol(board, row, col, step=1):
    """
    递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。  这什么玩意？
    """
    if row >= 0 and row < SIZE and col >= 0 and col < SIZE and board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f"第{total}种走法：")
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def dp():
    """
    动态规划
    子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值
    """
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


def main():
    items = [12, 55, 33, 123, 56, 88546, 234, 525, 13]
    # print(bin_search(items, 33))

    # fish()

    # thief_pick_helper()

    # print(quick_sort(items))

    # board = [[0] * SIZE for _ in range(SIZE)]
    # patrol(board, SIZE - 1, SIZE - 1)

    # dp()

    print(fib(5))

    # gen = calc_avg()
    # next(gen)
    # print(gen.send(10))
    # print(gen.send(20))
    # print(gen.send(30))


if __name__ == "__main__":
    main()
