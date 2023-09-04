from math import sqrt
from time import sleep

# 练习1：定义一个类描述数字时钟。


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x-other.x
        dy = self.y-other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def clock_main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


def point_main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-5, 7)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    # clock_main()
    point_main()
