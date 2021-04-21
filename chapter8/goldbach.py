# goldbach.py
from chapter8.findprimes import find_primes


def main():
    print("This program finds one or more sets of two prime numbers that sum "
          "to the inputted even number, according to the Goldbach conjecture.")
    num = int(input("Enter an even number: "))
    while num % 2 != 0:
        num = int(input("That number is not even. Enter a number divisible "
                        "by 2: "))
    primes = find_primes(num)
    index = len(primes) - 1
    found = False
    for i in range(len(primes)):
        prime1 = primes[i]
        prime2 = primes[index]
        while index > i:
            if prime1 + prime2 == num:
                found = True
                print("Two primes that sum to %d are %d and %d." % (num, prime1, prime2))
                break
            elif prime1 + prime2 > num:
                index -= 1
                prime2 = primes[index]
            else:
                index = len(primes) - 1
                break
    if not found:
        print("Could not find primes that sum to %d." % num)


if __name__ == '__main__':
    main()