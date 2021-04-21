# doubling.py


def main():
    print("This program determines how many years it takes for an investment "
          "to double.")
    interest = float(input("Enter the annual interest rate (in decimal): "))
    principal = 1  # Note: amount does not matter, start with 1
    goal = principal * 2
    count = 0
    while principal < goal:
        principal = principal + (principal * interest)
        count += 1
    print("At the rate of", interest, "it will take %d years for an "
                                      "investment to double." % count)


if __name__ == '__main__':
    main()

