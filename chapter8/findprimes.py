# findprimes.py
from chapter8.prime import is_prime



def main():
    print("This program finds all primes below or equal to an inputted number.")
    num = int(input("Enter a number: "))
    primes = find_primes(num)
    print(
        "The prime numbers less than or equal to %d are: \n%s" % (num, primes))


def find_primes(num):
    primes = []
    for i in range(num + 1):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    main()
