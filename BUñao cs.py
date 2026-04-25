# Create an empty dictionary
student = {}

# Get user input
name = input("Enter your name: ")

# Error checking for age
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        if age > 0:
            break
        else:
            print("Age must be greater than 0. Try again.")
    else:
        print("Invalid input. Please enter a valid number.")

subject = input("Enter your favorite subject: ")

# Store data in dictionary
student["name"] = name
student["age"] = age
student["subject"] = subject

# Display output
print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Favorite Subject: {student['subject']}")
