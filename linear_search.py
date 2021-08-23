# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:07:39 2021

@author: Natasha Camargo
"""

recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "avocado"

def linear_search(search_list, target_value):
    for id in range(len(search_list)):
        if search_list[id] == target_value:
            return id
    raise ValueError("{0} not in list".format(target_value))
    
    
print(linear_search(recipe, target_ingredient))