# mpg.py


def get_from_file():
    odo_readings = []
    gas_usages = []
    filename = input("Enter filename: ")
    file = open(filename, "r")
    for line in file.readlines():
        data = line.split()
        if len(data) > 0:
            odo_readings.append(data[0])
        if len(data) > 1:
            gas_usages.append(data[1])
    return odo_readings, gas_usages


def main():
    print("This program computes the fuel efficiency of a multi-leg journey.")
    file = input("Is your input from a file or will you do it manually? (f/m)")
    if file[0] == "f":
        odo_readings, gas_usages = get_from_file()
    else:
        odo_readings = [int(input("Enter the initial odometer reading: "))]
        gas_usages = []
        while True:
            new_line = input("Enter the current odometer reading and the "
                             "amount of gas used, separated by a space. ["
                             "Enter to quit] ")
            if new_line == "":
                break
            data = new_line.split()
            odo_readings.append(int(data[0]))
            gas_usages.append(float(data[1]))
    mpgs = []
    for i in range(len(odo_readings) - 1):
        miles = odo_readings[i + 1] - odo_readings[i]
        mpg = miles / gas_usages[i]
        mpgs.append(mpg)
        print("Leg %d: miles per gallon is %.2f." % (i + 1, mpg))
    count = 0
    for i in range(len(mpgs)):
        count += mpgs[i]
    average = count / len(mpgs)
    print("Average miles per gallon over trip: %.2f." % average)


if __name__ == '__main__':
    main()