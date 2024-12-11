#!/usr/bin/python3

def is_winner(x, nums):
    """Determine the winner of the prime game after x rounds."""
    
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    
    # Sieve of Eratosthenes to find all primes up to max_n
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # List of all prime numbers up to max_n
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    def count_primes_up_to(n):
        """Count primes <= n using the sieve."""
        return len([p for p in primes if p <= n])

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        primes_count = count_primes_up_to(n)
        # Maria goes first; if primes_count is odd, Maria wins (she gets the last pick).
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
