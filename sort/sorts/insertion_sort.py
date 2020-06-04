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
        for j in range(i-1, -1, -1):
            if l[j] > tmp_val:
                l[j+1] = l[j]
            else:
                l[j] = tmp_val
                break

    return l
