# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/4
"""
import random
import time
from typing import List, Callable


def generate_random_list(n: int = 10000, start: int = 0, end: int = 10000) -> List[int]:
    l = []
    for i in range(n):
        l.append(random.randint(start, end))
    return l


def generate_nearly_sorted_list(n: int = 10000, swap: int = 100) -> List[int]:
    l = [i for i in range(n)]
    for i in range(swap):
        index_a = random.randint(0, n - 1)
        index_b = random.randint(0, n - 1)
        l[index_a], l[index_b] = l[index_b], l[index_a]
    return l


def is_sorted(func: Callable, l: List) -> None:
    for i in range(len(l) - 1):
        assert l[i] <= l[i + 1], f'Not Sorted! func<{func.__name__}> [{i}]={l[i]}, [{i + 1}]={l[i + 1]}'


def evaluate_sort(sort_func: Callable, l: List, repeat: int = 1) -> float:
    total_time = 0
    for i in range(repeat):
        list_tmp = l.copy()
        start = time.clock()
        sort_func(list_tmp)
        end = time.clock()
        is_sorted(sort_func, list_tmp)
        total_time += (end - start)
    print(f'{sort_func.__name__}: {total_time}s')
    return total_time
