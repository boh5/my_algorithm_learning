# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/4
"""
from typing import List, Tuple


def shell_sort(l: List, gap_list: Tuple = (109, 41, 19, 5, 1)) -> List:

    # for gap in gap_list:
    gap = len(l) // 2
    while gap > 0:
        groups = len(l) // gap
        for i in range(1, groups):
            tmp_val = l[gap * i]
            j = (i + 1) * gap
            while j > 0:
                j -= gap
                if l[j - gap] < tmp_val:
                    break
                l[j] = l[j - gap]
            l[j] = tmp_val
        gap //= 2
    return l
