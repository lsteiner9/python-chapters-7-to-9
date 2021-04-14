# hours.py

def calc_pay(hours, rate):
    if hours <= 40:
        wages = hours * rate
    else:
        overtime = hours - 40
        wages = (40 * rate) + (overtime * (rate * 1.5))
    return wages


def main():
    print("This program calculates wages given the hours worked and hourly "
          "rate, assuming time-and-a-half for any hours above 40.")
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    print("You earned $%.2f this week." % calc_pay(hours, rate))


if __name__ == '__main__':
    main()