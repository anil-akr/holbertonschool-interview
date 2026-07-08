#!/usr/bin/python3
"""Module that calculates the minimum number of
items needed to reach a certain amount"""


def makeChange(coins, total):
    if total == 0 or total < 0:
        return 0

    min_coins = [(float('inf'))] * (total + 1)
    min_coins[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                min_coins[amount] = min(min_coins[amount],
                                        min_coins[amount - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
