# leapyear.py


def main():
    print("This program determines whether a year is a leap year.")
    year = int(input("Enter the year: "))
    if leap_year(year):
        print("%d is a leap year." % year)
    else:
        print("%d is not a leap year." % year)


def leap_year(year):
    leap = (year % 4) == 0 and not (year % 100 == 0 and year % 400 != 0)
    return leap


if __name__ == '__main__':
    main()
