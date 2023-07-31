#!/usr/bin/env python3
# collatz_sequence.py — An exercise in understanding functions.
# For more information, see README.md

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def collatz(number):
    """Perform collatz sequence calculations
    and print output until sequence completes."""

    while number != 1:
        if number % 2:
            print(int(3 * number + 1))
            number = int(3 * number + 1)
        else:
            print(int(number / 2))
            number = int(number / 2)


def main():
    """Call collatz function with try/except block to detect value errors."""

    try:
        number = int(input("Please enter an integer greater than 1: "))
        if number > 1:
            collatz(number)
        else:
            raise ValueError
    except ValueError:
        print("You must enter an integer value greater than 1 for the program to work.")


if __name__ == "__main__":
    main()
