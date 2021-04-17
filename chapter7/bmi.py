# bmi.py

class WeightError(object):
    pass


class HeightError(object):
    pass


def main():
    print("This program calculates your body mass index, and evaluates "
          "whether it is in a healthy range.")
    try:
        pounds = float(input("Enter your weight in pounds: "))
        if pounds < 0:
            raise WeightError
        height = float(input("Enter your height in inches: "))
        if height < 0:
            raise HeightError
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
    except ValueError:
        print("Invalid input.")
    except HeightError:
        print("Please enter a valid height (greater than 0).")
    except WeightError:
        print("Please enter a valid weight (greater than 0).")


if __name__ == '__main__':
    main()
