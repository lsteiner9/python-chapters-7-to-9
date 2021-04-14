# credits.py

def main():
    print("This program calculates the class of a college student based on "
          "their number of earned credits.")
    credit = int(input("Enter the number of earned credits: "))
    if credit >= 26:
        standing = "senior"
    elif credit >= 16:
        standing = "junior"
    elif credit >= 7:
        standing = "sophomore"
    else:
        standing = "freshman"
    print("This student is a", standing)


if __name__ == '__main__':
    main()
