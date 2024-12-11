def isWinner(x, nums):
    """
    Determines the winner of a prime number game played over x rounds.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list): A list of integers representing the upper limit (n) of the set 
                 of consecutive integers for each round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         Returns None if there is no winner.
    """
    def sieve_of_eratosthenes(n):
        """
        Generates all prime numbers up to n using the Sieve of Eratosthenes.

        Parameters:
        n (int): The upper limit for generating prime numbers.

        Returns:
        list: A list of all prime numbers less than or equal to n.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        remaining = [True] * (n + 1)  # Track numbers still available in the game
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn

        while True:
            # Find the first available prime
            prime_to_pick = None
            for prime in primes:
                if prime <= n and remaining[prime]:
                    prime_to_pick = prime
                    break

            if prime_to_pick is None:
                # No primes available, current player loses
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Mark the chosen prime and its multiples as removed
            for i in range(prime_to_pick, n + 1, prime_to_pick):
                remaining[i] = False

            # Switch turn (0 -> Maria, 1 -> Ben)
            turn = 1 - turn

    # Determine the final winner based on who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
