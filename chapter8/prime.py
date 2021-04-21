# prime.py

def is_prime(num):
    divisor = 2
    prime = True
    while (divisor * divisor) <= num:
        div = num / divisor
        if int(div) == div:
            prime = False
            break
        divisor += 1
    return prime


def main():
    print("This program determines whether a inputted number is prime.")
    num = int(input("Enter an integer: "))
    prime = is_prime(num)
    if prime:
        print("%d is prime." % num)
    else:
        print("%d is not prime." % num)


if __name__ == '__main__':
    main()
