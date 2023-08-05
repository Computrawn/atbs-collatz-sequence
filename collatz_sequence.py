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


def collatz(number: int) -> int:
    """Perform collatz sequence calculations, then print and return output."""

    if number % 2:
        number = int(3 * number + 1)
    else:
        number = int(number // 2)
    print(number)
    return number


def main() -> None:
    """Call collatz function to completion using try/except block to detect value errors."""

    while True:
        try:
            user_input = int(input("Please enter an integer greater than 1:\n"))

            if user_input <= 1:
                raise ValueError

        except ValueError:
            print("Invalid input.")

        else:
            while user_input > 1:
                user_input = collatz(user_input)
            exit()


if __name__ == "__main__":
    main()
