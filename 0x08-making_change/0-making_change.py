#!/usr/bin/python3
"""
This module provides a function to determine fewest coins
needed to meet a given amount
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins

    :param coins: list of integers representing the coin dominations
    :parem total: integer representing the toal amount
    :return: Fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
