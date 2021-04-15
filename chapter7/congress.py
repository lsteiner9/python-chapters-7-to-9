# congress.py

def main():
    print("This program determines if you are eligible to be a US Senator or "
          "a US representative.")
    age = int(input("Enter your age: "))
    citizenship = int(input("Enter the number of years you have been a US "
                            "citizen: "))
    senator = age >= 30 and citizenship >= 9
    rep = age >= - 25 and citizenship >= 7
    if senator:
        print("You are eligible to be a US Senator or a US Representative.")
    elif rep:
        print(
            "You are eligible to be a US Representative but not a US Senator.")
    else:
        print("You are not yet eligible to be in the US Congress.")


if __name__ == '__main__':
    main()
