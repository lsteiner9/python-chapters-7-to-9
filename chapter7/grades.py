# grades.py

def quiz():
    print("This program determines the letter grade for a quiz based on the "
          "number of points received.")
    num = int(input("Enter the number of points (0-5): "))
    if num > 3:
        if num == 5:
            grade = "A"
        else:
            grade = "B"
    else:
        if num == 3:
            grade = "C"
        elif num == 2:
            grade = "D"
        else:
            grade = "F"
    print("The letter grade is", grade)


def exam():
    print("This program determines the letter grade for an exam based on the "
          "number of points received.")
    num = int(input("Enter the number of points (0-100): "))
    if num > 69:
        if num >= 90:
            grade = "A"
        elif num >= 80:
            grade = "B"
        else:
            grade = "C"
    else:
        if num >= 60:
            grade = "D"
        else:
            grade = "F"
    print("The letter grade is", grade)


def main():
    grade = input("Do you want quiz (Q) or exam (E) grades? ")
    if grade == "E" or grade == "e":
        exam()
    elif grade == "Q" or grade == "q":
        quiz()
    else:
        print("Incorrect type.")


if __name__ == '__main__':
    main()
