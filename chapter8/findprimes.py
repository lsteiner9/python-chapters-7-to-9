# findprimes.py
from chapter8.prime import is_prime


def main():
    print("This program finds all primes below or equal to an inputted number.")
    num = int(input("Enter a number: "))
    primes = []
    for i in range(num + 1):
        if is_prime(i):
            primes.append(i)
    print(
        "The prime numbers less than or equal to %d are: \n%s" % (num, primes))


if __name__ == '__main__':
    main()
