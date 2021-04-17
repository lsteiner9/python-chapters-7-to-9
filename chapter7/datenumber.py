# datenumber.py
from chapter7.date import check_date
from chapter7.leapyear import leap_year


def get_number(date):
    elements = date.split("/")
    month = int(elements[0])
    day = int(elements[1])
    year = int(elements[2])
    leap = leap_year(year)
    day_num = (31 * (month - 1)) + day
    if month > 2:
        day_num = (day_num - ((4 * month) + 23) / 10) + 1
        if leap:
            day_num += 1
    return day_num


def main():
    print("If an inputted date is valid, this program calculates the day "
          "number: 1 through 365 (or 366).")
    date = input("Enter a date in format M/D/Y: ")
    if not check_date(date):
        print("This date or format is invalid.")
    else:
        day_num = get_number(date)
        print("The day number for %s is %d." % (date, day_num))


if __name__ == '__main__':
    main()
