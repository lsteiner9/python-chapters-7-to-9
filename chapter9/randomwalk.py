# randomwalk.py
from random import random


def random_walk(n):
    position = 0
    for i in range(n):
        if random() < .5:
            position -= 1
        else:
            position += 1
    return position


def main():
    print("This program simulates a number of one-dimensional random walks to "
          "see how many steps away from the starting point you end up.")
    n = int(input("Enter the number of steps to take: "))
    sims = int(input("Enter the number of simulations to run: "))
    abs_count = 0
    count = 0
    for i in range(sims):
        position = random_walk(n)
        print("Sim %d: position %d." % (i + 1, position))
        abs_count += abs(position)
        count += position
    print("The average number of steps away is %d and the average position is "
          "%d." % (abs_count / sims, count / sims))


if __name__ == '__main__':
    main()