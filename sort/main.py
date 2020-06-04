# -*- coding: utf-8 -*-
"""
    
    ~~~
    
    
    
    :author: Huangbo
    :date: 2020/6/4
"""
from sort.commons import generate_random_list, generate_nearly_sorted_list, evaluate_sort
from sort.sorts.bubble_sort import bubble_sort
from sort.sorts.insertion_sort import insertion_sort
from sort.sorts.selection_sort import selection_sort

# 乱序排序
from sort.sorts.shell_sort import shell_sort

print()
print('-------------乱序排序-------------')
l = generate_random_list(n=2000)
evaluate_sort(selection_sort, l.copy())
evaluate_sort(insertion_sort, l.copy())
evaluate_sort(bubble_sort, l.copy())
evaluate_sort(shell_sort, l.copy())
# 几乎有序排序
print()
print('-------------几乎有序排序-------------')
l2 = generate_nearly_sorted_list(n=2000, swap=100)
evaluate_sort(selection_sort, l2.copy())
evaluate_sort(insertion_sort, l2.copy())
evaluate_sort(bubble_sort, l2.copy())
evaluate_sort(shell_sort, l.copy())
