#!/usr/bin/python3
def makeChange(coins, total):
    """returns the fewest number of coins"""
    coins.reverse()
    number_of_coins = 0
    times = 0
    if total > 0:
        for coin in coins:
            times = int(total / coin)
            number_of_coins += times
            total = total - (coin * times)
        if total == 0:
            return number_of_coins
        else:
            return -1
    else:
        return 0
