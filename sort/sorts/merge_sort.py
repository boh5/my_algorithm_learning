# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/5
"""
from typing import List

from sort.sorts.insertion_sort import insertion_sort_lr


def __merge(arr: List, l: int, mid: int, r: int) -> None:
    tmp = [num for num in arr[l:r + 1]]
    i = l
    j = mid + 1
    for k in range(l, r + 1):
        if i > mid:
            arr[k] = tmp[j - l]
            j += 1
        elif j > r:
            arr[k] = tmp[i - l]
            i += 1
        else:
            if tmp[i - l] < tmp[j - l]:
                arr[k] = tmp[i - l]
                i += 1
            else:
                arr[k] = tmp[j - l]
                j += 1


def __merge_sort(arr: List, l, r) -> None:
    # if l >= r:
    #     return
    if (r - l) < 15:
        insertion_sort_lr(arr, l, r)
        return

    mid = (l + r) // 2
    __merge_sort(arr, l, mid)
    __merge_sort(arr, mid + 1, r)

    if arr[mid] > arr[mid + 1]:
        __merge(arr, l, mid, r)


def merge_sort(arr: List) -> None:
    __merge_sort(arr, 0, len(arr) - 1)
