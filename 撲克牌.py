# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:47:57 2024

@author: Student
"""

import random

# 建立撲克牌
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [rank + suit for suit in suits for rank in ranks]

# 洗牌
random.shuffle(deck)

# 分發給四個人，並排序
players_hands = [sorted(deck[i::4], key=lambda x: (ranks.index(x[:-1]), x[-1])) for i in range(4)]

# 顯示每位玩家的牌
for i, player_hand in enumerate(players_hands):
    print(f"Player {i+1}: {player_hand}")
