
# Create an empty list
students = []

# Loop to collect data for 3 students
for i in range(3):
    print(f"\nEnter details for student {i + 1}")
    
    name = input("Name: ")
    
    # Error checking for age
    while True:
        age_input = input("Age: ")
        if age_input.isdigit():
            age = int(age_input)
            if age > 0:
                break
            else:
                print("Age must be greater than 0. Try again.")
        else:
            print("Invalid input. Please enter a valid number for age.")
    
    grade = input("Grade: ")
    
    # Create dictionary for each student
    student = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    
    # Add dictionary to list
    students.append(student)

# Display all student records
print("\n--- Class Directory ---")
for i, student in enumerate(students, start=1):
    print(f"\nStudent {i}:")
    print(f"Name: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Grade: {student['Grade']}")
    
