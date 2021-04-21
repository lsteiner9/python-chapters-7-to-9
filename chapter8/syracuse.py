# syracuse.py


def main():
    print(
        "This program prints the Syracuse sequence based on a starting value.")
    start = int(input("Enter a starting value (must be a natural number): "))
    sequence = [start]
    while start != 1:
        if (start % 2) == 0:
            start = int(start / 2)
        else:
            start = (3 * start) + 1
        sequence.append(start)
    print("The Syracuse sequence starting on %d is: \n" % (sequence[0]),
          sequence)


if __name__ == '__main__':
    main()
