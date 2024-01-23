import json
import sys

import time
from contextlib import contextmanager


@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"time: {elapsed_time}")


def print_result(func):
    def write(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result

    return write


path = "/Users/bogdan/Documents/data_light.json"

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return (sorted(set(job['job-name'].lower() for job in arg if isinstance(job, dict)), key=str.lower)) if isinstance(arg, list) else []


@print_result
def f2(arg):
    return list(filter(lambda job: job.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda job: job +', с опытом Python', arg))


@print_result
def f4(arg):
    return [job + f", зарплата {salary} руб." for job, salary in zip(arg, range(100000, 200001, 1000))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
