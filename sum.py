#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program finds the sum of all natural numbers preceding the
#     number inputted by the user


def main():
    # This function finds the sum of all natural numbers preceding the
    #     number inputted by the user

    # Input
    counter = 0
    sum = 0
    natural_string = input("Enter a natural number (To Find Sum 1 to N): ")
    print("")

    # Process & Output
    try:
        natural_integer = int(natural_string)
    except Exception:
        print("You have not inputted an integer, please input an integer"
              " (natural number)!")
    else:
        if natural_integer <= 0:
            print("You have not inputted a natural number, please input a"
                  " natural number!")
        else:
            while counter <= natural_integer:
                sum = sum + counter
                counter = counter + 1
            print("The Sum of all natural numbers 1 to {0} is {1}"
                  .format(natural_integer, sum))


if __name__ == "__main__":
    main()
