#!/usr/bin/python3
"""prime game implementation module"""


def isWinner(x, nums):
    """returns the winner of the prime game"""
    ben_round_wins = []
    maria_round_wins = []
    if x <= 0:
        return None
    for limit in nums:
        ben_count = 0
        maria_count = 0
        captured_primes = []
        player = 2
        if limit >= 1:
            for number in range(1, limit + 1):
                found = False
                if len(captured_primes) > 0:
                    if check_number_validity(number, captured_primes):
                        if check_prime(number):
                            found = True
                            captured_primes.append(number)
                            if player % 2 == 0:
                                maria_count += 1
                            else:
                                ben_count += 1
                            player += 1
                else:
                    if check_prime(number):
                        captured_primes.append(number)
                        found = True
                        if player % 2 == 0:
                            maria_count += 1
                        else:
                            ben_count += 1
                        player += 1
            if found is False:
                if player % 2 == 0:
                    maria_count -= 1
                else:
                    ben_count -= 1
        if ben_count > maria_count:
            ben_round_wins.append(1)
            maria_round_wins.append(0)
        if maria_count > ben_count:
            maria_round_wins.append(1)
            ben_round_wins.append(0)
        if maria_count == ben_count:
            ben_round_wins.append(0)
            maria_round_wins.append(0)
    ben_points = 0
    maria_points = 0
    for i in ben_round_wins:
        ben_points += i
    for i in maria_round_wins:
        maria_points += i
    if ben_points > maria_points:
        return 'Ben'
    if ben_points < maria_points:
        return 'Maria'
    if ben_points == maria_points:
        return None


def check_prime(number):
    """checks if a number is a prime number"""
    i = 0
    if number == 1:
        return False
    for divisible in range(1, number):
        if number % divisible == 0:
            i += 1
            if i > 1:
                return False
    return True


def check_number_validity(number, captured_primes):
    """checks if a number is avaible of use of has been removed"""
    for prime_number in captured_primes:

        if number % prime_number == 0:
            return False
    return True
