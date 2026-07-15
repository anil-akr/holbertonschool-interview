#!/usr/bin/python3
"""Prime Game: determine the winner of the prime-picking game."""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the Prime Game.

    Removing a prime and its multiples never removes another prime, so the
    number of moves in a round equals the number of primes <= n. The player
    making the last move wins, so the parity of that prime count decides the
    round: odd -> Maria (first player), even -> Ben.

    Args:
        x (int): number of rounds.
        nums (list): list of n values, one per round.

    Returns:
        str or None: "Maria", "Ben", or None if it cannot be decided.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes: is_prime[i] is True when i is prime.
    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    if max_n >= 1:
        is_prime[1] = False
    for number in range(2, max_n + 1):
        if is_prime[number]:
            for multiple in range(number * number, max_n + 1, number):
                is_prime[multiple] = False

    # Prefix count: prime_count[i] = number of primes <= i.
    prime_count = [0] * (max_n + 1)
    for index in range(1, max_n + 1):
        prime_count[index] = prime_count[index - 1]
        if is_prime[index]:
            prime_count[index] += 1

    # Each round: odd prime count -> Maria wins, even -> Ben wins.
    maria_wins = 0
    ben_wins = 0
    for limit in nums:
        if prime_count[limit] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
