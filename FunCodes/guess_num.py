# -*- coding:utf-8 -*-

import random

def guess_num(min, max, times):
    # generate a number
    number = random.randint(min, max)
    print("The right answer is between %d and %d" % (min, max))
    # start guess
    for i in range(times):
        answer = int(input("Please enter a number:"))
        if answer == number:
            print("Yes, you are right, you are so clever!")
            return True
        elif answer > number:
            print("The right answer is smaller than your guess, please try again.")
        elif answer < number:
            print("The right answer is bigger than your guess, please try again.")

    print("retry out, you are failed!")
    return False

if __name__ == "__main__":
    guess_num(1, 10, 5)