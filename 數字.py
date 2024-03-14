# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:46:27 2024

@author: Student
"""

import random

n = int(input("請輸入 n（要隨機抽取的數字個數）："))
a = int(input("請輸入 a（隨機範圍起始值）："))
b = int(input("請輸入 b（隨機範圍結束值）："))

random_numbers = random.sample(range(a, b+1), n)
random_numbers = list(set(random_numbers))  # 刪除重複數字
random_numbers.sort(reverse=True)  # 由大到小排序

print(f"隨機抽取、刪除重複並排序後的數字列表：{random_numbers}")
