# babysitter.py

def main():
    print("This program calculates the rate of a babysitter, given the "
          "starting and ending time.")
    start = float(input("Enter the starting time (with partial hours given in "
                        "decimals): "))
    end = float(input("Enter the ending time (with partial hours given in "
                      "decimals): "))
    if 9 > end > start:
        rate = 2.5 * (end - start)
    else:
        awake_time = 9 - start
        asleep_time = (end + 12 - 9) % 12.0
        rate = (2.5 * awake_time) + (1.75 * asleep_time)
    print("The rate for this evening is $%.02f." % rate)


if __name__ == '__main__':
    main()
