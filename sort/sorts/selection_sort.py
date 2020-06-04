# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/4
"""
from typing import List


def selection_sort(l: List) -> None:
    length = len(l)
    for i in range(length):

        tmp_val = l[i]
        min_index = i
        for j in range(i, length):
            if l[j] < tmp_val:
                min_index = j
                tmp_val = l[j]
        l[i], l[min_index] = l[min_index], l[i]
