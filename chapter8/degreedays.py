# degreedays.py

def get_from_file():
    filename = input("Enter the file name: ")
    file = open(filename, "r")
    heat = 0
    cool = 0
    for line in file.readlines():
        temp = int(line)
        if temp > 80:
            heat += temp - 80
        elif temp < 60:
            cool += 60 - temp
    return cool, heat


def main():
    print("This program takes in a list of temperatures and computes a "
          "running total of heating- and cooling-degree-days.")
    input_type = input("Will you enter temperatures manually or in a file? ("
                       "manual/file): ")
    if input_type[0] == "f":
        cool, heat = get_from_file()
    else:
        cool = 0
        heat = 0

        while True:
            temp = input("Enter a temperature [enter to quit]: ")
            if temp == "":
                break
            temp = int(temp)
            if temp > 80:
                heat += temp - 80
            elif temp < 60:
                cool += 60 - temp
    print("The cooling-degree total is %d and the heating-degree total is %d."
          % (cool, heat))


if __name__ == '__main__':
    main()
