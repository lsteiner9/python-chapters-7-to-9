# speedingticket.py

def main():
    print("This program calculates the value of a speeding ticket in a "
          "fictional town, given the speed limit and the clocked speed.")
    speed_limit = int(input("Enter the speed limit: "))
    speed = int(input("Enter the clocked speed: "))
    if speed <= speed_limit:
        print("This speed is legal.")
    else:
        base_fine = 50
        if speed > 90:
            base_fine += 200
        fine = base_fine + (5 * (speed - speed_limit))
        print("The ticket amount is $%.2d." % fine)


if __name__ == '__main__':
    main()
