# windchill.py

def chill(temp, speed):
    return 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (
        0.4275 * temp * (speed ** 0.16))


def main():
    print("This program prints out a table of windchill values from 0-50 mph "
          "and -20 to +60 degrees Fahrenheit.\n")
    print("      % 3.2f  % 3.2f  % 3.2f  % 3.2f  % 3.2f  % 3.2f  % 3.2f  "
          "% 3.2f  % 3.2f deg. F\n"
          % (-20, -10, 0, 10, 20, 30, 40, 50, 60))  # temp labels
    print("%2d    % 3.2f  % 3.2f  % 3.2f  % 3.2f  % 3.2f  % 3.2f  % 3.2f  "
          "% 3.2f  % 3.2f" %
          (0, -20, -10, 0, 10, 20, 30, 40, 50, 60))  # zero wind
    for i in range(5, 51, 5):
        print("%2d    % -3.2f  % -3.2f  % -3.2f  % -3.2f  % -3.2f  % -3.2f  "
              "% -3.2f  % -3.2f  % -3.2f" %
              (i, chill(-20, i), chill(-10, i), chill(0, i), chill(10, i),
               chill(20, i), chill(30, i), chill(40, i), chill(50, i),
               chill(60, i)))


if __name__ == '__main__':
    main()
