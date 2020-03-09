import random


class Rand(object):

    __result = 0

    def rand(self, min=0, max=1, point_num=2):
        self.result = random.uniform(min, max)
        return self

    def add(self, value):
        self.result = self.result + value
        return self

    def red(self, value):
        self.result = self.result - value
        return self

    def output(self, point_num=2):
        return format(self.result, "." + str(point_num) + "f")


if __name__ == "__main__":
    print(Rand().rand().add(222).red(111).output())
