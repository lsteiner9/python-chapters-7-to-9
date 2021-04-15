# bmi.py

def main():
    print("This program calculates your body mass index, and evaluates "
          "whether it is in a healthy range.")
    pounds = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = (pounds * 720) / (height * height)
    if bmi > 25:
        print("Your body mass index is %.2d. This is above the "
              "healthy range." % bmi)
    elif bmi < 19:
        print("Your body mass index is %.2d. This is below the "
              "healthy range." % bmi)
    else:
        print("Your body mass index is %.2d. This is within the "
              "healthy range." % bmi)


if __name__ == '__main__':
    main()
