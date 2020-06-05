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
