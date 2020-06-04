# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/4
"""
from typing import List

from sort.sorts.insertion_sort import insertion_sort


def shell_sort(l: List, init_gap: int = 5, step: int = 1):
    gap = init_gap
    groups = len(l) // gap
    while gap > 0:
        for i in range(groups):
            tmp_list = insertion_sort(l[i * gap: (i + 1) * gap])
            index = i * gap
            for num in tmp_list:
                l[index] = num
                index += 1
        gap -= step