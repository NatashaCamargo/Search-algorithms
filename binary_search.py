# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:25:59 2021

@author: Natasha Camargo
"""
def binary_search(list, target):
    left_pointer = 0
    right_pointer = len(list)
    
    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer)//2
        mid_val = list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            right_pointer = mid_idx
        if target > mid_val:
            left_pointer = mid_idx + 1
            
        
            
