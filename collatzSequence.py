# This program asks the user to input an integer and calls collatz() until the function returns the value 1.


def collatz(number):
    while number != 1:
        if number % 2 == 1:
            print(int(3 * number + 1))
            number = int(3 * number + 1)
        else:
            print(int(number / 2))
            number = int(number / 2)


print("Please enter an integer value: ")

try:
    collatz(int(input()))
except:
    print("You must enter an integer for the program to work.")
