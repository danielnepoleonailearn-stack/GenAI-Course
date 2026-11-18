
# STEP 1: Display the welcome message
print("Welcome to the Grade Manager!")


# STEP 2: Create an empty list to store all student records
students = []


# STEP 3: Define a function to calculate the grade based on marks
def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"


# STEP 4: Define a function to add a new student
def add_student():

    # 4.1: Get the student's name and remove unwanted spaces
    name = input("Enter student name: ").strip()

    # 4.2: Check whether the name is empty
    if not name:
        print("Student name cannot be empty.")
        return

    # 4.3: Get the student's mark and convert it into an integer
    try:
        mark = int(input("Enter student mark (0-100): "))

        # 4.4: Validate whether the mark is within the allowed range
        if mark < 0 or mark > 100:
            print("Invalid mark! Please enter a mark between 0 and 100.")
            return

    # 4.5: Handle non-numeric input
    except ValueError:
        print("Invalid input! Please enter a numeric mark.")
        return

    # 4.6: Calculate the grade by calling get_grade()
    grade = get_grade(mark)

    # 4.7: Store student details inside a dictionary
    details = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    # 4.8: Add the student dictionary to the students list
    students.append(details)

    # 4.9: Display a success message
    print(f"{name} added successfully! Grade: {grade}")


# STEP 5: Define a function to display all student results
def show_results():

    # 5.1: Check whether any student records are available
    if not students:
        print("No student records available.")
        return

    # 5.2: Display the results heading
    print("\n--------- Student Results ---------")

    # 5.3: Display the column headers with proper alignment
    print(f"{'Name':<15}{'Mark':<10}{'Grade':<10}")

    # 5.4: Print a separator line (35 hyphens)
    print("-" * 35)

    # 5.5: Iterate through each student record and display details
    for student in students:
        print(
            f"{student['name']:<15}"
            f"{student['mark']:<10}"
            f"{student['grade']:<10}"
        )

    # 5.6: Extract all student marks into a separate list
    marks = [student["mark"] for student in students]

    # 5.7: Calculate class statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # 5.8: Display the calculated statistics
    print("-" * 35)
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


# STEP 6: Create the main menu using an infinite while loop
while True:

    # 6.1: Display the available menu options
    print("\nPlease select an option:")
    print("1. Add Student")
    print("2. View Student Details")
    print("3. Quit")

    # 6.2: Get the user's menu selection
    choice = input("Enter your choice: ").strip()

    # 6.3: If the user selects 1, call add_student()
    if choice == "1":
        add_student()

    # 6.4: If the user selects 2, call show_results()
    elif choice == "2":
        show_results()

    # 6.5: If the user selects 3, exit the loop
    elif choice == "3":
        print("Thank you for using Grade Manager!")
        break

    # 6.6: Handle any invalid menu selection
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
