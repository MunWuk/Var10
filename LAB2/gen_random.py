import random


def gen_random(count, start, finish):
    for _ in range(count):
        yield random.randint(start, finish)


pass
