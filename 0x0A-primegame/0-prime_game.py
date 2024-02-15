#!/usr/bin/python3
"""prime game implementation module"""

def isWinner(x, nums):
    """returns the winner of the prime game"""
    ben = False
    maria = True
    ben_round_wins = []
    maria_round_wins = []
    for limit in nums:
        ben_count = 0
        maria_count = 0
        captured_primes = []
        for number in range(1, limit + 1):
            
            if len(captured_primes) > 0:
                if check_number_validity(number, captured_primes):
                    if check_prime(number):
                        captured_primes.append(number)
                        if ben:
                            ben_count += 1
                            ben = False
                            maria = True
                        if maria:
                            maria_count += 1
                            maria = False
                            ben = True
            else:
                if check_prime(number):
                    captured_primes.append(number)
                    if ben:
                        ben_count += 1
                        ben = False
                        maria = True
                    if maria:
                        maria_count += 1
                        maria = False
                        ben = True
        print(captured_primes)
        if ben_count > maria_count:
            ben_round_wins.append(1)
            maria_round_wins.append(0)
        if maria_count > ben_count:
            maria_round_wins.append(1)
            ben_round_wins.append(0)
        if maria_count == ben_count:
            ben_round_wins.append(0)
            maria_round_wins.append(0)
    print(ben_round_wins)
    print(maria_round_wins)
    return 'Ben'

def check_prime(number):
    """checks if a number is a prime number"""
    i = 0;
    if number == 1:
        return False
    for divisible in range(1, number):
        if number % divisible == 0:
            i += 1
            if i > 1:
                return False;
    return True

def check_number_validity(number, captured_primes):
    """checks if a number is avaible of use of has been removed"""
    for prime_number in captured_primes:

        if number % prime_number == 0:
            return False
    return True
