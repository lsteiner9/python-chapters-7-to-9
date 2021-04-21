# euclid.py


def main():
    print("This program finds the GCD of two values using Euclid's algorithm.")
    m = int(input("Enter an integer: "))
    n = int(input("Enter an integer: "))
    initial_m = m
    initial_n = n
    while m > 0:
        n, m = m, (n % m)
    print("The GCD of %d and %d is %d." % (initial_m, initial_n, n))


if __name__ == '__main__':
    main()
