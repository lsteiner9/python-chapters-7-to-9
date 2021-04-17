# easter.py

def main():
    print("This program determines the date of Easter in the years between "
          "1900-2099, inclusive.")
    year = int(input("Enter the year: "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
    days = d + e + 22
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        days -= 7
    if days > 31:
        days = days % 31
        print("The date of Easter in the year %d is April %d" % (year, days))
    else:
        print("The date of Easter in the year %d is March %d" % (year, days))


if __name__ == '__main__':
    main()
