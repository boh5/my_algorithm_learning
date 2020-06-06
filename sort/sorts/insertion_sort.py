# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/4
"""
from typing import List


def insertion_sort(l: List) -> List:
    length = len(l)
    for i in range(1, length):
        tmp_val = l[i]
        j = i + 1
        while j > 0:
            j -= 1
            if l[j - 1] < tmp_val:
                break
            l[j] = l[j - 1]
        l[j] = tmp_val

    return l


def insertion_sort_lr(l: List, left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        tmp_val = l[i]
        j = i + 1
        while j > left:
            j -= 1
            if l[j - 1] < tmp_val:
                break
            l[j] = l[j - 1]
        l[j] = tmp_val
