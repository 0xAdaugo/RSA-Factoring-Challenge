#!/usr/bin/env python3
import sys

def find_prime_factor(number):
    """
    Find the smallest prime factor of a given number.

    Args:
        number (int): The input number to find the smallest prime factor for.

    Returns:
        int: The smallest prime factor of the input number.
    """
    if number <= 3:
        return int(number)
    if number % 2 == 0:
        return 2
    elif number % 3 == 0:
        return 3
    else:
        for i in range(5, int((number)**0.5) + 1, 6):
            if number % i == 0:
                return int(i)
            if number % (i + 2) == 0:
                return find_prime_factor(number // (i + 2))
    return int(number)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prime_factor_finder.py <number>")
        sys.exit(1)
    input_number = int(sys.argv[1])
    result = find_prime_factor(input_number)
    print("The smallest prime factor of", input_number, "is:", result)

