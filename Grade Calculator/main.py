def calculate():
    while True:
        try:
            students_no = int(input("Enter the number of students: "))
            if students_no <= 0:
                raise ValueError("Number of students must be greater than zero.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    total = 0

    for i in range(students_no):
        while True:
            try:
                marks = float(input(f"Enter the marks of student {i+1}: "))
                if marks < 0 or marks > 100:
                    raise ValueError("Marks should be between 0 and 100.")
                total += marks
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
    average = total / students_no
    print(f"\nThe average marks of {students_no} students is {average:.2f}")

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
calculate()
