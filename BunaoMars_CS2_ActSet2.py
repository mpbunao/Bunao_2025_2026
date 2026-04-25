#create empty list for students
students = []

#collect onfi for all 3 students
for i in range(3):
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")
    print("")

    #create a dictionary for each student
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    
    #add the student dictionary to the students list
    students.append(student)

#print all of the students information
for student in students:
    print(f"Name: {student['name']}, \n Age: {student['age']}, \n Grade: {student['grade']}")