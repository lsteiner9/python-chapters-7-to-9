# date.py
from chapter7.leapyear import leap_year


def main():
    print("This program determines whether an inputted date is valid.")
    date = input("Enter a date in format M/D/Y: ")
    valid = check_date(date)
    if valid:
        print("%s is a valid date." % date)
    else:
        print("%s is not a valid date." % date)


def check_date(date):
    elements = date.split("/")
    valid = True
    if len(elements) != 3:
        valid = False
    else:
        month_lengths = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                         9: 30, 10: 31, 11: 30, 12: 31}
        month = int(elements[0])
        day = int(elements[1])
        year = int(elements[2])
        leap = leap_year(year)
        if month > 12 or month < 0:
            valid = False
        elif day < 0 or day > 31:
            valid = False
        elif day > month_lengths[month]:
            valid = leap and month == 2 and day == 29
    return valid


if __name__ == '__main__':
    main()
