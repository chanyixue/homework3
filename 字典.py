# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:33:02 2024

@author: Student
"""

lower_to_upper_dict = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z'
}

input_letter = input("請輸入一個小寫英文字母：")
upper_letter = lower_to_upper_dict.get(input_letter, "找不到對應的大寫字母")

print(f"轉換為大寫字母後為：{upper_letter}")
